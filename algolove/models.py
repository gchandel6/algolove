from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pygments import lexers, formatters, highlight
from tagging.fields import TagField
from markdown import markdown
import datetime

# Create your models here.

class Language(models.Model):
	name=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	language_code=models.CharField(max_length=50)
	mime_type=models.CharField(max_length=100)


	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name;

	def get_absolute_url(self):
		return ('cab_language_detail',(),{ 'self' : self.slug })

	def get_lexer(self):
		return lexers.get_lexer_by_name(self.language_code)



class Snippet(models.Model):
	title=models.CharField(max_length=300)
	language=models.ForeignKey(Language)
	author=models.ForeignKey(User)
	description=models.TextField()
	description_html=models.TextField(editable=False)
	code=models.TextField()
	highlighted_code=models.TextField(editable=False)
	pub_date=models.DateTimeField(editable=False)
	updated_date=models.DateTimeField(editable=False)
#	tags=TagField()

	class Meta:
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def highlight(self):
		return highlight(self.code,
							self.language.get_lexer(),
							formatters.HtmlFormatter(linenos=True))

	def save(self):
		if not self.id:
			self.pub_date = datetime.datetime.now()
		self.updated_date = datetime.datetime.now()
		self.description_html = markdown(self.description)
		self.highlighted_code = self.highlight()
		super(Snippet, self).save()





		

	
