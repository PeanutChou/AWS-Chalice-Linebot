from chalicelib.components.configuration import get_config_setting
from linebot import WebhookHandler
from linebot import LineBotApi
import os
import datetime

setting = get_config_setting()
print(setting.config_linebot)

line_bot_api = LineBotApi(setting.config_linebot["access_token"])
handler = WebhookHandler(setting.config_linebot["channel_secret"])

def get_now_dt_string():
    dt_object       = datetime.datetime.now()
    datetime_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return datetime_string
