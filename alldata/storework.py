from django.db import models

class Worksubmit(models.Model):
	uniqueID=models.CharField(max_length=70,null=True)
	work_from=models.TimeField(null=True)
	Team_Leader=models.CharField(max_length=70,null=True)
	Mentor=models.CharField(max_length=70,null=True)
	Member_Name=models.CharField(max_length=70,null=True)
	Work_Description=models.TextField(null=True)
	work_to=models.TimeField(null=True)

	def __str__(self):
		return str(self.uniqueID)
