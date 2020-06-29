from django.shortcuts import render,redirect,reverse
from .models import Job
from django.core.paginator import Paginator
from .form import Applyform, addform
# Create your views here.


def job_list(request):
    job_list=Job.objects.all()

    paginator = Paginator(job_list, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'job_list': page_obj,

    }
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job=job
            myform.save()
    else:
        form = Applyform()

    context = {
        'job':job,
        'form':form,
    }
    return render(request,'job/job_detail.html',context)


def add_job(request):
    if request.method=='POST':
        form=addform(request.POST,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form=addform()
    context = {
    'form':form
    }
    return render(request,'job/add_job.html',context)
