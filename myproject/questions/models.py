from django.db import models

# Create your models here.
GENDER = {
    'female': 'Female',
    'Male': 'Male'
}
TRIBE= { 'Igbo':1,'Hausa':2, 'Yoruba':3} 
REL= {
    1 :'Christianity', 2: 'Islam',3: 'Traditional African Religion', 4:'Atheist'
}
MOTHER_EDU_LEVEL = {
   1: 'None formal', 2: 'Primary',3: 'Secondary',4: 'Tertiary' 
}
FATHER_EDU_LEVEL = {
     1: 'None formal', 2: 'Primary',3: 'Secondary',4: 'Tertiary' 
}
SES_PARENTS={
    1: 'Upper class – professional',2: 'Upper middle class - managerial',3:'Lower middle class clerical/skilled', 4: 'Upper lower class – semi-skilled',5: 'Lower class – unskilled'
}

class Question(models.Model):
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, default=0,max_length=100)
    religion = models.IntegerField(choices=REL,default=0)
    tribe= models.CharField(max_length=50,choices=TRIBE,default='0')
    level= models.CharField(max_length=50,default='none')
    mum_occup = models.CharField(max_length=50,default='none')
    mother_edu_level= models.IntegerField(choices=MOTHER_EDU_LEVEL,default=0)
    father_edu_level= models.IntegerField(choices=FATHER_EDU_LEVEL,default=0)
    dad_occup = models.CharField(max_length=50,default='none',blank=True)
    ses_parents= models.IntegerField(max_length=50, choices=SES_PARENTS,default=0)
    por= models.CharField(max_length=50)