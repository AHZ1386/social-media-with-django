from django.views.generic import CreateView, UpdateView
from .models import twitt
from . forms import TwitteFrom
from Account.models import CustomUser
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class TwitteCreateView(CreateView):
    model = twitt
    template_name = "Twitter/post_twitte.html"
    success_url = '/'
    fields = ['text',]
    def form_valid(self, form):
        form.instance.auther = self.request.user #twitte.auther == loginde user
        return super().form_valid(form)

class TwitteUpdateView(LoginRequiredMixin, UpdateView):
    model = twitt
    template_name = "Twitter/edit_twitte.html"
    success_url = '/'
    fields = ['text',]
    def get_queryset(self):
        queryset = super(TwitteUpdateView, self).get_queryset()
        queryset = queryset.filter(auther=self.request.user) # check if request.user is auther of twiite
        return queryset
    

    