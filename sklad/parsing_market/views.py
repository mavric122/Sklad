from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views import View
from tovar.models import *


def title_parsing(request):
    context = {

    }
    return render(request, 'parsing_market/index_parsing.html',
                  context)


def ozon_title(request):
    context = {

    }
    return render(request, 'parsing_market/ozon_title.html', context)


def test(request):
    context = {

    }
    return render(request, 'parsing_market/test.html', context)
