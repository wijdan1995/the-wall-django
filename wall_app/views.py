from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Message, Comment
from login_app.models import User
import datetime
def index(request):
    if 'user_email' in request.session:
        context = {
            'all_messages': Message.objects.all(),
            'message_time': datetime.datetime.now() - datetime.timedelta(seconds=60 * 30),
            'user_first_name': request.session['user_first_name'],
            'user_email':request.session['user_email']
        }
        return render(request, 'wall_app/index.html', context)
    else:
        return redirect('login:root')

def message_create(request, user_email):
    if request.method == 'POST':
        errors = Message.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='message')
            return redirect('wall:root')
        Message.objects.create(content=request.POST['content'], written_by=User.objects.get(email=user_email))
        print(request.POST)
        print(user_email)
    return redirect('wall:root')

def message_delete(request, user_email, message_id):
    if request.method == 'POST':
        errors = Message.objects.delete_validator(user_email, message_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='message')
            return redirect('wall:root')
        Message.objects.get(id=message_id).delete() 
    return redirect('wall:root')

def comment_create(request, user_email, message_id):
    if request.method == 'POST':
        errors = Comment.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='comment')
            return redirect('wall:root')
        Comment.objects.create(comment=request.POST['comment'], written_by=User.objects.get(email=user_email), written_on=Message.objects.get(id=message_id))
    return redirect('wall:root')
