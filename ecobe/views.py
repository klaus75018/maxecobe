from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        if request.POST["useremail"] == "":
            messages.success(request,("Entrer à minima un email valide"))
        
            return redirect("index")
        else:
            username = request.POST["username"]
            email = request.POST["useremail"] 
            tel = request.POST["telephone"]
            full_message = f"""
                Received message below from {username}, 
                ________________________


                contacter: {username}

                {email}

                {tel}
            """

            send_mail(
                subject="Received contact form submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=False,
            )
            messages.success(request,("Votre demande a bien été envoyée !"))
        
            return redirect("index")
    else:
        return render(request, 'index.html', {})
    
    
    # Create your views here.
def contact_main(request):
    if request.method == 'POST':
        if request.POST["useremail"] == "":
            messages.success(request,("Entrer à minima un email valide"))
        
            return render(request, 'contact_main.html', {})
        else:
            username = request.POST["username"]
            message = request.POST["message"]
            email = request.POST["useremail"] 
            tel = request.POST["tel"]
            full_message = f"""
                Received message below from {username}, 
                ________________________


                {message}

                {email}

                {tel}
            """

            send_mail(
                subject="Received contact form submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=False,
            )
            messages.success(request,("Votre demande a bien été envoyée !"))
        
            return render(request, 'index.html', {})
    else:
        return render(request, 'contact_main.html', {})
