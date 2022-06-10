from pickle import DICT
from django.shortcuts import redirect, render

from django.contrib import messages

from . import models
# Create your views here.




def index(request):
    
    # if request.method =='POST':
    #     postedData = request.POST
    #     name = postedData.get('name',None)
    #     english_qualification = postedData.get('english_qualification',None)
    #     country = postedData.get('country',None)

    #     cv = models.CvData.objects.create(
    #         name = name,
    #         english_qualification=english_qualification,
    #         country = country
    #     )
    #     cv.save()
    #     messages.success(request, 'Thanks for your intrest we would get back to you soon!!')
    #     return render(request,'index.html')

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

    return render(request,'index.html')


def privacy(request):

    return render(request,'privacy.html')

def survey(request):
    context  =dict()
    closeSurvey = models.closeSurvey.objects.first()
    if closeSurvey.isOpen ==False:
        messages.success(request, 'Assessment Closed')
    
        return redirect('indexView')
    if request.method == 'POST':
        POST = dict(request.POST)
        email = POST['email'][0]
        discordID = POST['discordID'][0]
        if models.Survey.objects.all().filter(email=email,).exists():
            messages.success(request, 'You already took this test')
            return render(request,'survey.html',
            {'quetions':models.Quetions.objects.values()}
            )
        quetions = models.Quetions.objects.all()
        for q in quetions:
            answer = POST.get(q.name)[0]
            models.Survey.objects.create(
                email=email,
                discordID=discordID,
                quetion=q.name,
                anser=answer
            )
    

        # print(dict(request.POST)['email']) 

        messages.success(request, 'Thank You We would get back to you through your email')

    return render(request,'survey.html',
    {'quetions':models.Quetions.objects.values()}
    )