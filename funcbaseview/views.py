from django.shortcuts import render

from funcbaseview.models import Employee,Address


def welcome_page_emp(req):
    return render(request=req,template_name='employee.html',context={
        'emplist':Employee.objects.all(),
         'emp':Employee.get_dummy_emp(),
        'adrlist': Address.objects.all()
    })


def add_update_emp(req):
    msg=''
    if req.method=='POST':
        data=req.POST
        eid=data.get('id')
        adrs = data.getlist('adr')
        dbemp=Employee.objects.filter(id=eid).first()
        emp=Employee(name=data.get('name'),age=data.get('age'),email=data.get('email'),salary=data.get('salary'))
        # adr = Address.objects.filter(id=int(data.get('adr'))).first()
        if dbemp:
            dbemp.name=emp.name
            dbemp.age=emp.age
            dbemp.email=emp.email
            dbemp.salary=emp.salary
            if adrs:
                adrlist = []
                for adr in adrs:
                    adrlist.append(Address.objects.filter(id=int(adr)).first())

            dbemp.save()
            dbemp.adrref.add(*adrlist)
            msg="Employee updated succesfully..!"
        else:
            adrlist = []
            if adrs:
                for adr in adrs:
                    adrlist.append(Address.objects.filter(id=int(adr)).first())
            emp.save()
            emp.adrref.add(*adrlist)

            msg='Employee added succesfully'
    return render(request=req, template_name='employee.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_emp(),
        'message':msg,
        'adrlist': Address.objects.all()
    })

def edit_emp(req,eid):
    return render(request=req, template_name='employee.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.objects.filter(id=eid).first(),
        'adrlist': Address.objects.all()
    })

def delete_emp(req,eid):
    demp=Employee.objects.filter(id=eid).first()
    msg= ''
    if demp:
        demp.delete()
        msg="Employee Deleted Succesfully..!"
    return render(request=req, template_name='employee.html', context={
        'emplist': Employee.objects.all(),
        'emp': Employee.get_dummy_emp(),
        "message":msg,
        'adrlist': Address.objects.all()
    })




def welcome_page_adr(req):
    return render(request=req,template_name='address.html',context={
        'adrlist':Address.objects.all(),
         'adr':Address.get_dummy_adr(),
        'emplist':Employee.objects.all()
    })


def add_update_adr(req):
    msg=''
    if req.method=='POST':
        data=req.POST
        aid=data.get('id')
        dbadr=Address.objects.filter(id=aid).first()
        adr=Address(city=data.get('city'),state=data.get('state'),pincode=data.get('pincode'))
        if dbadr:
            dbadr.city=adr.city
            dbadr.state=adr.state
            dbadr.pincode=adr.pincode
            dbadr.save()
            msg="Address updated succesfully..!"
        else:
            adr.save()
            msg='Address added succesfully'
    return render(request=req, template_name='address.html', context={
        'emplist': Employee.objects.all(),
        'adrlist': Address.objects.all(),
        'adr': Address.get_dummy_adr(),
        'message':msg
    })

def edit_adr(req,aid):
    return render(request=req, template_name='address.html', context={
        'emplist': Employee.objects.all(),
        'adrlist': Address.objects.all(),
        'adr':Address.objects.filter(id=aid).first()
    })

def delete_adr(req,aid):
    dadr=Address.objects.filter(id=aid).first()
    msg= ''
    if dadr:
        dadr.delete()
        msg="Address Deleted Succesfully..!"
    return render(request=req, template_name='address.html', context={
        'adrlist': Address.objects.all(),
        'emplist': Employee.objects.all(),
        'adr': Address.get_dummy_adr(),
        "message":msg
    })