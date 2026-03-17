# SlackBoltインスタンスで、コマンド「/demo」の実行を検知
@s_app.command('/semihelper')
def demo(ack, respond, command):
    ack()
    # # もしボット以外の人からの投稿だった場合          
        # 指定のメッセージを組み立て
    reply_text = "https://frontend-eight-pi-54.vercel.appですよ"
        # 指定のメッセージを返却
    respond(reply_text)