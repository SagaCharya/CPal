from django.shortcuts import redirect, render
from django.http import HttpResponse
from core.settings import EMAIL_ADDRESS
from emails.forms import EmailForm
from .services import verify_token, start_verification_event
from django.contrib import messages
from django_htmx.http import HttpResponseClientRedirect
# Create your views here.


def logout_btn_hx_view(request):
    if not request.htmx:
        return redirect('/')
    if request.method == 'POST':
        try:
            del request.session['email_id']
        except:
            pass
        email_id_in_session = request.session.get('email_id')
        if email_id_in_session is not None:
            return HttpResponseClientRedirect('/')
    return render(request, 'emails/hx/logout_bth.html', {})


def email_token_login_view(request):
    if not request.htmx:
        return redirect('/')
    email_id_in_session = request.session.get('email_id')
    template_name = 'emails/hx/form.html'
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        'message': '',
        'show_form': not email_id_in_session,
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = start_verification_event(email_val)
        context['form'] = EmailForm()
        context['message'] = f'success, check your emial for verification from {EMAIL_ADDRESS}'
        
    else:
        print(form.errors)
  
   
    return render(request, template_name, context)


def verify_email_token_view(request, token, *args, **kwargs,):
    did_verify, msg, email_obj = verify_token(token)
    
    if not did_verify:
        try:
            del request.session['email_id']
        except:
            pass
        messages.error(request, msg)
        return redirect('/login/')
    messages.success(request, msg)
    request.session['email_id'] = f"{email_obj.id}"
    next_url = request.session.get('next_url') or '/'
    if not next_url.startswith('/'):
        next_url = '/'     
    return redirect(next_url)
