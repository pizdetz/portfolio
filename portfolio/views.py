# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm

def index(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('portfolio/contact_template.txt')
            context = ({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['colton.sweeney@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            send_mail('Subject here', content, contact_email, ['colton.sweeney@gmail.com'], fail_silently=False)
            messages.add_message(request, messages.SUCCESS, 'Your email has been sent successfully.')
            return redirect('contact')

    return render(request, 'portfolio/basic.html', {
        'form': form_class,
        
    })

def services(request):
    return render(request, 'portfolio/services.html')