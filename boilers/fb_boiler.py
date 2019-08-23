import requests

HOST_URL = "graph.facebook.com"
APP_ID = "2416382405262462"
PAGE_ACCESS_TOKEN = "EAAiVr97oPH4BAPINDhZC7ZC7cZCRghP2KsZBRKRgLnnj6P6TFhGYibtipjYooEU2z0fCYPyANdsnNiFsXjTwVbQaaFymloylQskTmI3BZC0jLBOC4H7t7eydeLWM7UKnLXCEg1ZCZCXPOrPgZAVOhQoT4x7Dxb57hfmyRIxh4JD2LIQQw5cKZCZAIZA"
FB_API_URL = 'https://graph.facebook.com/v4.0/me/messages'

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()