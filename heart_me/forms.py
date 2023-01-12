from django import forms
from django_countries.data import COUNTRIES

class HeartDiseaseForm(forms.Form):
    
    age = forms.FloatField( label='Age', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.FloatField(label='Sex 0 for male , 1 for female', min_value=0, max_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cp = forms.FloatField(initial=0,label='CP from 0(min) to 4(max)', min_value=0, max_value=4, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    trestbps = forms.FloatField(label='TRESTBPS', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chol = forms.FloatField(label='CHOL', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fbs = forms.FloatField(label='FBS', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    restecg = forms.FloatField(label='RESTECG', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thalach = forms.FloatField(label='THALACH', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exang = forms.FloatField(label='EXANG', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    oldpeak = forms.FloatField(label='OLDPEAK', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    slope = forms.FloatField(label='SLOPE', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ca = forms.FloatField(label='CA', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thal = forms.FloatField(label='THAL', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')
class registerForm(forms.Form):
    name = forms.CharField(label='name' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    age = forms.IntegerField(label='age', min_value=0, max_value=100,initial="",widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages={'required': 'Please enter your age'})
    country = forms.ChoiceField(label='country',initial="India",choices = sorted(COUNTRIES.items()),help_text='country.',error_messages={'required': 'Please select country'})
    state = forms.CharField(label='state' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    home_address= forms.CharField(label='Home_address' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your home address'}  )
    Practisable_Hospital_Address= forms.CharField(label='Practisable hospital Address' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=1000,error_messages={'required': 'Please enter your address'}  )
    Email= forms.EmailField(label='Email' ,initial="@gmail.com" ,widget=forms.EmailInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    State_Council_ID= forms.CharField(label='state_council_id' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    Hospital_ID= forms.CharField(label='Hospital_Id' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    Userame= forms.CharField(label='Username' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    Password= forms.CharField(label='Password' ,initial="" ,widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    
    confirm_Password= forms.CharField(label='Confirm password' ,initial="" ,widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100,error_messages={'required': 'Please enter your name'}  )
    Agreeing_to_terms_and_conditions= forms.CharField(label='Agreeing to  terms and conditions' ,initial="" ,widget=forms.CheckboxInput(attrs={'class':'form-control'}),max_length=100, help_text='100 characters max.',error_messages={'required': 'Please enter your name'}  )
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')