from channels import Group
from channels.sessions import channel_session

@channel_session
def ws_connect(message):
    prefix = message['path'].strip('/').split('/')
    print message.reply_channel
    Group("notifications", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = "notifications"

@channel_session
def ws_receive(message):
    Group("notifications",
           channel_layer=message.channel_layer).send({'text': "ana are mere"})

@channel_session
def ws_disconnect(message):
    Group("notifications", channel_layer=message.channel_layer).discard(message.reply_channel)
