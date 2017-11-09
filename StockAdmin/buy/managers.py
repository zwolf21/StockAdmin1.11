from django.db import models



class BuyManager(models.Manager):

	def get_or_create_cart(self, cart_name):
		cart, created = self.get_or_create(buy_num=cart_name)
		return cart