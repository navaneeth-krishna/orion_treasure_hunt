from django.shortcuts import render
from accounts.models import UserProgress
import datetime

# Create your views here.
def leaderboard(request):
    lead = UserProgress.objects.all().order_by('-clueReached').exclude(clueReached=16)[:10]
    now = datetime.datetime.now()
    check_date = datetime.datetime(2020,6,21,11,00,0)

    show_dash = False

    if (now >= check_date) :
        show_dash=True

    return render(request,'leaderboard.html',{'leads':lead,'show':show_dash})