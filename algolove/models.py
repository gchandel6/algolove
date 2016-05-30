from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pygments import lexers, formatters, highlight
from tagging.fields import TagField
from markdown import markdown
from datetime import datetime,date

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

	@models.permalink
	def get_absolute_url(self):
		return ('language_detail',(),{ 'slug' : self.slug })

	def get_lexer(self):
		return lexers.get_lexer_by_name(self.language_code)



class Algo_snippet(models.Model):
	title=models.CharField(max_length=300)
	language=models.ForeignKey(Language)
	author=models.ForeignKey(User)
	description=models.TextField()
	description_html=models.TextField(editable=False)
	code=models.TextField()
	highlighted_code=models.TextField(editable=False)
	pub_date=models.DateField(editable=False)
	updated_date=models.DateField(editable=False)
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
			self.pub_date = date.today()
		self.updated_date = date.today()
		self.description_html = markdown(self.description)
		self.highlighted_code = self.highlight()
		super(Algo_snippet, self).save()

	@models.permalink
	def get_absolute_url(self):
		return ('algo_snippet_detail',(),{ 'algo_snippet_id' : self.id })	


class Coding_snippet(models.Model):
	prob_name=models.CharField(max_length=30)
	judge_name=models.CharField(max_length=30)
	tech=models.CharField(max_length=50)
	language=models.ForeignKey(Language)
	author=models.ForeignKey(User)
	description=models.TextField()
	description_html=models.TextField(editable=False)
	code=models.TextField()
	highlighted_code=models.TextField(editable=False)
	pub_date=models.DateField(editable=False)
	updated_date=models.DateField(editable=False)
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
			self.pub_date = date.today()
		self.updated_date = date.today()
		self.description_html = markdown(self.description)
		self.highlighted_code = self.highlight()
		super(Coding_snippet, self).save()

	@models.permalink
	def get_absolute_url(self):
		return ('coding_snippet_detail',(),{ 'coding_snippet_id' : self.id })



		

	
