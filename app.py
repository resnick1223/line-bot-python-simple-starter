# 引入flask模組
from flask import Flask, request, abort
# 引入linebot相關模組
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

# MessageEvent: 收到訊息的處理器
# TextMessage: 接收使用者文字訊息的處理器
# StickerMessage: 接收使用者貼圖訊息的處理器
# TextSendMessage: 回傳文字訊息的處理器
# StickerSendMessage: 回傳貼圖訊息的處理器
# 如需增加其他處理器請參閱以下網址的 Message objects 章節
# https://github.com/line/line-bot-sdk-python
from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, StickerSendMessage
)

# 定義應用程式是一個Flask的實例
app = Flask(__name__)
print("[程式開始運行]")

# LINE的Webhook為了辨識開發者身份所需的資料
# 設定linebot messeging API的access token與channel secret
# 相關訊息進入網址(https://developers.line.me/console/)
# 登入選擇Messaging API建立後即可取得channel secret與access token
CHANNEL_ACCESS_TOKEN = '請將此字串置換成你的 CHANNEL_ACCESS_TOKEN'
CHANNEL_SECRET = '請將此字串置換成你的 CHANNEL_SECRET'


# ================== 以下為 X-LINE-SIGNATURE 驗證程序 ==================

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# 當LINE收到使用者傳的訊息後將會Post到
# https://你的應用程式網址/callback
# 並在此過程中驗證你的應用程式是否合法
# 以下的callback()函式不需做修改
@app.route("/callback", methods=['POST'])
def callback():
    # 當LINE發送訊息給機器人時，從header取得 X-Line-Signature
    # X-Line-Signature 用於驗證頻道是否合法
    signature = request.headers['X-Line-Signature']
    print('[REQUEST]')
    print(request)
    print('[SIGNATURE]')
    print(signature)

    # 將取得到的body內容轉換為文字處理
    body = request.get_data(as_text=True)
    print("[BODY]")
    print(body)
    app.logger.info("Request body: " + body)

    # 一但驗證合法後，將body內容傳至handler
    try:
        print('[try]')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('[except]')
        abort(400)

    return 'OK'

# ================== 以上為 X-LINE-SIGNATURE 驗證程序 ==================


# ========== 文字訊息傳入時的處理器 ==========
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當有文字訊息傳入時
    # event.message.text : 使用者輸入的訊息內容
    print('[使用者傳入文字訊息]')
    print(str(event))
    # 準備要回傳的訊息
    # HINT: TextSendMessage(text="機器人要回傳給使用者的訊息")
    reply = TextSendMessage(text='你剛才說的是' + event.message.text)

    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        reply)


# ========== 貼圖訊息傳入時的處理器 ==========
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # 當有貼圖訊息傳入時
    print('[使用者傳入貼圖訊息]')
    print(str(event))

    # 準備要回傳的貼圖訊息
    # HINT: 機器人可用的貼圖 https://devdocs.line.me/files/sticker_list.pdf
    reply = StickerSendMessage(package_id='2', sticker_id='149')

    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        reply)


import os
if __name__ == "__main__":
    print('[伺服器開始運行]')
    # 取得遠端環境使用的連接端口，若是在本機端測試則預設開啟於port8080
    port = int(os.environ.get('PORT', 8080))
    # 使app開始在此連接端口上運行
    print('[預計運行於連接端口:{}]'.format(port))
    app.run(host='0.0.0.0', port=port)
