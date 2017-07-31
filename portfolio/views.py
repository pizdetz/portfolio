# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    return render(request, 'portfolio/basic.html',{
        'content':[
            'If you would like to contact me, please email me.',
            'colton.sweeney@gmail.com'
            ]
        }
    )