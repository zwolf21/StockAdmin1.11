import datetime

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from utils.shortcuts import sequence_date_slugify



class Buy(models.Model):
	slug = models.SlugField('구매서번호', unique=True, blank=True, editable=False)
	date = models.DateField('구매일자', default=datetime.date.today)
	commiter = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

	class Meta:
		verbose_name = '구매요청서'
		verbose_name_plural = '구매요청서'

	def __str__(self):
		return self.slug

	def save(self, **kwargs):
		if not self.slug:
			self.slug = sequence_date_slugify(self, 'date')
		return super(Buy, self).save(**kwargs)



class BuyItem(models.Model):
	buy = models.ForeignKey(Buy, blank=True, null=True)
	item = models.ForeignKey('profiles.BuyProfile')
	amount = models.IntegerField('수량')
	update = models.DateTimeField(auto_now=True)
	create = models.DateTimeField(auto_now_add=True)

	
	class Meta:
		verbose_name = '구매품목'
		verbose_name_plural = '구매품목'

	def __str__(self):
		return str(self.item)

	def clean(self):
		if self.buy:
			if self.buy.buyitem_set.filter(item=self.item).exists():
				raise ValidationError('이미 구매요청서에 항목이 있습니다')




