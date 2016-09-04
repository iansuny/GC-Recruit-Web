from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=50, default='Medical Health')
	def __str__(self):
		return str(self.name)

class Talent(models.Model):
	name = models.CharField(max_length=50, default='Math')
	def __str__(self):
		return self.name

class Badge(models.Model):
	name = models.CharField(max_length=50, default='none')
	def __str__(self):
		return self.name
class Team(models.Model):
	name = models.CharField(max_length=50, default='none')
	need = models.IntegerField(max_length=5, default=0)
	interest = models.ForeignKey(Interest)
	def __str__(self):
		return self.name


class Student(models.Model):
	#name = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.ForeignKey(User, unique=True,)
	realname = models.CharField(max_length=50, default='')
	nickname = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	motto = models.CharField(max_length=20, blank=True)
	interest = models.ForeignKey(Interest, null=True)
	talent = models.ForeignKey(Talent, null=True)#many student to one talent
	badge = models.ForeignKey(Badge, default=1 )#many student to one badge???
	team = models.ForeignKey(Team, default=1 )#many student to one team
	follow=models.ManyToManyField('self', blank=True, symmetrical=False)
	class Meta:
		permissions = (
			("can_edit_base_profile", "Can edit base profile"),
			("can_view_base_profile", "Can view base profile"),

		)
	def __str__(self):
		return self.realname

#class Follow(models.Model):
	
	#this is name's shopping cart
	#query:user.follow_set
	#name = models.OneToOneField(User)
	#students = models.ManyToManyField(Student)
	#def __str__(self):
		#return self.name.username