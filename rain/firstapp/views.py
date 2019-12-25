from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from firstapp.models import Client,Created_Rooms,Joined_Rooms
from firstapp.forms import clientForm,Created_RoomsForm,Joined_RoomsForm
from firstapp.forms import UserForm
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from firstapp.forms import UserProfileInfoForm

# Create your views here.
#
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

#@login_required
def index(request):
    # client_Form = clientForm(request.POST or None)
    # if client_Form.is_valid():
    #     instance = client_Form.save()
    # my_dict = {'insert_me':"Hello i am view.py", 'form':client_Form}
    # print current_user.id
    # if request.user.is_authenticated():
    #     current_user = request.user.password
    # else:
    #     current_user =''
    return render(request,'firstapp/index.html')

def signup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile.pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'firstapp/signup.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed!")
            # print("Username {} and password {}".formate(username,password))
            # return HttpResponse("invalid login detaion supplied!")
            # strng="Incalid user name or Password"
            # invalid_dic = {'inval':strng}
            return render(request,'firstapp/login.html', {})


    else:
        return render(request,'firstapp/login.html', {})

#logout

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))



# @login_required
def special(request):
    # client_Form = clientForm(request.POST or None)
    # if client_Form.is_valid():
    #     instance = client_Form.save()
    # my_dict = {'insert_me':"Hello i am view.py", 'form':client_Form}
    return render(request,'firstapp/special.html')

def chat(request):
    return render(request,'firstapp/caht.html')

def chat1(request):
    return render(request,'firstapp/caht1.html')
@login_required
def counsel(request):
    return render(request,'firstapp/counsel.html')


# @login_required
# def C_Rooms(request):

#     c_rooms= Created_Rooms.objects.all()
   # rname=c_rooms
#     form= Created_RoomsForm(request.POST or None)
#     if form.is_valid():
#         fs= form.save(commit=False)
#         fs.user= request.user
#         fs.save()

#     context= {'form': form,
#               'c_rooms': c_rooms,
#               }

#     return render(request, 'firstapp/createdRooms.html', context)


    # @login_required
    # def J_Rooms(request):

    #     j_rooms= Joined_Rooms.objects.all()
    #     # rname=c_rooms
    #     form= Joined_RoomsForm(request.POST or None)
    #     if form.is_valid():
    #         fs= form.save(commit=False)
    #         fs.user= request.user
    #         fs.save()

    #     context= {'form': form,
    #               'j_rooms': j_rooms,
    #               }

    #     return render(request, 'firstapp/joinedrooms.html', context)
