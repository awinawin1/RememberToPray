from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re
import requests, json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('/52Vu4/OPS4F/WVMJTvm/F/g3gOnuIwvZneoJaSxVI2YkIAMYUaZhoPcWWjMmmts/B3ucawJAu6nf9VKP+9INrOfUD6cEaAIpY9pCC/QlygrK3Fy/7eADZmycdxgK0liDojDNy3lRIu+NpWV/4a7ggdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('528d87d1aebfb8fb9a247b280de8a912')
#===========[ NOTE SAVER ]=======================
notes = {}

#input mencari
def cariteman(kota):
    URLteman = "https://time.siswadi.com/timezone/" + kota
    r = requests.get(URLteman)
    data = r.json()
    # print(data)
    status = data['time']['timezone']
    jam = data['time']['time']
    print("Daerah : " + status + "\n" + "Jam sholat : " + jam)
cariteman("Bandung")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receive message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

data=text.split('-')
if(data[0]=='new'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cariteman(data[1])))
    
   
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)