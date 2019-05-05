
from django import forms
from .models import Comment, Post
from .tinymcemodel import PostTiny
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class PostFormSample(forms.ModelForm):
    class Meta:
        model=PostTiny
        fields=['title','description','content','draft']



class PostForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorUploadingWidget(
        attrs={'required':False,
        'cols':30,'rows':10
        }
    ))
    class Meta:
        model = Post
        fields = ('title','overview','content',
        'thumbnail','categories','featured','previous_post','next_post',)




class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id':'usercomment',
        'rows':'4',
    }))
    class Meta:
        model = Comment
        fields = ('content',)
