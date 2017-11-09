import datetime

from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from .managers import BuyManager

from utils.shortcuts import sequence_date_slugify



class Buy(models.Model):
    buy_num = models.SlugField('구매서번호', unique=True, blank=True, editable=False)
    buy_date = models.DateField('구매일자', default=datetime.date.today)
    commiter = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    objects = BuyManager()

    class Meta:
        verbose_name = '구매요청서'
        verbose_name_plural = '구매요청서'

    def __str__(self):
        return self.buy_num

    def save(self, **kwargs):
        if not self.buy_num:
            self.buy_num = sequence_date_slugify(self, 'date')
        return super(Buy, self).save(**kwargs)



class BuyItem(models.Model):
    buy = models.ForeignKey(Buy, blank=True, null=True)
    item = models.ForeignKey('profiles.BuyProfile')
    buy_amount = models.IntegerField('수량', validators=[MinValueValidator(1, '1 이상의 값을 입력 해야합니다')])

    stocked_amount = models.IntegerField('입고수량', default=0, blank=True, null=True, editable=False)
    incompleted_amount = models.IntegerField('미입고수량', blank=True, null=True, editable=False)
    completed = models.BooleanField('입고완료', default=False, editable=False)
    force_end = models.BooleanField('강제종결', default=False, blank=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = '구매품목'
        verbose_name_plural = '구매품목'

    def __str__(self):
        return str(self.item)

    def clean(self):
        if not self.id:
            if self.buy:
                if self.buy.buyitem_set.filter(item=self.item).exists():
                    raise ValidationError('이미 구매요청서에 항목이 있습니다')

    def save(self, **kwargs):
        self.calc_amounts(commit=False)
        return super(BuyItem, self).save(**kwargs)


    def calc_amounts(self, commit=True):
        agg_stock = self.buystock_set.aggregate(total_stock=Sum('stock_amount'))
        stocked = agg_stock['total_stock'] or 0
        self.stocked_amount = stocked
        self.incompleted_amount = self.buy_amount - stocked
        self.completed = (self.incompleted_amount == 0)
        if commit:
            self.save()
        return self




class BuyStock(models.Model):
    buyitem = models.ForeignKey(BuyItem)
    stock_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    stock_date = models.DateField('입고일자', default=datetime.date.today)
    stock_amount = models.IntegerField('입고수량')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '구매입고'
        verbose_name_plural = '구매입고'

    def __init__(self, *args, **kwargs):
        super(BuyStock, self).__init__(*args, **kwargs)
        self.stock_amount_old = self.stock_amount

    def __str__(self):
        return str(self.buyitem)

    def save(self, **kwargs):
        return super(BuyStock, self).save(**kwargs)

    def clean(self):
        if self.stock_amount < 1:
            raise ValidationError('최소 1 이상의 수량을 입력하여야 합니다')

        if self.id:
            result_amount = self.buyitem.stocked_amount - self.stock_amount_old + self.stock_amount
        else:
            result_amount = self.buyitem.stocked_amount + self.stock_amount

        if result_amount > self.buyitem.buy_amount:
            raise ValidationError('입고수량이 구매수량을 초과 합니다.')


@receiver(post_save, sender=BuyStock)
def buystock_post_save(sender, instance, created, *args, **kwargs):
    instance.buyitem.calc_amounts()


@receiver(post_delete, sender=BuyStock)
def buystock_post_delete(sender, instance, *args, **kwargs):
    instance.buyitem.calc_amounts()




    










