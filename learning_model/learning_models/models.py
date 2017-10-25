#coding=utf-8
from django.db import models

'''　查询集特性　１.惰性查询 2.缓存 '''

#Django中管理器就是ORM,与数据库做交互,模型中的类的对象和数据库做映射
#自定义管理器的第一个作用
#重写方法,修改管理器返回的原始查询集
class BookInfoManager(models.Manager):
    def get_queryset(self):
                                            #原查询的基础上，再筛选
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    #__init__在框架中已经用了，修改管理器的第二作用，方便创建对象
    def create(self,btitle,bpub_date):
        b=BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.read = 0
        b.bcommet = 0
        b.isDelete = False
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    def __unicode__(self):
        return self.btitle
    #元选项：类中定义类
    class Meta:
        #数据表改名为bookinfo
        db_table='bookinfo'
        #默认排序规则,增加数据库开销
        #ordering = ['(/-)id']
    #管理器默认为objects,可修改,支持自定义
    books1=models.Manager()
    #自定义管理器
    books2=BookInfoManager()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=1000)
    book = models.ForeignKey('BookInfo')

