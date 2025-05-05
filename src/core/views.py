from django.shortcuts import render
from django.conf import settings
from emails.forms import EmailForm
from emails.models import Email,EmailVerificationEvent
from emails.services import verify_email, start_verification_event

EMAIL_ADDRESS = settings.EMAIL_ADDRESS

def login_logout_template_view(request, *args, **kwargs):
    return render(request, 'auth/login.html', {})

def home_view(request, *args, **kwargs):
    template_name = 'home.html'
    
    print(request.POST)
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        'message': ''
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = start_verification_event(email_val)
        print(obj)
        
        context['form'] = EmailForm()
        context['message'] = f'success, check your emial for verification from {EMAIL_ADDRESS}'
    else:
        print(form.errors)
  
    print("email_id:",request.session.get('email_id'))
    return render(request, template_name, context)