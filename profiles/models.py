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
	need = models.IntegerField(max_length=5)
	interest = models.ForeignKey(Interest)
	def __str__(self):
		return self.name

class Follow(models.Model):
	name = models.CharField(max_length=50, default='none')
	def __str__(self):
		return self.name

class Student(models.Model):
	#name = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.ForeignKey(User, unique=True,)
	realname = models.CharField(max_length=50, default='')
	nickname = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	motto = models.CharField(max_length=20, blank=True)
	interest = models.ForeignKey(Interest, default=1)
	talent = models.ForeignKey(Talent, default=1)
	badge = models.ForeignKey(Badge, default=1 )
	team = models.ForeignKey(Team, default=1 )
	follow = models.ForeignKey(Follow, default=1)
	class Meta:
		permissions = (
			("can_edit_base_profile", "Can edit base profile"),
			("can_view_base_profile", "Can view base profile"),

		)
	def __str__(self):
		return self.realname

class Chatroom(models.Model):
	# roomname = models.CharField(max_length=50)
	student1 = models.ForeignKey(Student, null=True, related_name='student1')
	student2 = models.ForeignKey(Student, null=True, related_name='student2')
	content = models.CharField(max_length=50)
	date_time = models.DateTimeField()
	def __str__(self):
		return self.content



