from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import CharField, related


# Create your models here.


class Tag(models.Model):
    title=models.CharField(max_length=32)
    def __str__(self):
        return self.title

class Home_tag(models.Model):
    title=models.CharField(max_length=52)
    tags=models.ManyToManyField(Tag,related_name="Tags")
    def __str__(self):
        return self.title

class About(models.Model):
    description=models.TextField(max_length=512)
    def __str__(self):
        return "About"

class Interest(models.Model):
    title=models.CharField(max_length=20)
    icon=models.URLField()
    description=models.CharField(max_length=256)
    def __str__(self):
        return self.title

class Bullet(models.Model):
    description=models.TextField()
    def __str__(self):
        return self.description

class Education(models.Model):
    title=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    start_year=models.DateField()
    end_year=models.DateField()
    description=models.ManyToManyField(Bullet,related_name="education_bullet")
    def __str__(self):
        return self.title

class Experience(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    start_year=models.DateField()
    end_year=models.DateField()
    description=models.ManyToManyField(Bullet,related_name="experience_bullet")
    def __str__(self):
        return self.title

class Achievement(models.Model):
    title=models.CharField(max_length=20)
    icon=models.URLField()
    description=models.TextField(max_length=256)
    def __str__(self):
        return self.title

class Link(models.Model):
    title=models.CharField(max_length=200)
    url=models.URLField()
    def __str__(self):
        return self.title

class Skill(models.Model):
    title=models.CharField(max_length=200)
    icon=models.URLField()
    def __str__(self):
        return self.title

class Skill_Type(models.Model):
    title=models.CharField(max_length=200)
    skill=models.ManyToManyField(Skill,related_name="skill")
    def __str__(self):
        return self.title

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.URLField()
    url=models.URLField(blank=True)
    type=models.CharField(max_length=200,choices=(("Mech","Mechanical"),("Comp","Computer"),("Other","Other")),default="Comp")
    tags=models.ManyToManyField(Tag,related_name="Project_tag")
    def __str__(self):
        return self.title
