from Keys import line_access_token, line_channel_secret
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time
app = Flask(__name__)
@app.route("/", methods=['POST']) #
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(line_access_token)
        handler = WebhookHandler(line_channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data['events'][0]['replyToken']
        user_id = json_data['events'][0]['source']['userId']
        print(json_data)
        if 'message' in json_data['events'][0]:
            if json_data['events'][0]['message']['type'] == 'text':
                text = json_data['events'][0]['message']['text']
                if text == '雷達回波圖' or text == '雷達回波':
                    radar_url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
                    radar = requests.get(radar_url)
                    json1=radar.json()
                    img1=json1['cwaopendata']['dataset']['resource']['ProductURL']
                    reply_image(img1, reply_token, line_access_token)
    except:
        print('error')
    return 'OK'


def reply_image(msg, rk, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    body = {
        'replyToken': rk,
        'messages': [{
            'type': 'image',
            'originalContentUrl': msg,
            'previewImageUrl': msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,
                           data=json.dumps(body).encode('utf-8'))
    print(req.text)


if __name__ == "__main__":
    app.run()