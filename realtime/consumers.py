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
    session_string = message.content['headers'][9][1]
    for f_char in session_string.split(' '):
        if f_char[0] == 's':
            splited = f_char.split('=')
            if splited[1].endswith(";"):
                splited[1] = splited[1][:-1]
            session_key = splited[1]
    session = Session.objects.get(session_key=session_key)
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id')
    user = User.objects.get(id=uid)
    message.channel_session['user'] = user.username
    if user.account.has_related_object():
        print "spartans-" + user.spartan.category.name
        Group("spartans-" + user.spartan.category.name).add(
            message.reply_channel)
    if(label[0] == "room"):
        room = Room.objects.get(slug=label[1])
        Group("chat-" + label[1]).add(message.reply_channel)
        message.channel_session['room'] = room.slug


@channel_session
def ws_message(message):
    data = json.loads(message['text'])
    print data['mesaj']
    label = message.channel_session['room']
    room = get_object_or_404(Room, slug=data['room_slug'])
    user = get_object_or_404(User, username=data['user_name'])
    message = Message.objects.create(room=room, message=data['text'],
                                     submitter=user)

    html_txt = """
    <div class="avatar"><img src="http://www.gravatar.com/avatar/
""" + message.submitter.account.code + """" draggable="false"/></div>
    <div class="msg">
    <p>""" + message.message + """</p>
    <time>""" + message.timestamp.strftime('%B %d, %Y, %I:%M %p') + """</time>
    </div>
    </li>
    <hr>
    """
    dic = {
        'message': data['text'],
        'submitter': user.username,
        'code': user.account.code,
        'html': html_txt
    }
    Group("chat-" + label).send({'text': json.dumps(dic)})


@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group("chat-" + label).discard(message.reply_channel)
