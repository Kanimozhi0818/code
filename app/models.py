from django.db import models
from django.utils import timezone
class Register_Detail(models.Model):
	username = models.CharField(max_length=50,unique=True)
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	mobile = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	zip = models.CharField(max_length=50)
	user_type = models.CharField(max_length=50)
	def __str__(self):
		return self.username
class CA_Login(models.Model):
	username = models.CharField(max_length=50,unique=True)
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	mobile = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	zip = models.CharField(max_length=50)
	def __str__(self):
		return self.username
class Upload_File(models.Model):
	user_id = models.ForeignKey(Register_Detail, on_delete=models.CASCADE,null=True)
	name = models.CharField('File Name',max_length=100)
	file = models.FileField('File',upload_to='',null=True)
	notes = models.TextField('Notes',max_length=2000)
	date = models.DateField('Uploaded Date',default=timezone.now())
	def __str__(self):
		return self.name
	def publish(self):
		self.date = timezone.now()
		self.save()
class File_Request(models.Model):
	user_id = models.ForeignKey(Register_Detail, on_delete=models.CASCADE)
	file_id = models.ForeignKey(Upload_File, on_delete=models.CASCADE)
	public_key = models.CharField('Public Key',max_length=1000,null=True,blank=True)
	private_key = models.CharField('Private Key',max_length=1000,null=True,blank=True)
	status = models.CharField('Status',max_length=1000)
	def __str__(self):
		return self.file_id.name
class File_Key(models.Model):
	file_id = models.ForeignKey(Upload_File, on_delete=models.CASCADE)
	file_key = models.CharField('keywords',max_length=1000,null=True,blank=True)
	def __str__(self):
		return self.file_id.name
