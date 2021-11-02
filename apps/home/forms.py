from django import forms
from django.forms import ModelForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import Order_incomings
from . import models




#------------------------------------------------------------------------------
class TimeForm(forms.ModelForm):
    class Meta:
        model = Order_incomings
        fields = ('date_created',)

    def __init__(self, *args, **kwargs):
        super(TimeForm, self).__init__(*args, **kwargs)
        self.fields['date_created'] = JalaliDateField( widget=AdminJalaliDateWidget(attrs={'style':'width:15px; height:37px'}) )
        self.fields['date_created'].required = False
        self.fields['date_created'].label = False
