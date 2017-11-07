import datetime, copy

from django.db import models


class Market(models.Model):
	name = models.CharField('도매상명', unique=True, max_length=50)
	tel = models.CharField('전화', max_length=30, blank=True, null=True)
	fax = models.CharField('팩스', max_length=30, blank=True, null=True)
	start_date = models.DateField('거래개시일', blank=True, null=True, default=datetime.date.today)
	end_date = models.DateField('거래종료일', blank=True, null=True, default=datetime.date(2999, 12, 31))
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '도매상'
		verbose_name_plural = '도매상'

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField('제품명', max_length=50)
	code = models.CharField('제품코드', unique=True, max_length=50)
	std_price = models.DecimalField('표준가격', max_digits=100, decimal_places=2)
	markets = models.ManyToManyField(Market, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '제품'
		verbose_name_plural = '제품'

	def __str__(self):
		markets = ', '.join(n.name for n in self.markets.all())
		return "{}-{}".format(self.name, markets)





