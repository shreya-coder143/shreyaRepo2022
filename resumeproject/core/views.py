from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def index(request):
    return render(request, 'core/index.html')


def contact_us(request):
    context={}
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        obj=Contact(name=name,email=email,subject=subject,message=message)
        obj.save()
        context['message']=f"Dear {name},Thnks for your time!"
        # return HttpResponse("dear {} Thanks for regisetring")

    return render(request,'index.html',context)
