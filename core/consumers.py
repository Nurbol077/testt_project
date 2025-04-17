import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'WebSocket байланыш ийгиликтүү түзүлдү!'
        }))

    async def disconnect(self, close_code):
        print("WebSocket үзүлдү.")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', 'Билдирүү жок')
        await self.send(text_data=json.dumps({
            'message': f'Сиз жибердиңиз: {message}'
        }))