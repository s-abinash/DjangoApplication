from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import FormContact
from myapp.models import BioForm
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
        form=FormContact(fname=fname, lname=lname, no=no)
        form.save()
        return HttpResponse(rep_str)
    return render(request, 'contact.html', context={ 'data':saved})


def getcontact(request):
    contacts={}
    allc=FormContact.objects.all()
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


def bio_insert(request):
    error = []
    message = ""
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        print(fname, lname, email, phone,age)
        if '@' not in email:
            error.append(" email should have @ ")
        else:
            ins = BioForm(fname=fname, lname=lname, email=email, phone=phone, age=age)
            ins.save()
            message="Data saved successfully"
            print("Data saved Successfully")
    return render(request, 'BioInsert.html', {'error': error, 'message': message})


def bio_search(request):
    error = []
    q=""
    if 'fname' in request.GET:
        q = request.GET['fname']
    if not q:
        error.append("Enter a search term ( It can not be empty) ")
    elif len(q) < 3:
        error.append(" length can not be lesser than 3")
    else:
        name = BioForm.objects.filter(fname=q).values()
        print("fname...", name)
        return render(request, 'BioSearch.html', {'names': name, 'query': q})

    return render(request, 'BioSearch.html', {'error': error})



