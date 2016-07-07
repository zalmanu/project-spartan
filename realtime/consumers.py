import json

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from channels import Group
from channels.sessions import channel_session

from chat.models import Room, Message


@channel_session
def ws_add(message):
    label = message['path'].strip('/').split('/')
    room = Room.objects.get(slug=label[1])
    Group("chat-" + label[1]).add(message.reply_channel)
    message.channel_session['room'] = room.slug


@channel_session
def ws_message(message):
    data = json.loads(message['text'])
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
