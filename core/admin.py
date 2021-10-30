from django.contrib import admin
from .models import About,Home_tag,Interest,Tag,Education,Achievement,Link,Project,Bullet,Experience,Skill,Skill_Type
# Register your models here.

admin.site.register(Home_tag)
admin.site.register(About)
admin.site.register(Interest)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Achievement)
admin.site.register(Project)
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(Bullet)
admin.site.register(Skill_Type)
admin.site.register(Skill)