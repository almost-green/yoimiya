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
from flask import Flask, request, abort  # 匯入 Flask 庫中的 Flask 類別、request 對象和 abort 函數
from linebot import WebhookHandler, LineBotApi  # 匯入 LINE SDK 的 WebhookHandler 和 LineBotApi
from linebot.models import MessageEvent, TextMessage  # 匯入 LINE SDK 中的 MessageEvent 和 TextMessage 類別
# from keys import line_access_token, line_channel_secret
app = Flask(__name__)  # 創建一個 Flask 應用實例，__name__ 表示當前模塊名稱

# 這裡填入你的 LINE Channel 的密鑰
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)  # 創建 LineBotApi 實例，傳入你的 Channel Access Token
handler = WebhookHandler(LINE_CHANNEL_SECRET)  # 創建 WebhookHandler 實例，傳入你的 Channel Secret

@app.route("/", methods=['POST'])  # 設置路由，當 POST 請求發送到根目錄執行根目錄函數
def callback():  # 定義 callback 函數，這是處理 LINE 事件的核心函數
    # 獲取 Webhook 事件的簽名
    signature = request.headers['X-Line-Signature']  # 從請求標頭中提取 X-Line-Signature，用來驗證請求來源
    body = request.get_data(as_text=True)  # 獲取請求的內容，並將其轉換為文本格式

    try:
        handler.handle(body, signature)  # 處理 Webhook 事件，傳入事件內容和簽名
    except Exception as e:
        abort(400)  # 如果處理過程中出現錯誤，返回 400 錯誤，並中止執行

    return 'OK'  # 返回 OK 以表示成功處理請求

@handler.add(MessageEvent, message=TextMessage)  # 當接收到 TextMessage 類型的消息事件時，執行 handle_message 函數
def handle_message(event):  # 定義處理消息的函數，這裡會對收到的消息做回覆
    line_bot_api.reply_message(  # 使用 LineBotApi 的 reply_message 方法回覆消息
        event.reply_token,  # 傳入回覆的 token，用於標識此次回應的事件
        TextMessage(text="Hello, this is a response from your bot!")  # 回覆的消息內容，這裡是簡單的文字消息
    )

if __name__ == "__main__":  # 檢查這段代碼是否在主程序中運行
    app.run(debug=True)  # 啟動 Flask 應用，debug=True 開啟調試模式，這樣可以在開發過程中快速查看錯誤

