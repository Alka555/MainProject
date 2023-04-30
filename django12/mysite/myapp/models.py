from django.db import models
filetypes = (
    ('pdf','pdf'),
    ('jpeg', 'jpeg'),
    ('mp3','mp3'),
    ('mp4','mp4'),
    ('docx','docx'),
)
# Create your models here.
class Document(models.Model):
    filetype=models.CharField(choices=filetypes,max_length=10) 
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

