from django.db import models


# Create your models here.
class person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
class news(models.Model):
	title=models.CharField(max_length=1000)
	description=models.TextField()
	image=models.ImageField(upload_to="data",blank=True)
	date=models.DateField()
class publications(models.Model):
	book_name=models.CharField(max_length=1000)
	Author_name=models.CharField(max_length=1000)
	File=models.FileField()
class video(models.Model):
	title=models.CharField(max_length=1000)
	images=models.ImageField(upload_to="data",blank=True)
	video=models.FileField()
class services(models.Model):
	sevice_name=models.CharField(max_length=1000)
	description=models.TextField()
	images=models.ImageField(upload_to="data",blank=True)
class current_issue(models.Model):
	title=models.CharField(max_length=1000)
	description=models.TextField()
	image=models.ImageField(upload_to="data",blank=True)
	date=models.DateField()
class FAQ(models.Model):
	question=models.TextField()
	answer=models.TextField()
class laws(models.Model):
     year=models.TextField()
     description=models.TextField()
class university(models.Model):
      uni_name=models.CharField(max_length=1000)
      description=models.TextField()
      images=models.ImageField(upload_to="data",blank=True)
      subject_score=models.CharField(max_length=1000)
      global_score=models.CharField(max_length=1000)
      enrollement=models.CharField(max_length=100)
      country_name=models.CharField(max_length=1000)
      city=models.CharField(max_length=1000)
class energy(models.Model):
      name=models.CharField(max_length=1000)
      description=models.TextField()
      author=models.CharField(max_length=1000)
      date=models.DateField()
      image=models.ImageField(upload_to="data",blank=True)
      
      
class health(models.Model):
	name=models.CharField(max_length=1000)
	description=models.TextField()
	author=models.CharField(max_length=1000)
	date=models.DateField()
	image=models.ImageField(upload_to="data",blank=True)
class technology(models.Model):
	  name=models.CharField(max_length=1000)
	  description=models.TextField()
	  author=models.CharField(max_length=1000)
	  date=models.DateField()
	  image=models.ImageField(upload_to="data",blank=True)
class myregister(models.Model):
      first_name=models.CharField(max_length=1000)
      last_name=models.CharField(max_length=1000)
      phone=models.CharField(max_length=1000)
      Email=models.EmailField()
      Password=models.CharField(max_length=1000)
class  myhelp(models.Model):
	  title=models.CharField(max_length=1000)
	  message=models.CharField(max_length=1000)
class myrev(models.Model):
      title=models.CharField(max_length=1000)
      message=models.CharField(max_length=1000)

class userRegister(models.Model):
	first_name=models.CharField(max_length=1000)
	last_name=models.CharField(max_length=1000)
	phone=models.CharField(max_length=1000)
	Email=models.CharField(max_length=1000)
	Password=models.CharField(max_length=1000)	  
	Address=models.CharField(max_length=1000,blank=True,null=True)	  
	DOB=models.CharField(max_length=1000,blank=True,null=True)	  



	  








       		       
      

			

			


