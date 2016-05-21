
from django.conf.urls import url
from django.views.generic.list import ListView
from algolove.models import Language
from algolove.views.languages import language_detail

lang_query= Language.objects.all()


urlpatterns = [

	url(r'^$',
		ListView.as_view(queryset=lang_query,
							paginate_by=20),
							name="all_lang"
		),

	url(r'^(?P<slug>[-\w]+)/$' ,
						language_detail,
						name="language_detail"
		),

	
]							
