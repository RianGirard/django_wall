from django.shortcuts import render, redirect, HttpResponse
from login.models import User
from wall.models import Message, Comment
from datetime import datetime
from django.utils.timezone import utc

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
    return HttpResponse("")          # sending HttpResponse just to send something; AJAX performs reload of screen;

def delete_message(request):
    if request.method == "POST":
        message = Message.objects.get(id=request.POST['message_id'])
        now = datetime.utcnow().replace(tzinfo=utc)                 # need UTC time to compare with 'updated_at' in db
        then = message.updated_at
        diff = (now - then)
        secs = diff.total_seconds()
        path = 1
        if secs < 1800:                             # if the Message is < 30 minutes old, then delete Message; else render HTML partial back
            message.delete()
            path = 2                                # path variable is passed in dict to partial snippet
        return render(request, 'partials/delete_response.html', {"path":path})
    return redirect('/wall')

def delete_comment(request):
    if request.method == "POST":
        comment = Comment.objects.get(id=request.POST['comment_id'])
        now = datetime.utcnow().replace(tzinfo=utc)                 # need UTC time to compare with 'updated_at' in db
        then = comment.updated_at
        diff = (now - then)
        secs = diff.total_seconds()
        path = 1
        if secs < 1800:                             # if the Comment is < 30 minutes old, then delete Comment; else render HTML partial back
            comment.delete()
            path = 2                                # path variable is passed in dict to partial snippet
        return render(request, 'partials/delete_response.html', {"path":path})
    return redirect('/wall')

def logoff(request):
    request.session.flush()
    return redirect('/')




# Create your views here.
