from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Responder)
admin.site.register(PrimaryQuestionBase)
admin.site.register(PrimaryQuestionAnswer)
admin.site.register(SubquestionBase)
admin.site.register(SubquestionPredefinedAnswer)
admin.site.register(SubquestionAnswer)
