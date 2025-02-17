# import requests
# from keys import line_notify_key
# url="https://notify-api.line.me/api/notify"
# token=line_notify_key
# headers={'Authorization':'Bearer '+token}   #headers(標頭)的形式為{'Authorization':'Bearer '+token}
# data={'message':'<3'}
# data=requests.post(url,headers=headers,data=data)



# from keys import line_access_token, line_channel_secret
# from flask import Flask, request
# from linebot import LineBotApi, WebhookHandler
# from linebot.models import MessageEvent, TextMessage, TextSendMessage
# import requests, json, time
# app = Flask(__name__)
# @app.route("/",method=['POST'])
# def linebot():
#     body = request.get_data(as_text=True)
#     try:
#         line_bot_api = LineBotApi(line_access_token)
#         handler = WebhookHandler(line_channel_secret)
#         signature = request.headers['X-Line-Signature']
#         handler.handle(body, signature)
#         json_data = json.loads(body)
#         reply_token = json_data['events'][0]['replyToken']
#         user_id = json_data['events'][0]['source']['userId']
#         print(json_data)
#         if 'message' in json_data['events'][0]:
#             if json_data['events'][0]['message']['type'] == 'text':
#                 text = json_data['events'][0]['message']['text']
#                 if text == '雷達回波圖' or text == '雷達回波':
#                     radar_url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
#                     radar = requests.get(radar_url)
#                     json1=radar.json()
#                     img1=json1['cwaopendata']['dataset']['resource']['ProductURL']
#                     reply_image(img1, reply_token, line_access_token)
#     except:
#         print('error')
#     return 'OK'



from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from keys import line_access_token, line_channel_secret

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        line_bot_api = LineBotApi(line_access_token)              # 確認 token 是否正確
        handler = WebhookHandler(line_channel_secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            reply = msg
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()