from django.shortcuts import render
from .models import Clue
from accounts.models import WonUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
import datetime 
# Create your views here.

# CALLED ON LOGIN-------------------------------
def dashboard(request):
    
    now = datetime.datetime.now()
    check_date = datetime.datetime(2020,6,21,11,00,0)
    user = request.user

    if(user.userprogress.clueReached == 1):
        user.userprogress.updateclue()

    # if(user.userprogress.clueReached == 1 and not(user.userprogress.dead)):

    #     if( user.last_login < timezone.make_aware(check_date, timezone.get_default_timezone()) ):
    #         user.userprogress.cluedead = timezone.make_aware(check_date, timezone.get_default_timezone()) + datetime.timedelta(minutes = 3)
    #     else:
    #         if(user.userprogress.cluedead > user.last_login + datetime.timedelta(minutes = 3) ):
    #             user.userprogress.cluedead = user.last_login + datetime.timedelta(minutes = 3)
    #     user.userprogress.save()

    #     if user.userprogress.clue1solved is None :
    #         user.userprogress.updateclue()

    # if ((timezone.now() > user.userprogress.cluedead)and user.userprogress.clueReached<=15):
    #     user.userprogress.dead=True
    #     user.userprogress.save()
    #     return render(request,'end.html')

    show_dash = False

    if (now >= check_date) :
        show_dash=True
    
    if(user.userprogress.clueReached<=15):
        clue = Clue.objects.get(clue_no=user.userprogress.clueReached)
        return render(request,'dashboard.html',{'clue':clue,'show':show_dash})

    else:
        user_won = WonUser.objects.get(username=user.username)
        return render(request,'win.html',{'won':user_won})
        







# FUNCTION TO CHECK ANSWER ---------------------------------------

def check(request):

    now = datetime.datetime.now()
    check_date = datetime.datetime(2020,6,21,11,00,0)
    user = request.user

    # if (timezone.now() > user.userprogress.cluedead):
    #     user.userprogress.dead=True
    #     user.userprogress.save()
    #     return render(request,'end.html')

    show_dash = False

    if (now >= check_date) :
        show_dash=True

    if(request.method=='POST'):
        ans = request.POST['answer']
        no_user = len(WonUser.objects.all())+1

# Checking if the user has won---------------------

        if(user.userprogress.clueReached == 16):
            user_won = WonUser(position=no_user,time_won=timezone.now(),first_name=user.first_name,last_name=user.last_name,username=user.username,email=user.email,clue1solved=user.userprogress.clue1solved,clue2solved=user.userprogress.clue2solved,clue3solved=user.userprogress.clue3solved,clue4solved=user.userprogress.clue4solved,clue5solved=user.userprogress.clue5solved,clue6solved=user.userprogress.clue6solved,clue7solved=user.userprogress.clue7solved,clue8solved=user.userprogress.clue8solved,clue9solved=user.userprogress.clue9solved,clue10solved=user.userprogress.clue10solved,clue11solved=user.userprogress.clue11solved,clue12solved=user.userprogress.clue12solved,clue13solved=user.userprogress.clue13solved,clue14solved=user.userprogress.clue14solved,clue15solved=user.userprogress.clue15solved)
            
            if(not(WonUser.objects.filter(username=user_won.username).exists())):
                user_won.save()
            won = WonUser.objects.get(username=user.username)
            return render(request,'win.html',{'user': user,'won':won})

        else:
            # if (timezone.now() > user.userprogress.cluedead):
            #     return render(request,'end.html')
            clue = Clue.objects.get(clue_no=user.userprogress.clueReached)
            if(clue.verify(ans)):
                user.userprogress.clueReached +=1
                if(user.userprogress.clueReached == 2 or user.userprogress.clueReached == 5 or user.userprogress.clueReached == 8 or user.userprogress.clueReached == 10 or user.userprogress.clueReached == 12):
                    user.userprogress.cluedead = datetime.datetime.now() + datetime.timedelta(minutes=5)
                else:
                    user.userprogress.cluedead = datetime.datetime.now() + datetime.timedelta(minutes=3)
                user.userprogress.updateclue()

# Checking if user has already won---------------------
                if(user.userprogress.clueReached == 16):
                    user_won = WonUser(position=no_user,time_won=timezone.now(),first_name=user.first_name,last_name=user.last_name,username=user.username,email=user.email,clue1solved=user.userprogress.clue1solved,clue2solved=user.userprogress.clue2solved,clue3solved=user.userprogress.clue3solved,clue4solved=user.userprogress.clue4solved,clue5solved=user.userprogress.clue5solved,clue6solved=user.userprogress.clue6solved,clue7solved=user.userprogress.clue7solved,clue8solved=user.userprogress.clue8solved,clue9solved=user.userprogress.clue9solved,clue10solved=user.userprogress.clue10solved,clue11solved=user.userprogress.clue11solved,clue12solved=user.userprogress.clue12solved,clue13solved=user.userprogress.clue13solved,clue14solved=user.userprogress.clue14solved,clue15solved=user.userprogress.clue15solved)
            
                    if(not(WonUser.objects.filter(username=user_won.username).exists())):
                        user_won.save()
                    won = WonUser.objects.get(username=user.username)
                    return render(request,'win.html',{'user': user,'won':won})

# If user is not won--------------------------

                clue=Clue.objects.get(clue_no=user.userprogress.clueReached)
                return render(request,'dashboard.html',{'clue':clue,'show':show_dash})
            else:
                
                messages.info(request,"Incorrect Answer! Try again!")
                return render(request,'dashboard.html',{'clue':clue,'show':show_dash})