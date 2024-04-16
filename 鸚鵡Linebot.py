# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('s9tMj/mYxr1ykK/DnJnaqLYoMVLRX+J+ccLf58/dm5GnkWhBhasKM6jVKGYZ95AFcmItzlifPjube2ePkYMn8Mu+vo9FgRwlxEh7Wcn2Xh3oN09OqHHpnNxG1WAdg6lhe4z6sPA/4MenL4EjpFyibAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f3cea207b0af0ea05db52902408f75e4')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError: 
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=event.message.text))
    
if __name__ == '__main__':
    app.run()