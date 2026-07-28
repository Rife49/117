from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me (request):
    return render(request, 'pages/about_me.html')

def experience (request):
    return render(request, 'pages/experience.html')

def contact(request):
    if request.method =='POST':
        #form is not empty
        #To send email
        form = ContactForm(request.POST)
        #Collect the data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Build the message
            message_body = (
                f'You have a new email from your portfolio \n'
                f'Name: {name} \n'
                f'Email: {email} \n'
                f'Message: {message}'
            )
            
            # Try to send email
            try:
                send_mail(
                    'New email from Portfolio', #Subject
                    message_body, # What the users type
                    email, # Users Email
                    ['rifer4949@gmail.com']
                )
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f'Error sending email: {e}')
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form})
        else:
            print('Form not valid')
            form = ContactForm()
            return render(request, 'pages/contact.html', {'form': form})  
    else:   
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})  
    
    
