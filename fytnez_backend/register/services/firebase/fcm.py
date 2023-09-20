from typing import List
from firebase_admin import messaging, credentials
import firebase_admin


class FcmService:
    def __init__(self):
        creds = credentials.Certificate(
            "../../../configs/fytnez_firebase_private_key.json"
        )
        default_app = firebase_admin.initialize_app(creds)

    def send_to_token(self, fcm_token: str, title: str, body: str, data: dict = None):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            token=fcm_token,
        )
        response = messaging.send(message)
        print(response)
        return response

    def send_to_token_multicast(
        self, fcm_token_list: List[str], title: str, body: str, data: dict = None
    ):
        assert isinstance(fcm_token_list, list)

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            token=fcm_token_list,
        )
        response = messaging.send_multicast(message)
        print(response)
        return response

    def send_to_topic(self, topic: str, title: str, body: str, data: dict = None):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            topic=topic,
        )
        response = messaging.send(message)
        print(response)
        return response
