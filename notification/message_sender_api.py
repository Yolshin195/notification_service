import requests


class MessageSenderApi:
    def __init__(self, path, token):
        self.path = path
        self.headers = {
            'content-type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    def __call__(self, message_id: int, phone: int, text: str) -> bool:
        try:
            body = {
                'id': message_id,
                'phone': phone,
                'text': text
            }
            response = requests.post(f"{self.path}/{message_id}", json=body, headers=self.headers)
            return True if response.json()['message'] == 'OK' else False
        except:
            return False


message_sender_api = MessageSenderApi(path="https://probe.fbrq.cloud/v1/send", token="your token")

if __name__ == "__main__":
    r = message_sender_api(1, 79834567233, 'Test')
    print(r)
