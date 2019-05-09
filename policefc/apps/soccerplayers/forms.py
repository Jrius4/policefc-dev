from django import forms
from .models import SoccerPlayer, ExecutiveTeam, TeamPosition
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SoccerPlayersForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}
    ))

    class Meta:
        model = SoccerPlayer
        fields = ('full_name','short_description','bio','team_positions','strongest_foot','ratings','dob','former_team','author','bio_picture','featured_picture','featured',)


class ExecutiveForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}
    ))

    class Meta:
        model = ExecutiveTeam
        fields = ('full_name','title','short_description','bio','author','featured_picture','featured')


# class ExecutivesForm(forms.ModelForm):
#     class Meta:


# class TechnicalTeamForm(forms.ModelForm):
#     class Meta:


# class StoreForm(forms.ModelForm):
#     class Meta:
#         pass