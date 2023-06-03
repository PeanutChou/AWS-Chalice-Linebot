from chalicelib.components import handler, line_bot_api
from chalicelib.components import do_transaction_pg
from chalicelib.components import setting
from chalicelib.utils.utils_common import get_event_info, get_user_info, linebot_send_text, linebot_send_flex
import json

print(handler)

from linebot.models import (
    MessageEvent, 
    TextMessage, 
    ImageSendMessage
)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    this_message = event.message.text
    print(this_message)
    linebot_send_text(event.reply_token, this_message)