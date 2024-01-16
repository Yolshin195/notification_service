from typing import TypedDict, Unpack
from urllib import request, error
from logging import getLogger
import json

from django.conf import settings

logger = getLogger(__name__)


class Message(TypedDict):
    id: int
    phone: int
    text: str


class MessageSenderApi:
    def __init__(self, path, token):
        self.path = path
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        self.method = 'POST'

    def get_url(self, message_id: int):
        return f"{self.path}/{message_id}"

    def __call__(self, **body: Unpack[Message]) -> bool:
        try:
            data = json.dumps(body).encode('utf-8')
            req = request.Request(self.get_url(body['id']), data=data, headers=self.headers, method=self.method)
            with request.urlopen(req) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                return True if response_data.get('message') == 'OK' else False
        except error.URLError as e:
            logger.error(f"Request failed: {e}")
            return False
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            return False


message_sender_api = MessageSenderApi(path=settings.MESSAGE_SENDER_API_PATH, token=settings.MESSAGE_SENDER_API_TOKEN)

if __name__ == "__main__":
    r = message_sender_api(id=1, phone=79834567233, text='Test')
    print(r)
