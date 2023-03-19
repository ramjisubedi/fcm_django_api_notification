import firebase_admin
from firebase_admin import credentials, messaging
from fcm_nonitication import settings


cred = credentials.Certificate(settings.cred)
firebase_admin.initialize_app(cred)

def sendPush(title, msg, registration_token, dataObject=None):
    dataObject = {'routeKey':"homework"}
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title,body=msg),
        data=dataObject,
        tokens=registration_token
    )
    response = messaging.send_multicast(message)
    print(message)
    print('successfully sent message', response)

def test_send():
    # This registration token comes from the client FCM SDKs.
    registration_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MDQ2NjIzLCJpYXQiOjE2Nzg5NjAyMjMsImp0aSI6ImQ1MGM1N2I4NTdmYjQ3YjM4NGM4YWRmOTE1OTQ3MmU3IiwidXNlcl9pZCI6NX0.jizco1_O6dxMYMv6y9Pxb3hPKgqWSJdylmv1dVYq2Q8'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)