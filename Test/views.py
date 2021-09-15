from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from Test.models import profile, banerImage, portfolio_image
from portfolio_Mz.settings import EMAIL_HOST_USER


def index(request):
    profiles = profile.objects.all()
    banerImages = banerImage.objects.all()
    portfolio_images = portfolio_image.objects.all()

    return render(request,'index.html',{'profiles':profiles,'banerImages':banerImages,'portfolio_images':portfolio_images})


def send_email(request):
    print('working')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        number = request.POST['number']
        if name and email and subject and number:
            print(name, subject, email)
            print('email')
            email = send_mail(' from :{}'.format(email), 'Hey, it\'s {}. Phone Number: {} '.format(name, number) + subject,
                              EMAIL_HOST_USER, ['MijanHawlader746@gmail.com', ], fail_silently=False)
            print(email)

            return render(request, 'index.html')

        else:
            return render(request, 'index.html')