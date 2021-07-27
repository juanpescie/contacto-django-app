from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_from = settings.EMAIL_HOST_USER
        email_to = ["juanppescie@gmail.com"]
        send_mail(asunto, mensaje, email_from, email_to, fail_silently=True)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")

