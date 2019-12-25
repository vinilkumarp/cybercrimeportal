from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import RegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . models import UserProfile
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    else:
        form = RegistrationForm()
    return render(request,'accounts/reg_form.html',{'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        return redirect('/')
    else:    
        args = {'user': request.user}
        return render(request,'accounts/validate.html', args)

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,instance=request.user)
        form_user = ProfileUpdateForm(request.POST,\
                                    request.FILES,\
                                    instance = request.user.userprofile)
        if form.is_valid() and form_user.is_valid:
            form.save()
            form_user.save()
            return redirect('/account/')
    else:
        form = UserUpdateForm(instance=request.user)
        form_user = ProfileUpdateForm(instance = request.user.userprofile)
    args = {'form': form,'form_user': form_user}
    return render(request,'accounts/edit_profile.html',args)

@login_required   
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile/')
        else:
            return redirect('/account/change-password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'accounts/change_password.html',args)  

def view_profile(request,id):
    post= get_object_or_404(UserProfile, user_id=id)
    return render(request,'accounts/view_profile.html',{'post':post})
    
def subscribe(request,id):
    post = get_object_or_404(UserProfile,user_id = id)
    post.subscribe = True
    post.save()
    return redirect('/forum/')

def admin_login(request):
    posts = UserProfile.objects.all().filter(user_id = request.user.id)
    for e in posts:
        if e.is_admin == True:
           return redirect('/complaints/view/')
        else:
            return redirect('/')

def validation(request):
    if request.method=='POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        params = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        status = verify_rs.get("success", False)
        if not status:
            raise forms.ValidationError(
                _('Captcha Validation Failed.'),
                code='invalid',
            )
            return redirect('login')
        if status:
            return redirect('/account')
    else:
        return render(request,'accounts/validate.html')