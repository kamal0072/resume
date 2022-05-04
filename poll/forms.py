from django import forms
from .models import Candidate
GENDER=[
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
    ]
CITY_CHOICES=[
    ("Pune","Pune"),
    ("Delhi","Delhi"),
    ("Lucknow","Lucknow"),
    ("Mumbai","Mumbai"),
    ("Banglore","Banglore"),
    ("Chennai","Chennai"),
    ("Delhi","Delhi"),
    ("Noida","Noida"),
    ("Gurgaon","Gurgaon"),
    ("Tamilnadu","Tamilnadu"),
    ("Punjab","Punjab"),
]
class Candidateform(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER,
            widget=forms.RadioSelect(attrs={'class':"ml-3"}))
    city=forms.MultipleChoiceField(label="Preferred Location:",choices=CITY_CHOICES,
                        widget=forms.CheckboxSelectMultiple(attrs={'class':'ml-3'}))
    class Meta:
        model=Candidate
        fields=[
        "name",'dob',"gender","location",'city','pin','state','mobile',
        'email','candidate_image','can_file',
                ]
        labels={
            "name":"Full Name",
            "dob":"Date Of Birth",
            "pin":'Pin Code',
            "mobile":"Mobile Number",
            "email":"Email Address",
            "candidate_image":"Candidate Image",
            "can_file":"Candidate File",
        }
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "dob":forms.DateInput(attrs={'class':"form-control","id":"datepicker"}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }