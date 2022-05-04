from django.db import models

states=state_choices = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"))
class Candidate(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    pin=models.PositiveBigIntegerField()
    state=models.CharField(choices=states,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_preference=models.CharField(max_length=20)
    candidate_image=models.ImageField(upload_to="canimages",blank=True,verbose_name="Candidate Images:")
    can_file=models.FileField(upload_to="canfiles",blank=True,verbose_name="Candidate File:")


