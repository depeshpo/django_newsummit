from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request,
                  "home.html")


def list_all_students(request):
    from .models import Student
    from django.shortcuts import redirect
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        roll_no = request.POST['roll_no']
        bio = request.POST['bio']
        obj = Student()
        obj.name = name
        obj.email = email
        obj.roll_no = roll_no
        obj.bio = bio
        obj.save()
        return redirect('/')
    else:
        students = Student.objects.all()
        context = {
            "stds": students
        }
        return render(request,
                      "list.html",
                      context=context)
