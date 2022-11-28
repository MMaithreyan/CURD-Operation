from django.shortcuts import render,redirect
from .models import studentdb
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def studentform(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        blood = request.POST.get('blood')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        address = request.POST.get('address')
        print(fullname)

        data = studentdb(fullname=fullname, blood=blood, email=email,
                         phone=phone, department=department, address=address)
        data.save()
        # data.clean()
        # return render(request, "list.html")
        # return redirect("list/")
           
    else:
        return render(request, "form.html")


def studentlist(request):
    # datalist = studentdb.objects.all()
    # return render(request, "list.html", {'data':datalist})

    mydata = studentdb.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))


def studentdelete(request, id):
    member = studentdb.objects.get(id=id)
    member.delete()
    return redirect('studentlist')

def studentupdate(request, id):
    mymember = studentdb.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    name = request.POST['name']
    blood = request.POST['blood']
    email = request.POST['email']
    phone = request.POST['phone']
    department = request.POST['department']
    address = request.POST['address']

    member = studentdb.objects.get(id=id)
    member.fullname = name
    member.blood = blood
    member.email = email
    member.phone = phone
    member.department = department
    member.address = address

    member.save()
    
    mydata = studentdb.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def adduser(request):
    return render(request,'form.html')