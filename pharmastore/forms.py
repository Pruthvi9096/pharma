from django import forms
from .models import DrugRequest,Pharmacy
from django.utils import timezone
from datetime import datetime
from django.utils.timezone import now, localtime
from django.core.validators import ValidationError
from django.utils.translation import gettext as _
import time

class PharmacyForm(forms.ModelForm):
    # delivery = forms.BooleanField(required=False,initial=False,label='Extra cheeze')
    class Meta:
        model = Pharmacy
        fields = '__all__'
        widgets = {
          'address': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'city': forms.TextInput(attrs={'placeholder':'City'}),
          'state': forms.TextInput(attrs={'placeholder':'State'}),
          'zip': forms.TextInput(attrs={'placeholder':'Zip'}),
          'delivery': forms.Select(attrs={'class':'form-control'}),
        }

class RequestForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'required':False}))
    def clean_pd_date(self):
        pd_date = self.cleaned_data['pd_date']
        print(type(pd_date))
        if pd_date < timezone.now():
            raise ValidationError(_("Past Date is Not Allowed"))
        return pd_date
    
    # def clean_pd_time(self):
    #     pd_time = self.cleaned_data['pd_time']
    #     print(time.localtime().)
    #     print("=======",pd_time,"====",datetime.now().time(),"====",timezone.timedelta(hours=2))
    #     if pd_time <= (localtime() + timezone.timedelta(hours=2)).time():
    #         raise ValidationError(_("Please Enter Time after 2 hours"))
    #     return pd_time

    class Meta:
        model = DrugRequest
        fields = '__all__'
        widgets = {
          'note': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'address': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'city': forms.TextInput(attrs={'placeholder':'City'}),
          'state': forms.TextInput(attrs={'placeholder':'State'}),
          'zip': forms.TextInput(attrs={'placeholder':'Zip'}),
          'pd_date':forms.TextInput(attrs={'type':'date'}),
          'dob':forms.TextInput(attrs={'type':'date'}),
          'pd_time':forms.TextInput(),
        }
