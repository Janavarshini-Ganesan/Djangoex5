from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    if request.method == "POST":
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        response = render(request, 'myapp/cookie_created.html', {'username': username})
        response.set_cookie('username', username)
        response.set_cookie('mobile', mobile)
        return response
    return render(request, 'myapp/set_cookie.html')

def set_session(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        request.session['username'] = username
        request.session['email'] = email
        return render(request, 'myapp/session_created.html', {'username': username})
    return render(request, 'myapp/set_session.html')

def home(request):
    return render(request, 'myapp/home.html')