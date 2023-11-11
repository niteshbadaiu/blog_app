from django.db import models

# Create your models here.
class Blog(models.Model):
    CAT=(
        (1,"Python"),
        (2,"Data Science"),
        (3,"Data Analysis"),
        (4,"Java"),
    )
    title=models.CharField(max_length=50,verbose_name="Blog Title")
    details=models.CharField(max_length=1000,verbose_name="Blog Details")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    created_at=models.DateTimeField()
    is_published=models.BooleanField(default=False,verbose_name="Published On")
    uid=models.IntegerField()

    def __str__(self):
        return self.title
    

# student model
class Student(models.Model):
    name=models.CharField(max_length=50)
    rno=models.IntegerField()
    p=models.FloatField()