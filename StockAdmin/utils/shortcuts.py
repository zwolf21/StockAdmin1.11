from mimetypes import guess_type
from urllib.parse import quote

from django.utils.text import slugify
from django.http import HttpResponse


# 파일 리스폰스, 한글로 파일 이름 지정 가능
def file_response(content, filename):
	ctype, encoding = guess_type(filename)
	response = HttpResponse(content, content_type=ctype or 'applicatioin/octet-stream')
	if encoding:
		response['Content-Encoding'] = encoding
	response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(quote(filename.encode('utf-8')))
	return response


def unique_slugify(instance, field_to_slugify, slug_field_name='slug', post_fix_init=1, **kwargs):
	model = instance.__class__
	counter = post_fix_init
	value_to_slugify = getattr(instance, field_to_slugify)
	slug = slugify(value_to_slugify, **kwargs)
	ret = slug
	while True:
		if model.objects.filter(**{slug_field_name: ret}).exists():
			ret = "{}-{}".format(slug, counter)
			counter +=1 			
		else:
			return ret

# 20171011-002 형식으로 슬러그화
def sequence_date_slugify(instance, datefield_to_slugify, num_digit=3):
	model = instance.__class__
	date = getattr(instance, datefield_to_slugify)
	str_date = date.strftime("%Y%m%d")
	format_string = "{}-" + "{:0" + str(num_digit) + "d}"
	seq = 1
	while True:
		slug = format_string.format(str_date, seq)
		if model.objects.filter(slug=slug).exists():
			seq +=1
			continue
		return slug