from django.contrib.auth import logout
from .froms import SignUpForm, UserEditForm
from django.shortcuts import render, redirect
from twitter.models import twitt
from .models import CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView
from django.forms import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse

def get_user(request, username):
    # get user_id from Username
    user_id = CustomUser.objects.get(username=username).pk
    # get current user from request
    current_user = request.user.pk
    # check if user want to go current_user_profile with get user redirect it to get_current_profile()
    if user_id == current_user:
        return HttpResponseRedirect(reverse('profile'))
    else:
        context = {
            'profile': CustomUser.objects.get(username=username),
            'twittes': twitt.objects.filter(auther=user_id)
        }
        return render(request, 'Account/user_profile.html', context)


@login_required
def get_current_profile(request):
    # get current user login from request
    current_user = request.user
    # check user is authenticated if not redirect it to login
    if current_user.is_authenticated == False:
        return HttpResponseRedirect(reverse('login'))
    
    else:
        user_id = CustomUser.objects.get(username=current_user).pk
        context = {
        'user': CustomUser.objects.get(username=current_user),
        'twittes': twitt.objects.filter(auther=user_id)
        }
        return render(request, 'Account/profile.html', context)
    


#home page
def home_page(request):
    context = {
        'twittes': twitt.objects.all()
    }
    return render(request, 'home.html', context)

# Cerate user
class UserCreateView(CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'Account/register.html'


class UserLoginView(LoginView):
    success_url = '/'
    template_name = 'Account/login.html'
    model = CustomUser



def followToggle(request, user):
    user = CustomUser.objects.get(username=user)
    currentUser = CustomUser.objects.get(username=request.user.username)
    following = user.following.all()
    if user != currentUser.username:
        if currentUser in following:
            user.following.remove(currentUser.id)
        else:
            user.following.add(currentUser.id)

    return HttpResponseRedirect('/')


class LogOutView(LoginRequiredMixin, View):
    template_name = 'Accout/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)

        if request.user:
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')


@login_required
def edit_profile(request):
    currentUser = request.user
    form = UserEditForm(request.POST, request.FILES or None,instance=currentUser)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {
        'form': form
    }
    return render(request, 'Account/edit_profile.html', context)


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "Account/edit_profile.html"
    fields = ['profile_image', 'biography',
              'last_name', 'first_name', 'username',]

    def get_object(self, queryset=None):
        return self.request.user


# def delete_profile_image(request):
#     try:
#         request.user.profile_image.delete()
#     except:
#         pass
#     return HttpResponseRedirect('/')

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        # results = Article.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) )
        profile_result = CustomUser.objects.filter(Q(username__icontains=query) | Q(
            last_name__icontains=query) | Q(first_name__icontains=query))
        twitte_result = twitt.objects.filter(Q(text__icontains=query))
        
    return render(request, 'Account/find_user.html', {'query': query, 'profile_result': profile_result,'twitte_result':twitte_result})


class CustomUserDeleteView(LoginRequiredMixin,DeleteView):
    model = CustomUser
    success_url = '/'
    template_name = "Account/delete_account.html"
    
    def get_object(self, queryset=None):
        return self.request.user