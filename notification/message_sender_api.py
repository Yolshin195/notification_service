import os
from typing import TypedDict, Unpack
from urllib import request, error
from logging import getLogger
import json

logger = getLogger(__name__)

MESSAGE_SENDER_API_PATH = os.getenv("MESSAGE_SENDER_API_PATH")
MESSAGE_SENDER_API_TOKEN = os.getenv("MESSAGE_SENDER_API_TOKEN")


class MessageSenderApiException(Exception):
    """Exception raised for errors in the MessageSenderApi."""


class Message(TypedDict):
    id: int
    phone: int
    text: str


class MessageSenderApi:
    def __init__(self, path, token):
        self.path = path
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        self.method = "POST"

    def __call__(self, **body: Unpack[Message]):
        req = self.build_request(body)
        response = self.send_request(req)
        if response.get("message") != "OK":
            raise MessageSenderApiException("Response: Not equal to 'OK'")

    def build_request(self, body: Message):
        url = f"{self.path}/{body["id"]}"
        data = json.dumps(body).encode("utf-8")
        return request.Request(
            url,
            data=data,
            headers=self.headers,
            method=self.method,
        )

    @staticmethod
    def send_request(req):
        logger.info(f"Sending request to {req.full_url} with data: {req.data}")
        try:
            with request.urlopen(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                logger.debug(f"Received response: {response_data}")
                return response_data
        except error.URLError as url_error:
            message = f"Request failed: {url_error}"
            logger.error(message)
            raise MessageSenderApiException(message)
        except json.JSONDecodeError as json_decode_error:
            message = f"Failed to parse JSON response: {json_decode_error}"
            logger.error(message)
            raise MessageSenderApiException(message)


message_sender_api = MessageSenderApi(
    path=MESSAGE_SENDER_API_PATH, token=MESSAGE_SENDER_API_TOKEN
)

if __name__ == "__main__":
    try:
        result = message_sender_api(id=1, phone=79834567233, text="Test")
        logger.info(f"API call result: {result}")
    except MessageSenderApiException as api_exception:
        logger.error(f"MessageSenderApiException: {api_exception}")
