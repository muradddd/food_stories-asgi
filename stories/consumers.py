import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import *

created_review = []

class CommentConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        self.story_id = self.scope['url_route']['kwargs']['pk']
        self.room = f'room_{self.story_id}'
        await self.channel_layer.group_add(
            self.room, # unique channel id
            self.channel_name # default attribute
        )
        await self.send({
            'type':"websocket.accept",
        })

    async def websocket_receive(self, event):
        print("receive", event)
        recived_data = json.loads(event.get('text'))
        comment_text = recived_data.get('text')
        user = self.scope['user']
        story = await self.get_story(self.story_id)
        parent_id = recived_data.get('parent_id')
        if parent_id != '':
            parent = await self.get_parent(int(parent_id))
            await self.create_comment(comment_text, user, story, parent)
        else:
            await self.create_comment(comment_text, user, story)
      
        await self.channel_layer.group_send(
            self.room,
            {
                'type':'comment_message',
                'text':json.dumps(self.data_response),
            }
        )

    async def comment_message(self, event):
         await self.send({
            'type':'websocket.send',
            'text':event['text'],
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)

    @database_sync_to_async
    def get_story(self, id):
        return Story.objects.get(id=id)

    @database_sync_to_async
    def get_parent(self, id):
        return Comment.objects.get(id=id)

    @database_sync_to_async
    def create_comment(self, text, user, story, parent=None):
        new_comment = Comment.objects.create(text=text, parent=parent, user=user, story=story)
        comment_id = new_comment.id
        text = new_comment.text
        first_name = new_comment.user.first_name
        last_name = new_comment.user.last_name
        if new_comment.parent:
            parent_id = new_comment.parent.id
        else:
            parent_id = ''
        updated_at = new_comment.updated_at
        self.data_response = {
            'comment_id' : comment_id,
            'text' : text,
            'first_name' : first_name,
            'last_name' : last_name,
            'parent_id' : parent_id,
            'updated_at' : str(updated_at),
        }
        return new_comment