from django.shortcuts import render

def login(request):
    print(request)
    data = {
        "name":"Rahul",
        "age":20
    }
    return render(request,"login.html",{'data':data})
  
def add(request):
    val1 = int(request.GET['number1'])
    val2 = int(request.GET['number2'])
    result = val1 + val2
    return render(request,"result.html",{'result':result})
  