from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.db.models.functions import Random
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from .forms import FlexForm
from .models import Connect, Profile, CommonFlex


class CommonFlexView(ListView):
    login_url = reverse_lazy('login')
    model = CommonFlex
    template_name = 'commonflex.html'
    context_object_name = 'common_flex'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flex'] = CommonFlex.objects.all().order_by(Random())
        return context


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'

    #def get_queryset(self):
         #Filter profiles based on the current user
        #return Profile.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['common_flex'] = CommonFlex.objects.filter(user=user)
        context['profile'] = Profile.objects.get(user=user)
        return context


class CreateFlex(CreateView):
    template_name = 'post.html'
    form_class = FlexForm
    success_url = reverse_lazy('post-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class CheckItOutView(DetailView):
    #login_url = reverse_lazy('login')
    template_name = 'check_it_out.html'
    model = Connect
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super(CheckItOutView, self).get_context_data(**kwargs)
        context['job'] = Connect.objects.all()
        return context


class ConnectView(ListView):
    login_url = reverse_lazy('login')
    template_name = 'connect.html'
    model = Connect
    context_object_name = 'available_jobs'

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        context['available_jobs'] = Connect.objects.all().order_by('client')
        return context

    # Queryset for class
    #def get_queryset(self):
     #   return AbstractModel.objects(
          #username=self.request.user
      #  )
