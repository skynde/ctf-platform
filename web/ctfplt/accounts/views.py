from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User
from accounts.models import SubmittedHistory

@login_required(login_url="/accounts/login/")
def profile(request):
    topUsers = User.objects.filter(is_superuser__exact=False).order_by("-score", "lastSubmitDatetime")
    idx = 1
    for user in topUsers:
        if user.username == request.user.username:
            break
        idx += 1
    maxSize = User.objects.filter(is_superuser__exact=False).count()
    fromIdx = 0 if idx-3 < 0 else idx-3
    toIdx   =  maxSize if idx+3 > maxSize else idx+3
    aroundUsers = topUsers[fromIdx:toIdx]
    history = SubmittedHistory.objects.filter(user__exact=request.user).order_by("-submitDatetime")[:5]
    return render(request,"accounts/profile.html", 
                  {'user' : request.user,
                   'baseIdx': fromIdx, 
                   'idx': idx,
                   'aroundUsers': aroundUsers,
                   'history': history
               }
              )

@login_required(login_url="/accounts/login/")
def update(request):
    #newUserID = request.POST['userID']
    newUsername = request.POST['userName']
    #newAffiliate = request.POST['affiliate']
    newEmail = request.POST['email']
    newPW = request.POST['newPW']
    confirmPW = request.POST['confirmPW']
    currentPW = request.POST['currentPW']
    #return render(request, 'accounts/error.html')

    changePWFlag = True
    if newPW == "" or (newPW != confirmPW):
        changePWFlag = False
    if request.user.check_password(currentPW) and changePWFlag:
        request.user.username = newUsername
        if newPW != "":
            request.user.set_password(newPW)
        request.user.save()
        return HttpResponseRedirect(reverse('accounts:index'))
    else:
        return render(request,"accounts/profile.html", 
                      {'user' : request.user, 
                       "errorStr": "Update Failed. Please try again.",
                   }
                  )

