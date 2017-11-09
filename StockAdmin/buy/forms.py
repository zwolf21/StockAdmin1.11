from django import forms
from django.forms import inlineformset_factory

from .models import Buy, BuyItem, BuyStock


class BuyItemForm(forms.ModelForm):

	class Meta:
		model = BuyItem
		fields = 'item', 'buy_amount', 'force_end',

	def __init__(self, *args, **kwargs):
	    super(BuyItemForm, self).__init__(*args, **kwargs)
	    BuyProfile = self.fields['item'].queryset.model
	    self.fields['item'].queryset = BuyProfile.objects.active()

	def clean_buy_amount(self):
		buy_amount = self.cleaned_data['buy_amount']
		if buy_amount <1:
			raise forms.ValidationError('1 이상의 값이 필요합니다.')
			pass
		return buy_amount


BuyItemFormSet = inlineformset_factory(Buy, BuyItem, BuyItemForm,
	fields=['item', 'buy_amount', 'force_end'],
	max_num=1000, extra=1
)



