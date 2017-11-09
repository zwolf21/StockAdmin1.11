from django.shortcuts import render
from django.views.generic import *

from .models import Buy, BuyItem, BuyStock
from .forms import BuyItemForm, BuyItemFormSet


CART_NAME = 'cart'

class BuyUpdateView(UpdateView):
    model = Buy
    fields = 'buy_date',
    success_url = '.'

    def get_object(self):
        buy_num = self.kwargs.get('buy_num')
        if buy_num == CART_NAME:
            return Buy.objects.get_or_create_cart(buy_num)
        return super(BuyUpdateView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(BuyUpdateView, self).get_context_data(**kwargs)
        context['formset'] = BuyItemFormSet(self.request.POST or None, instance=self.get_object())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            formset.save()
        else:
            ## TAGS: formset에 에러가 있을 시 에러를 렌더링 해줌
            return self.render_to_response(self.get_context_data(form=form))
        return super(BuyUpdateView, self).form_valid(form)




