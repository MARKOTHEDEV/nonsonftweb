from django.shortcuts import render

from django.contrib import messages

from . import models
# Create your views here.




def index(request):
    
    if request.method =='POST':
        postedData = request.POST
        name = postedData.get('name',None)
        english_qualification = postedData.get('english_qualification',None)
        country = postedData.get('country',None)

        cv = models.CvData.objects.create(
            name = name,
            english_qualification=english_qualification,
            country = country
        )
        cv.save()
        messages.success(request, 'Thanks for your intrest we would get back to you soon!!')

    return render(request,'index.html')
def contact(request):
        
    if request.method =='POST':
        postedData = request.POST
        name = postedData.get('your-name',None)
        email = postedData.get('your-email',None)
        message = postedData.get('your-message',None)


        contact= models.ContactUs.objects.create(
            name = name,
            email=email,
            message = message
        )
        contact.save()
        messages.success(request, 'Thanks for reaching! out  we would get back to you soon!!')
   
    return render(request,'contact.html')



def privacy(request):

    return render(request,'privacy.html')