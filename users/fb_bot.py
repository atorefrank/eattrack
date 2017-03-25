import json
from logging import info

import requests
from django.conf import settings


def send_message(fbid, answer, quick_replies=None):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.FB_TOKEN
    if quick_replies:
        quick_replies = create_quick_replies(quick_replies)
        response = {"recipient": {"id": fbid}, "message": {"text": answer, 'quick_replies': quick_replies}}
    else:
        response = {"recipient": {"id": fbid}, "message": {"text": answer}}
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=json.dumps(response))
    info(status.json())


def user_details(fbid):
    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': settings.FB_TOKEN}
    user_details = requests.get(user_details_url, user_details_params).json()
    return user_details


def create_quick_replies(sel_topics):
    qr = [{'content_type': 'text', 'title': topic, 'payload': topic} for topic in sel_topics]
    return qr
