from django.db import models
from django.contrib.auth.models import User

# Create your models here.=
GENERAL='general'
FOOD='food'
TRAVEL= 'travel'
HEALT= 'health'
EDUCATION= 'education'
ENTERTAINMENT= 'entertainment'
IT= 'it'
POLITICS= 'politics'
GEO_POLITICS= 'geo_politics'
COMMERCE= 'commerce'
CULTURE= 'culture'
SPORTS= 'sports'
ENVIRONMENT= 'environment'
RELIGION= 'religion'

Category_Choices = [
        (GENERAL, 'genral'),
        (FOOD, 'food'),
        (TRAVEL, 'travel'),
        (HEALT, 'health'),
        (EDUCATION, 'education'),
        (ENTERTAINMENT, 'entertainment'),
        (IT, 'it'),
        (POLITICS, 'politics'),
        (GEO_POLITICS, 'geo_politics'),
        (COMMERCE, 'commerce'),
        (CULTURE, 'culture'),
        (SPORTS, 'sports'),
        (ENVIRONMENT, 'environment'),
        (RELIGION, 'religion'),
    ]

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='blog_author')
    blog_title = models.CharField(max_length =256, verbose_name= 'Title of the Blog')
    slug = models.SlugField(max_length =256,unique = True)
    blog_content = models.TextField(verbose_name='Your Story Here..')
    blog_pic = models.ImageField(upload_to='blog_images')
    category = models.CharField(max_length=20,choices=Category_Choices,default='general')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name ='blog_comment', on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name ='user_comment', on_delete = models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog,related_name ='blog_liked', on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name ='user_liked', on_delete = models.CASCADE)

    def __str__(self):
        return self.user +" likes " + self.blog

class Love(models.Model):
    blog = models.ForeignKey(Blog,related_name ='blog_loved', on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name ='user_loved', on_delete = models.CASCADE)

    def __str__(self):
        return self.user +" loves " + self.blog
