from django.core.exceptions import ValidationError


class BuyProfileMixin(object):

	def save(self, **kwargs):
		if not self.id:
			previous = self.product.buyprofile_set.all()

			if not self.buy_price:
				self.buy_price = self.product.std_price
			
			if previous.exists():
				if not self.box_amount or self.box_amount == 1:
					self.box_amount = previous.last().box_amount
				if not self.buy_unit:
					self.buy_unit = previous.last().buy_unit
				if not self.buybox:
					self.buybox = previous.last().buybox

			if self.active == True:
				self.product.buyprofile_set.filter(market=self.market).update(active=False)

		else:
			if self.active == True:
				self.product.buyprofile_set.filter(market=self.market).exclude(id=self.id).update(active=False)	

		return super(BuyProfileMixin, self).save(**kwargs)


	def clean(self):
		if self.market not in self.product.markets.all():
			markets = ', '.join(n.name for n in self.product.markets.all())
			error_message='도매상 {}이 해당 제품의 거래 가능 도매상 목록에 존재 하지 않습니다.'.format(self.market)
			if markets:
				error_message+=' 선택가능한 도매상: {}'.format(markets)
			else:
				error_message+=' 제품정보로가서 거래 할 도매상을 한개이상 등록하십시오'
			raise ValidationError(error_message)