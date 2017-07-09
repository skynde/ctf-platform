from django.shortcuts import render
from accounts.models import User, SubmittedHistory
from django.http.response import JsonResponse
from accounts.models import Affiliate

def statistics(request):
    topUsers = User.objects.filter(is_superuser__exact=False).order_by("-score", "lastSubmitDatetime")[:5]
    history = SubmittedHistory.objects.filter(isCorrect__exact=True).order_by("-submitDatetime")[:10]
    return render(request,"scoreboard/statistics.html",
                  {"topUsers": topUsers, 
                   "history": history}
              )

def allUsers(request):
    allUsers = User.objects.filter(is_superuser__exact=False).order_by("-score", "lastSubmitDatetime")
    history = SubmittedHistory.objects.filter(isCorrect__exact=True).order_by("-submitDatetime")[:10]
    return render(request,"scoreboard/allUsers.html",
                  {"allUsers": allUsers, 
                   "history": history}
              )

def graphData(request):
    labels = []
    datum = {}
    datum["fillColor"]   = "rgba(151,187,205,0.5)"
    datum["strokeColor"] = "rgba(151,187,205,1)"
    datum["data"] = []
    for affiliate in Affiliate.objects.all().order_by("name"):
        labels += [affiliate.name]
        datum["data"] += [affiliate.score]
        datasets = [datum]
    return JsonResponse({"labels": labels, "datasets": datasets})
