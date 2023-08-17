from linebot import LineBotApi
from linebot.models import TextSendMessage
import json
import datetime

file = open("config.json", "r")
data = json.load(file)

CHANNEL_ACCESS_TOKEN = data["CHANNEL_ACCESS_TOKEN"]
USER_ID = data["USER_ID"]
app = LineBotApi(CHANNEL_ACCESS_TOKEN)


today = datetime.date.today()
weekday_num = today.weekday()

text = ""
    
if weekday_num == 0:
    text = "燃えるゴミ"
elif weekday_num == 1:
    text = ""
elif weekday_num == 2:
    text = ""
elif weekday_num == 3:
    text = "缶、ビン、ペットボトル"
elif weekday_num == 4:
    text = "燃えるゴミ"
elif weekday_num == 5:
    text = "プラごみ"
elif weekday_num == 6:
    text = ""

def main():
    
    if weekday_num != "":
        messages = TextSendMessage(text=text + "の日…ってコト！？")
        app.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()
    