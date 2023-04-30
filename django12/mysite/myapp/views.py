from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import AdminForm
import mysql.connector as sql
from django.http import HttpResponseRedirect
from .forms import upload

# Create your views here.
def index(request):

        return render(request,'myapp/index.html')
def loginaction(request):

        
        global em,pwd
        if request.method=="POST":
                form=AdminForm(request.POST)
                if form.is_valid():
                        em=form.cleaned_data['email']
                        pwd=form.cleaned_data['password']
                m=sql.connect(host="localhost",user="root",passwd="Alk@@008",database="db")
                cursor=m.cursor() 
                c="select * from tbl where email='{}' and password='{}'".format(em,pwd)
                cursor.execute(c)
                t=tuple(cursor.fetchall())
                if t==():
                        return HttpResponseRedirect("error")
            
                else:
                        return HttpResponseRedirect('welcome')
        form=AdminForm()
        return render(request,'myapp/ln.html',{'forms':form})
def welcomeaction(request):
        if request.method=='POST':
                form=upload(request.POST,request.FILES)
                if form.is_valid():
                        form.save()
                        return HttpResponse("hi")
        else:
                form=upload()
                return render(request,'myapp/admmm.html',{'forms':form})
 
          