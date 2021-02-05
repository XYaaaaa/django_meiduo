from django.db import models
# ORM model
# Create your models here.
# Models need to inherit from models.Model
#class = table, 
class BookInfo(models.Model): #book information
    #id inherit
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'bookinfo'
        verbose_name ='书籍管理'

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null = True)
    is_delete= models.BooleanField(default=False)
    
    
    #key constraint
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE) #级联，表明主表数据删除时连着从表的数据一块删除
    
    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name