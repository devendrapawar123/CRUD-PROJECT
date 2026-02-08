from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageViews(request):
    return render(request,"app/insert.html")

def InsertData(requst):
    fname = requst.POST['fname']
    lname = requst.POST['lname']
    email = requst.POST['email']
    contact = requst.POST['contact']
    
# creating object of model class 
# Inserting Data into Table 
    
    newuser = Student.objects.create(Firstname=fname, Lastname=lname
                                     , Email=email, Contact=contact)
    
# After Insert render on show.html
    
    return redirect('showpage')

#show page view
def Showpage(request):
    # select * from tablename 
    # For fetching all the data of the table 
    all_data = Student.objects.all() 
    return render(request,"app/show.html",{'key1':all_data})
# Edit page view
def Editpage(request,pk):
    #Fetching the data of particular id 
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html" , {'key2': get_data})

# Update data views
def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    
# Query for update
    udata.save()
    # Render to show page
    return redirect('showpage')

# Delete Data view
def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    
    # Query for Delete
    ddata.delete()
    return redirect('showpage')