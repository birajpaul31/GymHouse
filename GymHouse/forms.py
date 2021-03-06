from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from mainpage.models import Profile, Event, Class, Days
"""
from mainpage.models import Class
from mainpage.models import Days
"""
class NewEventForm(ModelForm):
    class Meta:
        model = Event
        #fields = '__all__'
        exclude = ['creator']

        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
        """
        labels = {
            'name': _('Event name'),
            'description': _('Event description'),
            'date': _('Date of the event'),
            'participants': _('Participants'),
            'trainer': _('Trainer for the event'),
            'level': _('Exercise level'),
        }
        help_texts = {
            'name': _('Event name will be shown in the calendar'),
        }

        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

        """


class NewClassForm(ModelForm):
    # Needed or not???
    """
    def __init__(self, *args, **kwargs):
        super(NewClassForm, self).__init__(*args, **kwargs)
        self.fields['days'].empty_label = None
    """
    MONDAY =        '0'
    TUESDAY =       '1'
    WEDNESDAY =     '2'
    THURSDAY =      '3'
    FRIDAY =        '4'
    SATURDAY =      '5'
    SUNDAY =        '6'

    DAY_CHOICES = (
        (MONDAY,    'Monday'),
        (TUESDAY,   'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY,  'Thursday'),
        (FRIDAY,    'Friday'),
        (SATURDAY,  'Saturday'),
        (SUNDAY,    'Sunday'),
    )

    class Meta:
        model = Class
        exclude = ['creator']
        #'time': forms.TimeInput(format='%H:00'),
        #days = forms.ModelMultipleChoiceField(queryset=Days.objects.all(), widget=forms.CheckboxSelectMultiple)

        widgets = {
                'begin_date': forms.DateInput(attrs={'class': 'datepicker'}),
                'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
                'days': forms.CheckboxSelectMultiple()
        }
        #days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
        days = forms.ModelMultipleChoiceField(queryset=Days.objects.all(), widget=forms.CheckboxSelectMultiple)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class RegistrationForm(ModelForm):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Profile
        exclude = ['user', 'image', 'registrations']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            print("OASSWORDS DONT MATCH")
            raise forms.ValidationError(
                "Passwords don't match. "
            )



        """

        """
