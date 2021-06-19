from django.shortcuts import render, redirect
from login.models import User
from wall.models import Message, Comment
from datetime import datetime

def wall(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "all_messages": Message.objects.all().order_by('updated_at').reverse(),
    }
    return render(request, "wall.html", context)

def enter_message(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(
            message=request.POST['message'],
            user=user
            )
    return redirect('/wall')

def enter_comment(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.create(
            comment=request.POST['comment'],
            user=user,
            message=message
        )
    return redirect('/wall')

# def delete_message(request):                                  # form POST version replaced below by AJAX version
#     if request.method == "POST":
#         message = Message.objects.get(id=request.POST['message_id'])
#         message.delete()
#     return redirect('/wall')

def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    now = datetime.datetime.now()
    print(now)
    print(message.updated_at)
    if (now - message.updated_at).minutes < 30:
        message.delete()
        return redirect('/wall')
    return render(request, 'partials/delete_message.html')      # this will be 'not allowed' message


def logoff(request):
    request.session.flush()
    return redirect('/')




# Create your views here.
