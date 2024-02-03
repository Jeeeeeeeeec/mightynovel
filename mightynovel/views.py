from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Novel


class HomeView(ListView):
    model = Novel
    template_name = 'pages/home.html'
    context_object_name = 'novels'


class AboutView(ListView):
    model = Novel
    template_name = 'pages/about.html'
    context_object_name = 'novels'


class ProductView(ListView):
    model = Novel
    template_name = 'pages/products.html'
    context_object_name = 'novels'


class LoginView(LoginView):
    template_name = 'pages/login.html'


class SignupView(CreateView):
    template_name = 'pages/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class ContactView(ListView):
    model = Novel
    template_name = 'pages/contact.html'
    context_object_name = 'novels'


class NovelListView(ListView):
    model = Novel
    template_name = 'pages/novel_list.html'
    context_object_name = 'novels'


class NovelDetailView(DetailView):
    model = Novel
    template_name = 'pages/novel_detail.html'
    context_object_name = 'novel'


class NovelCreateView(CreateView):
    model = Novel
    template_name = 'pages/add_novel.html'
    fields = ['title', 'author', 'description', 'genre', 'price']
    success_url = reverse_lazy('novel_list')


class NovelUpdateView(UpdateView):
    model = Novel
    template_name = 'pages/novel_form.html'
    fields = ['title', 'author', 'description', 'genre', 'price']

    def get_success_url(self):
        return reverse_lazy('novel_detail', kwargs={'pk': self.object.pk})


class NovelEditView(NovelUpdateView):
    template_name = 'pages/novel_edit.html'


class NovelDeleteView(DeleteView):
    model = Novel
    template_name = 'pages/novel_confirm_delete.html'
    success_url = reverse_lazy('novel_list')
