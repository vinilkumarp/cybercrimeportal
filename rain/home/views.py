from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from complaints.models import Complaint
# from accounts.models import UserProfile
from django.core.mail import send_mail
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
def view_home(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.user = request.user
            p.save()
        return redirect('/')
    else:
        posts = Complaint.objects.all()
        v1=0
        v2=0
        v3=0
        v4=0
        v5=0
        d1=0
        d2=0
        d3=0
        d4=0
        d5=0
        for e in posts:
            if e.category=='Bullying':
                v1=v1+1
            elif e.category=='Stalking':
                v2=v2+1
            elif e.category=='Grooming':
                v3=v3+1
            elif e.category=='Sexting':
                v4=v4+1
            else:
                v5=v5+1
        for s in posts:
            if s.social_media=='Facebook':
                d1=d1+1
            elif s.social_media=='Instagram':
                d2=d2+1
            elif s.social_media=='Whatsapp':
                d3=d3+1
            elif s.social_media=='Twitter':
                d4=d4+1
            else:
                d5=d5+1
        # print([v1,v2,v3,v4,v5,d1,d2,d3,d4,d5])
        p = [v1,v2,v3,v4,v5,d1,d2,d3,d4,d5]
        args = {'posts':p}
        return render(request,'base.html',args)
