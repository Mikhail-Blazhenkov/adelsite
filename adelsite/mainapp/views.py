from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')
def woman(request):
    return render(request, 'mainapp/woman.html')

def man(request):
    return render(request, 'mainapp/man.html')

def become(request):
    return render(request, 'mainapp/become.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def school(request):
    return render(request, 'mainapp/school.html')
