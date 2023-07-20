# Edit web/views.py
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from. models import Book,BookAuthor
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"


class Form(TemplateView):
    template_name = "pages/basic_elements.html"


class Icon(TemplateView):
    template_name = "pages/icon.html"


class Button(TemplateView):
    template_name = "pages/buttons.html"


class Typography(TemplateView):
    template_name = "pages/typography.html"


class Chart(TemplateView):
    template_name = "pages/chartjs.html"


class Table(TemplateView):
    template_name = "pages/tables.html"


class Error(TemplateView):
    template_name = "pages/error-404.html"


# books
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields="__all__"
    # success_url = reverse_lazy('web:book_list',)


class BookList(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Books"
        return context


class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = "__all__"


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = "/book_list/"


# authors
class AuthorCreate(LoginRequiredMixin,CreateView):
    model=BookAuthor
    template_name="books/author_create.html"
    fields="__all__"
    
    
class AuthorList(LoginRequiredMixin, ListView):
    model = BookAuthor
    template_name = "books/author_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Authors"
        return context


class AuthorDetail(LoginRequiredMixin, DetailView):
    model = BookAuthor
    template_name = "books/author_detail.html"


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = BookAuthor
    template_name = "books/author_update.html"
    fields = "__all__"


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = BookAuthor
    template_name = "books/author_delete.html"
    success_url = "/author_list/"


# users
class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Users"
        return context
    
    
class UserCreate(LoginRequiredMixin,CreateView):
    model=User
    template_name="users/user_create.html"
    fields=("username","email","password")
    success_url=reverse_lazy("web:user_list")
    
    
class UserUpdate(LoginRequiredMixin, UpdateView):
    model=User
    template_name="users/user_update.html"
    fields=("username","email","first_name","last_name","is_superuser")
    success_url=reverse_lazy("web:user_list")
    
    
class UserDelete(LoginRequiredMixin, DeleteView):
    model=User
    template_name="users/user_delete.html"
    success_url = reverse_lazy("web:user_list")
    
    
class BookTable(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_table.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Books"
        return context