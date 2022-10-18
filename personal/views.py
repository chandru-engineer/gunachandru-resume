from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Projects

# Create your views here.

def index(request):

    objects = Projects.objects.all() ## get all objects of projects
    context = {'objects': objects}


    if request.method == "POST":

        name = request.POST['name']
        reply_to = request.POST['_replyto']
        message = request.POST['message']

        template = render_to_string('personal/mail_template.html', {'name': name})
        template_admin = render_to_string('personal/mail_template_for_admin.html', {'name': name, 'email':reply_to, 'message':message})
        email = EmailMessage(
            'Thanking For Contect Mail',
            template,
            settings.EMAIL_HOST_USER,
            [reply_to]
        )
        email.fail_silently = False
        email.send()

        email_admin = EmailMessage(
            'Contect Mail',
            template_admin,
            settings.EMAIL_HOST_USER,
            ['tochandru.engineer@gmail.com']
        )
        email_admin.fail_silently = False
        email_admin.send()

        return render(request, 'personal/index.html', context = context)

    return render(request, 'personal/index.html', context = context)

