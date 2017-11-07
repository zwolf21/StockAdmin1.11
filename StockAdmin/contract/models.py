import datetime

from django.db import models
from django.conf import settings

from utils.shortcuts import sequence_date_slugify



# class Contract(models.Model):
# 	slug = models.SlugField('계약번호', unique=True, blank=True, editable=False)
# 	market = models.ForeignKey('product.Market')
# 	start_date = models.DateField('계약시작일', blank=True, null=True, default=datetime.date.today)
# 	end_date = models.DateField('계약종료일', blank=True, null=True, default=datetime.date(2999, 12, 31))
# 	commiter = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)


# 	class Meta:
# 		verbose_name = '구매계약서'
# 		verbose_name_plural = '구매계약서'

# 	def __str__(self):
# 		return self.slug



# class ContractItem(models.Model):
# 	contract = models.ForeignKey(Contract)
# 	buy_profile = models.ForeignKey('Profiles.BuyProfile')


# 	class Meta:
# 		verbose_name = '계약품목'
# 		verbose_name_plural = '계약품목'


# 	def __str__(self):
# 		return str(self.buy_profile)