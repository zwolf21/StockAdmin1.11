from django.db import models


class BuyProfileQuerySet(models.query.QuerySet):

	def active(self):
		return self.filter(active=True)

	def inactive(self):
		return self.exclude(active=True)


class BuyProfileManager(models.Manager):

	def get_queryset(self):
		return BuyProfileQuerySet(self.model, using=self._db)

	def active(self):
		return self.get_queryset().active()