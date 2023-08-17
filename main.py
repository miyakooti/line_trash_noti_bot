from linebot import LineBotApi
from linebot.models import TextSendMessage
import json

file = open("config.json", "r")
data = json.load(file)

CHANNEL_ACCESS_TOKEN = data["CHANNEL_ACCESS_TOKEN"]
USER_ID = data["USER_ID"]

app = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    messages = TextSendMessage(text="ぽこ")
    app.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()
    