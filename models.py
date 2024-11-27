from django.db import models

# Create your models here.

class FormdataForm(models.Modelform):
	class Meta:
		= FormData
		fields = ['student_id', 'roll_no']



class FormdataForm(models.Model):
	name = models.Charfield(max_length)