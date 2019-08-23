from operations import user, bot
import logging

VERIFY_TOKEN = "EAAiVr97oPH4BAPINDhZC7ZC7cZCRghP2KsZBRKRgLnnj6P6TFhGYibtipjYooEU2z0fCYPyANdsnNiFsXjTwVbQaaFymloylQskTmI3BZC0jLBOC4H7t7eydeLWM7UKnLXCEg1ZCZCXPOrPgZAVOhQoT4x7Dxb57hfmyRIxh4JD2LIQQw5cKZCZAIZA"

def verify_webhook(req):
    token = req.args.get("hub.verify_token")
    logging.debug(f"the verify token is {token}")
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        logging.info('webhook challange was successful')
        return req.args.get("hub.challenge")
    else:
        logging.warning('webhook challange failed')
        return "incorrect"

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = bot.get_bot_response(message)
    tup = sender, response
    return tup

def return_response(payload):
    print(f"calling return response") 
    event = payload['entry'][0]['messaging']
    final_tuple = None
    for x in event:
        if user.is_user_message(x):
            text = x['message']['text']
            sender_id = x['sender']['id']
            final_tuple = respond(sender_id, text)
    return final_tuple