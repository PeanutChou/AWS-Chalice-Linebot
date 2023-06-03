from chalice import Chalice
from chalicelib.components import handler
from linebot.exceptions import InvalidSignatureError
import json
import traceback

from chalicelib.components.handler_text import handler
app_name='WRA6-Linebot'
app = Chalice(app_name=app_name)

@app.route('/')
def index():
    return {'this_lambda': app_name, "built_by":"AWS Chalice"}

@app.route('/callback', methods=['GET', 'POST'])
def callback():
    headers = app.current_request.headers
    body = app.current_request.raw_body
    if 'x-line-signature' in headers.keys():
        signature = headers['x-line-signature']
        # handle webhook body
        try:
            handler.handle(body.decode("utf-8"), signature)
        except InvalidSignatureError:
            msg = traceback.format_exc()
            return {
                'statusCode': 502,
                'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
                }
        return {
            'statusCode': 200,
            'body': json.dumps("Hello from Lambda!")
            }