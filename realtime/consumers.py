import json

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

from channels import Group
from channels.sessions import channel_session

from chat.models import Room, Message


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
    if user.account.has_related_object() and user.spartan.spartanStatus:
        Group("spartans-" + user.spartan.category.name + "-" +
              user.account.city).add(message.reply_channel)
    if(label[0] == "room"):
        room = Room.objects.get(slug=label[1])
        Group("chat-" + label[1]).add(message.reply_channel)
        message.channel_session['room'] = room.slug


@channel_session
def ws_message(message):
    data = json.loads(message['text'])
    label = message.channel_session['room']
    room = get_object_or_404(Room, slug=data['room_slug'])
    user = get_object_or_404(User, username=message.channel_session['user'])
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
    dic = {
        'message': data['text'],
        'submitter': user.username,
        'code': user.account.code,
        'html': html_txt,
        'username': user.username
    }
    Group("chat-" + label).send({'text': json.dumps(dic)})


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
