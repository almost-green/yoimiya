from flask import Flask, request
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from Keys import line_access_token, line_channel_secret
app=Flask(__name__)
@app.route('/',methods=['POST'])
def linebot():
    body=request.get_data(as_text=True)
    json_data=json.loads(body)
    print('json_data:\n',json_data)
    try:
        line_bot_api=LineBotApi(line_access_token)
        handler=WebhookHandler(line_channel_secret)
        signature=request.headers['X-Line-Signature']
        handler.handle(body,signature)
        tk=json_data['events'][0]['replyToken']
        msg=json_data['events'][0]['message']['text']
        print('json_Data:\n')
        print(json_data)
        text_message=TextSendMessage(text=msg)
        line_bot_api.reply_message(tk,text_message)
    except Exception as e:
        print('error')
        print(e)
    return 'ok'
if __name__=='__main__':
    app.run()    
