#coding=utf-8
from django.shortcuts import render
from models import *
from django.db.models import Max,F,Q
#F对象一个列对比另外一个列比较筛选
#Q对象实现逻辑或筛选

def index(request):
    #list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')
    #list = BookInfo.books1.filter(pk__lte=3)
    #Max1 = BookInfo.books1.aggregate(Max('bpub_date'))
    #list = BookInfo.books1.filter(bread__gt=F('bcommet'))
    # list = BookInfo.books1.filter(pk__lte=3).filter(btitle__contains='1')－－逻辑与的关系　　要实现逻辑或用Ｑ对象
    list = BookInfo.books1.filter(Q(pk__lte=3) | Q(btitle__contains='1')) #逻辑或关系
    context = {'list1':list
                    #,'Max1':Max1
             }
    return render(request,'learning_models/index.html',context)