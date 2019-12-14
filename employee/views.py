from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee
from django.http import Http404  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  


# extra code
from django.http import HttpResponse
from employee.functions.functions import handle_uploaded_file

def setsession(request):  
   request.session['sname'] = 'akram'  
   request.session['semail'] = 'akram.sssit@gmail.com'  
   return HttpResponse("session is set")  
def getsession(request):  
   studentname = request.session['sname']  
   studentemail = request.session['semail']  
   return HttpResponse(studentname+" "+studentemail);  


def setcookie(request):  
   response = HttpResponse("Cookie Set")  
   response.set_cookie('java-tutorial', 'javatpoint.com')  
   return response  
def getcookie(request):  
   tutorial  = request.COOKIES['java-tutorial']  
   return HttpResponse("java tutorials @: "+  tutorial);  


# import csv  
# def getfile(request):  
#    response = HttpResponse(content_type='text/csv')  
#    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
#    writer = csv.writer(response)  
#    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
#    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
#    return response  


# import csv 
# from myapp.models import Employee
# def getfile(request):  
#    response = HttpResponse(content_type='text/csv')  
#    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
#    employees = Employee.objects.all()  
#    writer = csv.writer(response)  
#    for employee in employees:  
#       writer.writerow([employee.eid,employee.ename,employee.econtact])  
#    return response  

from reportlab.pdfgen import canvas  

def getpdf(request):  
   response = HttpResponse(content_type='application/pdf')  
   response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
   p = canvas.Canvas(response)  
   p.setFont("Times-Roman", 55)  
   p.drawString(100,700, "Hello, Javatpoint.")  
   p.showPage()  
   p.save()  
   return response


from crudexample import settings  
from django.core.mail import send_mail  

def mail(request):  
   subject = "Greetings"  
   msg     = "Congratulations for your success"  
   to      = "akramrp7@gmail.com"  
   res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
   if(res == 1):  
      msg = "Mail Sent Successfuly"  
   else:  
      msg = "Mail could not sent"  
   return HttpResponse(msg)  