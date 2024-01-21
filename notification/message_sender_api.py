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

    def get_url(self, message_id: int):
        return f"{self.path}/{message_id}"

    def __call__(self, **body: Unpack[Message]):
        try:
            data = json.dumps(body).encode("utf-8")
            url = self.get_url(body["id"])
            req = request.Request(
                url,
                data=data,
                headers=self.headers,
                method=self.method,
            )
            logger.info(f"Sending request to {url} with data: {data}")
            with request.urlopen(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                logger.debug(f"Received response: {response_data}")
                if response_data.get("message") != "OK":
                    raise MessageSenderApiException("Response: Not equal to 'OK'")
        except error.URLError as e:
            message = f"Request failed: {e}"
            logger.error(message)
            raise MessageSenderApiException(message)
        except json.JSONDecodeError as e:
            message = f"Failed to parse JSON response: {e}"
            logger.error(message)
            raise MessageSenderApiException(message)


message_sender_api = MessageSenderApi(
    path=MESSAGE_SENDER_API_PATH, token=MESSAGE_SENDER_API_TOKEN
)

if __name__ == "__main__":
    try:
        result = message_sender_api(id=1, phone=79834567233, text="Test")
        logger.info(f"API call result: {result}")
    except MessageSenderApiException as e:
        logger.error(f"MessageSenderApiException: {e}")
