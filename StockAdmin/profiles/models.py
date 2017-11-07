from django.db import models

from .managers import BuyProfileManager

from .mixins import BuyProfileMixin



class BuyProfile(BuyProfileMixin, models.Model):
	product = models.ForeignKey('product.Product')
	market = models.ForeignKey('product.Market', null=True)
	buy_price = models.DecimalField('구매가격', max_digits=100, decimal_places=2)
	box_amount = models.IntegerField('묶음수량', null=True, default=1)
	buy_unit = models.CharField('묶음단위', choices=[('BOX', 'BOX'), ('PKG', 'PKG')], blank=True, null=True, max_length=10)
	buybox = models.BooleanField('묶음단위구매', default=False)
	active = models.BooleanField('사용중', default=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	objects = BuyProfileManager()

	class Meta:
		verbose_name = '구매정보'
		verbose_name_plural = '구매정보'

	def __str__(self):
		std_unit = self.product.stockprofile.std_unit
		if self.buybox:
			box_total = self.product.stockprofile.pkg_amount * self.box_amount
			buy_amount_unit = "({}{}/{})".format(box_total, std_unit, self.buy_unit)
		else:
			pkg_total = self.product.stockprofile.pkg_amount
			buy_amount_unit = "({}{})".format(pkg_total, std_unit)
		return "{}{}-{}{}원".format(self.product.name, buy_amount_unit, self.market, self.buy_price)

	


STD_UNITs = 'AMP', 'VIAL', 'PEN','TAB', 'BTL', '포',

class StockProfile(models.Model):
	product = models.OneToOneField('product.Product')
	pkg_amount = models.IntegerField('포장수량')
	std_unit = models.CharField('기본단위', choices=zip(STD_UNITs, STD_UNITs), default='TAB', max_length=10)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = '재고정보'
		verbose_name_plural = '재고정보'

	def __str__(self):
		return self.product.name


