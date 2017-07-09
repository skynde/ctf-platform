from django.contrib import admin
from django.conf.urls import url
from .models import User, Affiliate, SubmittedHistory

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'affiliate', 'is_active', 'is_staff', 'is_superuser')
    fields = ["username", "userID", "affiliate", "score", "solvedProblems", "noHintSolvedProblems", "hintedProblems", "availableProblems"]

class SubmittedHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', "problem", "isCorrect", "submitDatetime")

admin.site.register(User, UserAdmin)
admin.site.register(Affiliate)
admin.site.register(SubmittedHistory, SubmittedHistoryAdmin)
