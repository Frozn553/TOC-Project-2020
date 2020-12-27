import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "news_initial", "TVBS_choose_category","Apple_choose_category","CNA_choose_category", "Ltn_choose_category","TVBS_choose_social","TVBS_choose_sport","TVBS_choose_world","TVBS_choose_politics","CNA_choose_social","CNA_choose_sport","CNA_choose_world","CNA_choose_politics","Apple_choose_social","Apple_choose_sport","Apple_choose_world","Apple_choose_politics","Ltn_choose_social","Ltn_choose_sport","Ltn_choose_world","Ltn_choose_politics"],
    transitions=[
        {
            "trigger": "advance_initial",
            "source": "user",
            "dest": "news_initial",
            "conditions": "is_going_to_news_initial",
        },
        {
            "trigger": "choose_which_media",
            "source": "news_initial",
            "dest": "TVBS_choose_category",
            "conditions": "is_going_to_TVBS_choose_category",
        },
        {
            "trigger": "choose_which_media",
            "source": "news_initial",
            "dest": "Apple_choose_category",
            "conditions": "is_going_to_Apple_choose_category",
        },
        {
            "trigger": "choose_which_media",
            "source": "news_initial",
            "dest": "Ltn_choose_category",
            "conditions": "is_going_to_Ltn_choose_category",
        },
        {
            "trigger": "choose_which_media",
            "source": "news_initial",
            "dest": "CNA_choose_category",
            "conditions": "is_going_to_CNA_choose_category",
        },


        {
            "trigger": "choose_which_type",
            "source": "TVBS_choose_category",
            "dest": "TVBS_choose_social",
            "conditions": "is_going_to_TVBS_choose_social",
        },
        {
            "trigger": "choose_which_type",
            "source": "TVBS_choose_category",
            "dest": "TVBS_choose_sport",
            "conditions": "is_going_to_TVBS_choose_sport",
        },
        {
            "trigger": "choose_which_type",
            "source": "TVBS_choose_category",
            "dest": "TVBS_choose_world",
            "conditions": "is_going_to_TVBS_choose_world",
        },
        {
            "trigger": "choose_which_type",
            "source": "TVBS_choose_category",
            "dest": "TVBS_choose_politics",
            "conditions": "is_going_to_TVBS_choose_politics",
        },
        {"trigger": "choose_which_type",
         "source": "TVBS_choose_category",
         "dest": "news_initial",
         "conditions": "is_going_to_initial_TVBS",
        },
        {"trigger": "choose_which_type",
         "source": ["TVBS_choose_social","TVBS_choose_sport","TVBS_choose_world","TVBS_choose_politics"],
         "dest": "TVBS_choose_category",
         "conditions": "is_going_back_to_TVBS_choose_category",
        },


        {
            "trigger": "choose_which_type",
            "source": "CNA_choose_category",
            "dest": "CNA_choose_social",
            "conditions": "is_going_to_CNA_choose_social",
        },
        {
            "trigger": "choose_which_type",
            "source": "CNA_choose_category",
            "dest": "CNA_choose_sport",
            "conditions": "is_going_to_CNA_choose_sport",
        },
        {
            "trigger": "choose_which_type",
            "source": "CNA_choose_category",
            "dest": "CNA_choose_world",
            "conditions": "is_going_to_CNA_choose_world",
        },
        {
            "trigger": "choose_which_type",
            "source": "CNA_choose_category",
            "dest": "CNA_choose_politics",
            "conditions": "is_going_to_CNA_choose_politics",
        },
        {"trigger": "choose_which_type",
         "source": "CNA_choose_category",
         "dest": "news_initial",
         "conditions": "is_going_to_initial_CNA",
        },
        {"trigger": "choose_which_type",
         "source": ["CNA_choose_social","CNA_choose_sport","CNA_choose_world","CNA_choose_politics"],
         "dest": "CNA_choose_category",
         "conditions": "is_going_back_to_CNA_choose_category",
        },


        {
            "trigger": "choose_which_type",
            "source": "Apple_choose_category",
            "dest": "Apple_choose_social",
            "conditions": "is_going_to_Apple_choose_social",
        },
        {
            "trigger": "choose_which_type",
            "source": "Apple_choose_category",
            "dest": "Apple_choose_sport",
            "conditions": "is_going_to_Apple_choose_sport",
        },
        {
            "trigger": "choose_which_type",
            "source": "Apple_choose_category",
            "dest": "Apple_choose_world",
            "conditions": "is_going_to_Apple_choose_world",
        },
        {
            "trigger": "choose_which_type",
            "source": "Apple_choose_category",
            "dest": "Apple_choose_politics",
            "conditions": "is_going_to_Apple_choose_politics",
        },
        {"trigger": "choose_which_type",
         "source": "Apple_choose_category",
         "dest": "news_initial",
         "conditions": "is_going_to_initial_Apple",
        },
        {"trigger": "choose_which_type",
         "source": ["Apple_choose_social","Apple_choose_sport","Apple_choose_world","Apple_choose_politics"],
         "dest": "Apple_choose_category",
         "conditions": "is_going_back_to_Apple_choose_category",
        },

        {
            "trigger": "choose_which_type",
            "source": "Ltn_choose_category",
            "dest": "Ltn_choose_social",
            "conditions": "is_going_to_Ltn_choose_social",
        },
        {
            "trigger": "choose_which_type",
            "source": "Ltn_choose_category",
            "dest": "Ltn_choose_sport",
            "conditions": "is_going_to_Ltn_choose_sport",
        },
        {
            "trigger": "choose_which_type",
            "source": "Ltn_choose_category",
            "dest": "Ltn_choose_world",
            "conditions": "is_going_to_Ltn_choose_world",
        },
        {
            "trigger": "choose_which_type",
            "source": "Ltn_choose_category",
            "dest": "Ltn_choose_politics",
            "conditions": "is_going_to_Ltn_choose_politics",
        },
        {"trigger": "choose_which_type",
         "source": "Ltn_choose_category",
         "dest": "news_initial",
         "conditions": "is_going_to_initial_Ltn",
        },
        {"trigger": "choose_which_type",
         "source": ["Ltn_choose_social","Ltn_choose_sport","Ltn_choose_world","Ltn_choose_politics"],
         "dest": "Ltn_choose_category",
         "conditions": "is_going_back_to_Ltn_choose_category",
        }




    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        if machine.state == "user":
            judge_advance_initial = machine.advance_initial(event)
            if judge_advance_initial == False:
                send_text_message(event.reply_token, "哈囉 想看新聞的話 請輸入看新聞")
        elif machine.state == "news_initial":
            judge_choose_media = machine.choose_which_media(event)
            if judge_choose_media == False:
                send_text_message(event.reply_token, "格式錯誤 請重新輸入!!")
        else:
            judge_choose_which_type = machine.choose_which_type(event)
            if judge_choose_which_type == False:
                send_text_message(event.reply_token, "格式錯誤 請重新輸入!!")


    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)

    app.run(host="0.0.0.0", port=port, debug=True)
