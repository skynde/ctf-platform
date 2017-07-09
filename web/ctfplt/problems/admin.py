from django.contrib import admin
from .models import Problem, Tag

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'listUnlockProblems')
    def listUnlockProblems(self, obj):
        return ", ".join([p.title for p in obj.unlockProblems.all()])

#admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(Problem, ProblemAdmin)
