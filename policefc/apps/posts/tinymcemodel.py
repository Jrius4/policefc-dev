from django.db import models
# from tinymce import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

class PostTiny(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    # content = HTMLField('Content')
    content = RichTextUploadingField(null=True,blank=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title