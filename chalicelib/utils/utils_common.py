import datetime
from chalicelib.components import line_bot_api
# from chalicelib.utils import utils_database
import json

from linebot.models import (
    TextSendMessage,
)

def get_event_info(event):
    event_dict      = event.message.as_json_dict()
    timestamp       = float(event.timestamp/1000)
    dt_object       = datetime.datetime.fromtimestamp(timestamp)
    datetime_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")                     # 0.日期時間
    source_type     = event.source.type
    group_id        = event.source.group_id if source_type == "group" else ""    # 4.群組ID
    summary         = line_bot_api.get_group_summary(group_id) if group_id != '' else ""
    group_name      = summary.group_name if group_id != '' else ""       # 5.群組名稱
    user_id         = event.source.user_id                                        # 6.傳訊者ID
    profile         = line_bot_api.get_group_member_profile(group_id, event.source.user_id) if group_id != '' else ""
    user_name       = profile.display_name        if group_id != '' else ""            # 7.傳訊者顯示名稱
    user_img        = profile.picture_url if group_id != '' else "" 
    msg_type        = event.message.type
    msg_id          = event.message.id
    image_set_id    = event_dict["imageSet"]["id"] if "imageSet" in event_dict.keys() else 'null'
    
    return {
        "source_type": source_type,
        "datetime": datetime_string,
        "group_id": group_id,
        "group_name": group_name,
        "user_id": user_id,
        "user_name": user_name,
        "user_img": user_img,
        "msg_type": msg_type,
        "msg_id": msg_id,
        "image_set_id": image_set_id
    }


def get_user_info(event):
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id)
    return {
        "user_id": user_id,
        "display_name": profile.display_name,
        "picture_url": profile.picture_url
    }

def linebot_send_text(reply_token, msg):
    message = TextSendMessage(text=msg)
    try:
        line_bot_api.reply_message(reply_token, message)
    except Exception as e:
        print("error: ", str(e))
    return

def linebot_send_flex(reply_token, flex_send_msg):
    try:
        line_bot_api.reply_message(reply_token, flex_send_msg)
    except Exception as e:
        print("error: ", str(e))
    return