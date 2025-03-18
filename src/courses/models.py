from django.db import models



class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = 'email_required', 'Email Required'

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'soon', 'Coming Soon'
    
    


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # image= models.ImageField()
    access = models.CharField(max_length=20, choices=AccessRequirement.choices, default=AccessRequirement.ANYONE)
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAFT)