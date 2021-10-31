
from django.core.serializers import serialize
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from .models import About, Achievement, Education,Experience, Home_tag, Interest, Link, Project, Skill_Type

def index(request):
    return JsonResponse({
                "0":"/all",
                "1":"/home",
                "2":"/about",
                "3":"/interests",
                "4":"/education",
                "5":"/experience",
                "6":"/achievements/",
                "7":'/projects',
                "8":'/links',
                "9":'/skills'
        })

def get_home(home):
    result={}
    result["title"]=home.title
    temp=home.tags.all()
    arr=[]
    for _ in temp:
        arr.append(_.title)
    result["tags"]=arr
    return result

def home(request,flag=False):
    temp=Home_tag.objects.all()
    result=None
    for _ in temp:
        result=get_home(_)
    if flag:
        return result
    return JsonResponse(result)

def about(request,flag=False):
    temp=About.objects.all()
    result={}
    for _ in temp:
        result["about"]=_.description 
    if flag:
        return result
    return JsonResponse(result)

def interest(request,flag=False):
    result={}
    temp=Interest.objects.all()
    i=1
    for _ in temp:
        result[i]={"title":_.title,"icon":_.icon,"description":_.description}
        i+=1
    if flag:
        return result
    return JsonResponse(result)

def education(request,flag=False):
    result={}
    temp=Education.objects.all()
    i=1
    for _ in temp:
        temp=_.description.all()
        l=[]
        for e in temp:
            l.append(e.description)
        result[i]={"title":_.title,
                   "school":_.school,
                   "start":_.start_year,
                   "end":_.end_year,
                   "description":l
                  }
        i+=1
    if flag:
        return result
    return JsonResponse(result)

def experience(request,flag=False):
    result={}
    temp=Experience.objects.all()
    i=1
    for _ in temp:
        temp=_.description.all()
        l=[]
        for e in temp:
            l.append(e.description)
        result[i]={"title":_.title,
                   "company":_.company,
                   "start":_.start_year,
                   "end":_.end_year,
                   "description":l
                  }
        i+=1
    if flag:
        return result
    return JsonResponse(result) 


def achievement(request,flag=False):
    result={}
    temp=Achievement.objects.all()
    i=1
    for _ in temp:
        result[i]={"title":_.title,
                   "icon":_.icon,
                   "description":_.description}
        i+=1
    if flag:
        return result
    return JsonResponse(result)

def project(request,flag=False):
    result={}
    temp=Project.objects.all()
    i=1
    for _ in temp:
        temp=_.tags.all()
        arr=[]
        for e in temp:
            arr.append(e.title)
        result[i]={"title":_.title,
                   "description":_.description,
                   "image":_.image,
                   "url":_.url,
                   "type":_.type,
                   "tags":arr
                }
        i+=1
    if flag:
        return result
    return JsonResponse(result)
    
def link(request,flag=False):
    result={}
    temp=Link.objects.all()
    i=1
    for _ in temp:
        result[i]={"title":_.title,
                   "url":_.url}
        i+=1
    if flag:
        return result
    return JsonResponse(result)

def skills(request,flag=False):
    result={}
    temp=Skill_Type.objects.all()
    for _ in temp:
        l=[]
        temp=_.skill.all()
        for e in temp:
            l.append({"title":e.title,
                      "url":e.icon
                })
        result[_.title]=l
    if flag:
        return result
    return JsonResponse(result)

def all_data(request):
    result={}
    hom=home(request,True)
    abt=about(request,True)
    interest_=interest(request,True)
    education_=education(request,True)
    experience_=experience(request,True)
    achievement_=achievement(request,True)
    project_=project(request,True)
    link_=link(request,True)
    skill=skills(request,True)
    result["home"]=hom
    result["about"]=abt
    result["interests"]=interest_
    result["education"]=education_
    result["experience"]=experience_
    result["skill"]=skill
    result["achievements"]=achievement_
    result["projects"]=project_
    result["links"]=link_
    return JsonResponse(result)

        