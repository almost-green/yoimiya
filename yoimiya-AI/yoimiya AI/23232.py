from flask import Flask, request, abort
from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent, TextMessage, TextMessage
from keys import line_access_token, line_channel_secret
app = Flask(__name__)

# 這裡填入你的LINE Channel的密鑰
line_bot_api = LineBotApi(line_access_token)
handler = WebhookHandler(line_channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    # 獲取Webhook事件
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text="Hello, this is a response from your bot!")
    )

if __name__ == "__main__":
    app.run(debug=True)