import os
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi import FastAPI, Request

s_app = App(token=os.getenv('SLACK_BOT_TOKEN'), signing_secret=os.getenv('SLACK_SIGNING_SECRET'))

app = FastAPI()
app_handler = SlackRequestHandler(s_app)


@app.post("/slack/events")
async def events(request: Request):
    return await app_handler.handle(request)

# SlackBoltインスタンスで、コマンド「/demo」の実行を検知
@s_app.command('/semihelper')
def demo(ack, respond, command):
    ack()
    # # もしボット以外の人からの投稿だった場合          
        # 指定のメッセージを組み立て
    reply_text = "https://frontend-eight-pi-54.vercel.appですよ"
        # 指定のメッセージを返却
    respond(reply_text)