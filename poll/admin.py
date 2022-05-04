from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display=[
        "id","name",'dob',"gender","location",'city','pin','state','mobile',
        'email','job_preference','candidate_image','can_file',
    ]
    
