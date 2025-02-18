import os
from flask import Flask, request, abort  # 匯入 Flask
from linebot import WebhookHandler, LineBotApi  # 匯入 LINE SDK
from linebot.models import MessageEvent, TextMessage, TextSendMessage  # 匯入 LINE SDK 模型

app = Flask(__name__)  # 創建 Flask 應用實例

# **從環境變數讀取 LINE Bot 密鑰**
line_access_token = os.getenv("LINE_ACCESS_TOKEN")  
line_channel_secret = os.getenv("LINE_CHANNEL_SECRET")  

line_bot_api = LineBotApi(line_access_token)  # 創建 LineBotApi 實例
handler = WebhookHandler(line_channel_secret)  # 創建 WebhookHandler 實例

@app.route("/", methods=['POST'])  # 設置 webhook 路由
def callback():  
    signature = request.headers['X-Line-Signature']  # 獲取請求簽名
    body = request.get_data(as_text=True)  # 獲取請求內容

    try:
        handler.handle(body, signature)  # 處理 Webhook 事件
    except Exception as e:
        abort(400)  

    return 'OK'  # 回應 LINE 伺服器

@handler.add(MessageEvent, message=TextMessage)  # 當收到 TextMessage 事件時執行
def handle_message(event):  
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello, this is a response from your bot!")  # 這裡的 `TextMessage` 需改成 `TextSendMessage`
    )

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)  
