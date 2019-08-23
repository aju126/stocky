from flask import Flask, request
from boilers import bot_boiler, fb_boiler
import logging;

app = Flask(__name__)

@app.route("/health")
def health_check():
    return "working"

@app.route("/webhook", methods=['GET','POST'])
def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return bot_boiler.verify_webhook(request)

    if request.method == 'POST':
        print(f"sending post request")
        request_object = request.json
        tup = bot_boiler.return_response(request_object)
        print(f"the bot boiler returned a tuple : {tup}")
        if(tup != None):
            fb_boiler.send_message(tup[0], tup[1])
    return "ok"