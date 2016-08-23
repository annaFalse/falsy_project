from django.db import models

class Blogs(models.Model):
    header = models.TextField(blank=True)
    blog_name= models.CharField(max_length=200)
    blog_date= models.DateTimeField('date published')
    blog_text= models.CharField(max_length=4000)
    tags = models.ManyToManyField(Tags)

    def __unicode__(self):
        return self.header

class Tags(models.Model):
    tag = models.CharField(blank=True, null=False, max_length=64, unique=True)

    def __unicode__(self):
        return self.tag




