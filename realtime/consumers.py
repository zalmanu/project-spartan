import json
import string
import random

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

from channels import Group
from channels.sessions import channel_session

from chat.models import Room, Message
from notifications.models import Notification


@channel_session
def ws_add(message):
    label = message['path'].strip('/').split('/')
    headers = message.content.get('headers')
    found = False
    for tup in headers:
        if found:
            break
        for item in tup:
            if item.startswith('csrftoken'):
                session_id = item.split(' ')[1]
                session_id = session_id.split('=')[1]
                found = True
                break
            elif item.startswith('sessionid'):
                session_id = item.split(';')[0]
                session_id = session_id.split('=')[1]
                found = True
                break
    session = Session.objects.get(session_key=session_id)
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    message.channel_session['user'] = user.username
    Group("channel-" + user.username).add(message.reply_channel)
    if user.account.has_related_object() and user.spartan.spartanStatus:
        Group("spartans-" + user.spartan.category.name + "-" +
              user.account.city).add(message.reply_channel)
    if(label[0] == "room"):
        room = Room.objects.get(slug=label[1])
        Group("chat-" + label[1]).add(message.reply_channel)
        message.channel_session['room'] = room.slug
    Group("messages-" + user.username).add(message.reply_channel)


@channel_session
def ws_message(message):
    data = json.loads(message['text'])
    label = message.channel_session['room']
    room = get_object_or_404(Room, slug=data['room_slug'])
    user = get_object_or_404(User, username=data['user_name'])
    message = Message.objects.create(room=room, message=data['text'],
                                     submitter=user)
    html_txt = """
    <div class="message-block">
    <div><span class="username">""" + message.submitter.username + """</span>
    <span class="message-datetime">""" + message.timestamp.strftime('%B %d, %Y, %I:%M %p') + """</span>
    </div>
    <div class="message">""" + message.message + """</div>
                                                </div>
                                            </li>
                                        </a>
    """
    url = "/room/" + label
    id_hash = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(6))
    bar_html = """
    <a href=\"""" + url + """\" data-notification=\"""" + id_hash + """\"
    onmouseover="seen_not(this.getAttribute('data-notification'));"
    id=\"""" + id_hash + """\">
    <li class="message">
     You received a message
    </li>
    """
    chat_dic = {
        'message': data['text'],
        'submitter': user.username,
        'html': html_txt,
        'type': 'chat_mess'
    }
    bar_dic = {
        'type': 'chat',
        'submitter': user.username,
        'html': bar_html
    }
    Group("chat-" + label).send({'text': json.dumps(chat_dic)})
    if(room.employer == user):
        Group("messages-" + room.spartan.username).send({'text':
                                                         json.dumps(bar_dic)})
        receiver = room.spartan
    else:
        Group("messages-" + room.employer.username).send({'text':
                                                          json.dumps(bar_dic)})
        receiver = room.employer
    notification = Notification.objects.create(receiver=receiver,
                                               not_type="chat", url=url,
                                               id_hash=id_hash)
    notification.save()


@channel_session
def ws_disconnect(message):
    username = message.channel_session['user']
    user = User.objects.get(username=username)
    if message.channel_session['room']:
        label = message.channel_session['room']
        Group("chat-" + label).discard(message.reply_channel)
    if user.account.has_related_object() and user.spartan.spartanStatus:
        Group("spartans-" + user.spartan.category.name + "-" +
              user.account.city).discard(message.reply_channel)
