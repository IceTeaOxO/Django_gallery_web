from calendar import weekday
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import User # 新增的程式碼
import random
import datetime
from datetime import date
# Create your views here.
def add(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        user_img = request.FILES.get('user_image')
        user = User(user_image=user_img)
        user.save()
        
        print("-----------")
        return render(request, 'index.html', locals())
    # =====新增的程式碼=====#  
      
    keyword = timer()
    return render(request, 'index.html', locals())
def detail(request):
    list_user = User.objects.all() # 把資料庫中所有的user資料全部撈出來
    return render(request, 'gallery.html', locals())


def randPick(seednum):
    random.seed(seednum)
    colorK = ["red","blue","green","black","white",'yellow',"pink","gray"]
    genderK = ["female","male","no gender"]
    ageK = ["0~10","11~15","16~20","20~30","30~40","40up"]
    #這邊其實可以做成資料庫，但是我目前沒打算做那麼大
    colorV = colorK[random.randrange(8)]
    genderV = genderK[random.randrange(3)]
    ageV = ageK[random.randrange(6)]
    
    return colorV,genderV,ageV
    #,genderV,ageV

def timer():#檢查日期是否有改變
    today = datetime.date.today()
    # print(today.day)
    # print(type(today.weekday()))#星期一為0，星期二為1，可以用這個設置每週一刷新
    # print(today.weekday())
    weekday = today.weekday()
    #暫時寫不出來，將就一下直接把日期當成隨機種子吧
    # print(weekday)
    K = randPick(weekday)

    # if(today.weekday==int(0)):#如果是禮拜一就隨機產生關鍵字
    #     K = randPick
    #     print("ok")
    # else:
    #     random.seed(314)#固定隨機結果
    #     K = randPick
    #     print("error")
    return K