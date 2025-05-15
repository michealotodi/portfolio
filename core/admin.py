from django.contrib import admin
from .models import Profile, Education, Experience, Skill, Reference

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline, SkillInline, ReferenceInline]
    list_display = ('name', 'email', 'phone')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'year', 'location')
    list_filter = ('year',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'period')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type')
    list_filter = ('skill_type',)

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')