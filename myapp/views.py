from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import formcontact
from Blog.models import BlogPortal
from django.template import Context
from datetime import date, timedelta, datetime



def index(request):
    return render(request, 'index.html')


def resume(request):
    now = datetime.datetime.now()
    now = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    context = {"cont": {"d_name": "ABINASH S", "d_mail": "s.abinash@outlook.com", "d_phone": "+91 9003326846", "datetime": now}}
    return render(request, 'resume.html', context)

def contact(request):
    rep_str=""
    saved={}
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        no=request.POST['no']
        rep_str="First Name: "+fname+"<br>Last Name: "+lname+"<br>No: "+no
        form=formcontact(fname=fname, lname=lname, no=no)
        form.save()
        return HttpResponse(rep_str)
    return render(request, 'contact.html', context={ 'data':saved})


def getcontact(request):
    contacts={}
    allc=formcontact.objects.all()
    for i in allc:
        contacts[i.id]={'fname':i.fname,'lname':i.lname,'no':i.no}
    for i in contacts.values():
        print(i)
    return render(request, 'GetContacts.html', context={"contacts":contacts})


def current_datetime(request):
    date_1 = date.today()
    hrs=0
    txt="Current"
    if request.method == "POST":
        hrs = request.POST['hrs']
        txt="Added"
    date_1 = date_1 + timedelta(days=int(hrs))
    return render(request, 'DateTimeAdd.html', context={"cur_date": date_1, "text": txt})

def calculate_age(request):
    cur = datetime.now()
    string=""
    if request.method == "POST":
        dob = request.POST['dob']
        dob = datetime.strptime(dob,'%Y-%m-%d')
        days = (cur-dob).days
        year=str(int(days/365))
        days=days-year*365
        month=str(int(days/12))
        days=str(int(days-month*12))
        string = "Your age is "+year+" years "+month+" months "+days+" days "
    return render(request, 'AgeCalculation.html', context={'age':string})


def read_disp(request):
    str1 = input()
    name = "<h1>Hello %s</h1>" % str1
    return HttpResponse(name)


def blogcreate(request):
    if request.method == "POST":
        title = request.POST['title']
        tags = request.POST['tags']
        content = request.POST['content']
        author = request.POST['author']
        blog = BlogPortal(title=title, tags =tags, content=content, author=author)
        blog.save()
    return render(request, 'blogs.html', context={'msg': "Blog Saved Successfully"})


