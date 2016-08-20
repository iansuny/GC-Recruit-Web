from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=50, default='Medical Health')
	def __unicode__(self):
		return self.name

class Talent(models.Model):
	name = models.CharField(max_length=50, default='Math')
	def __unicode__(self):
		return self.name

class Badge(models.Model):
	name = models.CharField(max_length=50, default='beginner')
	def __unicode__(self):
		return self.name
class Team(models.Model):
	name = models.CharField(max_length=50, default='ntu')
	need = models.IntegerField(max_length=5)
	interest = models.ForeignKey(Interest)
	def __unicode__(self):
		return self.name

class Follow(models.Model):
	name = models.CharField(max_length=50, default='student1')
	def __unicode__(self):
		return self.name

class Student(models.Model):
	#name = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.ForeignKey(User, unique=True,)
	realname = models.CharField(max_length=50, default='')
	nickname = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	motto = models.CharField(max_length=20, blank=True)
	interest = models.ForeignKey(Interest, null=True)
	talent = models.ForeignKey(Talent, null=True)
	badge = models.ForeignKey(Badge, null=True)
	team = models.ForeignKey(Team, null=True)
	follow = models.ForeignKey(Follow, null=True)
	class Meta:
		permissions = (
			("can_edit_base_profile", "Can edit base profile"),
		)


