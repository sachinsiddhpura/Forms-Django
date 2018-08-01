from django.db import models
from django.db.models import permalink
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models heRE
from django.dispatch import receiver
from django.db.models.signals import post_save
'''
QUESTION_CHOICES = (
    ("vada_paw", "Vada Paw"),
    ("paw_bhaji", "Paw Bhaji"),
    ("ghughra", "Ghughra"),
    ("pani_puri", "Pani Puri"),
    ("dal_pakwan", "Dal Pakwan"),
    ("fruit_salad", "Fruit Salad"),
    ("sandwhich", "Sandwhich"),
    ("bhajiya", "Bhajiya"),
    ("punjabi", "Punjabi"),
    ("pizza", "Pizza"),
    ("dabeli", "Dabeli"),
    ("manchurian", "Manchurian"),
)

class Profile(models.Model):

	users = models.ManyToManyField(User)
	has_voted = models.BooleanField(default=False)

	def __str__(self):
	    return str(self.user)


	@receiver(post_save, sender=User)
	def ensure_profile_exists(sender, **kwargs):
		if kwargs.get('created', False):
	   		Profile.objects.get_or_create(user=kwargs.get('instance'))


class Choice(models.Model):
	user = models.ForeignKey(User)
	#users = models.ManyToManyField(User)
	choices = models.CharField(
	    max_length=256, choices=QUESTION_CHOICES, unique=True)
	vote = models.IntegerField(default=0)

	def __str__(self):
	    return self.choices + " " + "-" + " " + str(self.vote)'''

class PersonType(models.Model):
	title	=models.CharField(max_length=240)
	slug	=models.SlugField(unique=True, blank=True)

	class Meta:
		verbose_name=('person type')
		verbose_name_plural=('person types')
		db_table='person_general'
		ordering=('title',)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
	    return reverse('person_genre_detail', None, { 'slug': self.slug})

class Person(models.Model):
	GENDER_CHOICES = (
	    (1, 'Male'),
	    (2, 'Female'),
	    (3, 'Other'),
	)
	SEM_CHOICES=(
		(1,'1'),
		(3,'3'),
		(5,'5'),
		(7,'7'),
		)
	YEARS=[x for x in range(2008,2020)]
	first_name = models.CharField(_('first name'), blank=True, max_length=100)
	middle_name = models.CharField(_('middle name'), blank=True, max_length=100)
	last_name = models.CharField(_('last name'), blank=True, max_length=100)
	#slug = models.SlugField(_('slug'), unique=True)
	enrollment_no=models.CharField(max_length=465,default="160130107091")
	sem	=models.IntegerField(default="5", choices=SEM_CHOICES)
	user = models.ForeignKey(User, blank=True, null=True, help_text='If the person is an existing user of your site.')
	gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
	birth_date = models.DateField(_('birth date'),default='1999-08-28')
	person_types = models.ManyToManyField(PersonType, blank=True)
	website = models.URLField(_('website'), blank=True)


	class Meta:
	    verbose_name = _('person')
	    verbose_name_plural = _('people')
	    db_table = 'people'
	    ordering = ('last_name', 'first_name',)

	def __str__(self):
		return self.first_name

	@property
	def full_name(self):
	    return u'%s %s' % (self.first_name, self.last_name)

	@permalink
	def get_absolute_url(self):
	    return ('person_detail', None, {'slug': self.slug})