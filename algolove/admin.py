from django.contrib import admin
from .models import Language , Algo_snippet , Coding_snippet

# Register your models here.

admin.site.register(Language)
admin.site.register(Algo_snippet)
admin.site.register(Coding_snippet)
