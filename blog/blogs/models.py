from django.db import models

class Blogs(models.Model):
    blog_name= models.CharField(max_length=200)
    blog_date= models.DateTimeField('date published')
    blog_text= models.CharField(max_length=4000)

    def __str__(self):
        return self.blog_name

    class Meta:
        ordering = ('blog_name',)

class Tags(models.Model):
    tag = models.CharField(max_length=100)
    publications = models.ManyToManyField(Blogs)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('tag',)
