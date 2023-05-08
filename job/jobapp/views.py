from django.shortcuts import render,HttpResponse,redirect
from .models import jobModel


# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")



def index2(request):
    username="Topper"
    email="topper4445@gmail.com"
    contact="12345"
    educational_details="MCA"
    work_experience=0
    resume=0
    print(username,email,work_experience,contact)
    return render(request,'index2.html',
                  {'username':username,'email':email,'contact':contact,'educational_details':educational_details,'work_experience':work_experience})

# def update(request):
#     id = request.GET["id"]
#     job = jobModel.objects.get(id=id)
#     if request.POST:
#         name = request.POST["name"]
#         email = request.POST["email"]

#         contact = request.POST["contact"]
#         details = request.POST["details"]
#         experience = request.POST["experience"]
#         # resume = request.POST["resume"]
#         job.name = name
#         job.email = email
#         job.contact = contact
#         job.details = details
#         job.experience = experience
#         # job.resume = resume
#         job.save()

#     return render(request, 'edit.html', {'jobs': job})
def create(request):

    name=''
    email = ''
    contact= ''
    details = ''
    experience = ''
    resume = ''
    submit = 0

    if request.GET:
        name = request.GET["name"]
        email = request.GET["email"]
        contact = request.GET["contact"]
        details = request.GET["details"]
        experience = request.GET["experience"]
        resume = request.GET["resume"]

        p = jobModel()
        p.name = name
        p.email = email
        p.contact = contact
        p.details = details
        p.experience = experience
        p.resume = resume

        p.save()
        print("saved")
        submit= name

    return render(request, "sign.html",
                  {"name": name, "email": email, "contact": contact,"details":details,'experience':experience,'resume':resume,
                   "submit": submit})
    # return  render(request,'sign.html',{'message':"saved"})



def read(request):
    job= jobModel.objects.all()
    return render(request, "read.html", {'jobs':job })

def delete(request):
    if request.GET:
        id = request.GET["id"]
        job = jobModel.objects.filter(id=id)
        job.delete()
    return render(request, "delete.html", {"jobs": job})

def view(request):
    job = jobModel.objects.filter(id=id)
    return render(request,'view.html',
                  {'jobs':job})

def edit(request):
    id=request.GET['id']
    job=jobModel.objects.get(id=id)
    print(job)


    return render(request,'edit.html',{'jobs':job})



def update(request):
    id = request.GET["id"]
    job = jobModel.objects.get(id=id)
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]

        contact = request.POST["contact"]
        details = request.POST["details"]
        experience = request.POST["experience"]
        # resume = request.POST["resume"]
        job.name = name
        job.email = email
        job.contact = contact
        job.details = details
        job.experience = experience
        # job.resume = resume
        job.save()

    return render(request, 'edit.html', {'jobs': job})
