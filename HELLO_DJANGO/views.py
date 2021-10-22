from django.http import HttpResponse
from django.shortcuts import render
from HELLO_DJANGO.dao_emp import DaoEmp
from django.http.response import JsonResponse


def index(request):
    return HttpResponse("Hello DJANGO", request)

def param1(request):
    a = request.GET['a']
    print('a',a)
    return HttpResponse("Hello[GET] " + a)

def param2(request):
    a = request.POST['a']
    print('a',a)
    return HttpResponse("Hello[POST] " + a)

def myforward(request):
    str = "1111"
    arr = [1,2,3,4] 
    data = {
        'id' : '1',
        'name' : '홍길동',
        'str' : str,
        'arr' : arr
    }
    
    return render(request,'myforward.html', data)

def emp_list(request):
    de = DaoEmp()
    list = de.myselect()
    data = {
        'list' : list
    }
    
    return render(request, 'emp_list.html', data)

def insert_ajax(request):
    de = DaoEmp()
    emp_id = request.POST['emp_id']
    emp_name = request.POST['emp_name']
    tel = request.POST['tel']
    address = request.POST['address']
    
    print("emp_id", emp_id)
    
    cnt = de.myinsert(emp_id, emp_name, tel, address)
    
    msg = "no"
    
    if cnt == 1:
        msg = "ok"

    myjson = {"msg" : msg}
        
    return JsonResponse(myjson)

def update_ajax(request):
    de = DaoEmp()
    emp_id = request.POST['emp_id']
    emp_name = request.POST['emp_name']
    tel = request.POST['tel']
    address = request.POST['address']
    
    cnt = de.myupdate(emp_id, emp_name, tel, address)
    
    msg = "no"
    
    if cnt == 1:
        msg = "ok"

    myjson = {"msg" : msg}
        
    return JsonResponse(myjson)

def delete_ajax(request):
    de = DaoEmp()
    emp_id = request.POST['emp_id']
    
    cnt = de.mydelete(emp_id)
    
    msg = "no"
    
    if cnt == 1:
        msg = "ok"
    
    myjson = {"msg" : msg}

    return JsonResponse(myjson)





