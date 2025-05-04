from .models import Email, EmailVerificationEvent
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def verify_email(email):
    qs = Email.objects.filter(email=email, active=False)
    return qs.exists()

def get_verification_email_msg(verification_instance, as_html=False):
    if not isinstance(verification_instance, EmailVerificationEvent):
        return None
    verify_link = verification_instance.get_link()
    if as_html:
        return f"<h1><a href={verify_link}>{verify_link}</a></h1>"
    return f"Verification link: {verify_link}"

def start_verification_event(email):
    email_obj, create = Email.objects.get_or_create(email=email)
    obj = EmailVerificationEvent.objects.create(parent=email_obj, email=email)
    sent = send_verification_email(obj.id)
    return obj, sent
    
    
def send_verification_email(verify_obj_id):   
    verify_obj = EmailVerificationEvent.objects.get(id=verify_obj_id)
    email = verify_obj.email
    subject = 'Verify your email'
    text_msg = get_verification_email_msg(verify_obj, as_html=False)
    text_html = get_verification_email_msg(verify_obj, as_html=True)
    from_user_email_add = EMAIL_HOST_USER
    to_user_email = email
    return send_mail(subject,
              text_msg,
              from_user_email_add,
              [to_user_email],
              fail_silently=False,
              html_message=text_html
              )
    
def verify_token(token, mak_attempts = 5):
    qs = EmailVerificationEvent.objects.filter(token=token)
    if not qs.exists() and not qs.count() == 1:
        return False, 'Invalid token', None
    has_email_expired = qs.filter(expired=True)
    if has_email_expired.exists():
        return False, 'Token expired', None
    max_attempts_reached = qs.filter(attempts__gte=mak_attempts)
    if max_attempts_reached.exists():
        # max_attempts_reached.update()
        return False, 'Token expired, used too many times', None
    '''token valid'''
    '''update attempts, expire token  to true'''
    obj = qs.first()
    obj.attempts += 1
    obj.last_attemp_at = timezone.now()
    if obj.attempts >= mak_attempts:
        obj.expired = True
        obj.expired_at = timezone.now()
    obj.save()
    email_obj = obj.parent
    return True, 'Welcome', email_obj
    

