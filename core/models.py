from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.URLField()
    about_me = models.TextField()
    
    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.institution} - {self.degree}"
    
    class Meta:
        ordering = ['-year']

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    roles = models.TextField()
    achievements = models.TextField()
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-id']

class Skill(models.Model):
    SKILL_TYPES = (
        ('technical', 'Technical Skill'),
        ('soft', 'Soft Skill'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    
    def __str__(self):
        return self.name

class Reference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name