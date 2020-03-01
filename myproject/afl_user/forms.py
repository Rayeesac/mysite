from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Newsletter,Contact,Profile,Country,State
from django.forms import ModelForm
from collections import OrderedDict

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ('email',)

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('first_name','last_name','email','phoneno','msg')

class DateInput(forms.DateInput):
	input_type = 'date'

########### Print Function ###############

from django.conf import settings
import builtins
from pprint import pprint
def pp(*args):
	if settings.DEBUG:
		for arg in args:
			pprint(arg)
		pass
builtins.pp = pp 

from django.core.validators import RegexValidator

class ProfileForm(forms.ModelForm):
	uid = forms.IntegerField(widget=forms.HiddenInput())
	PHONE_REGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")
	phone_number = forms.CharField(max_length=15,validators=[PHONE_REGEX])
	POSTCODES_REGEX = {
		'AC': r'^[A-Z]{4}[0-9][A-Z]$',
		'AD': r'^AD[0-9]{3}$',
		'AF': r'^[0-9]{4}$',
		'AI': r'^AI-2640$',
		'AL': r'^[0-9]{4}$',
		'AM': r'^[0-9]{4}$',
		'AR': r'^([0-9]{4}|[A-Z][0-9]{4}[A-Z]{3})$',
		'AS': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
		'AT': r'^[0-9]{4}$',
		'AU': r'^[0-9]{4}$',
		'AX': r'^[0-9]{5}$',
		'AZ': r'^AZ[0-9]{4}$',
		'BA': r'^[0-9]{5}$',
		'BB': r'^BB[0-9]{5}$',
		'BD': r'^[0-9]{4}$',
		'BE': r'^[0-9]{4}$',
		'BG': r'^[0-9]{4}$','BH': r'^[0-9]{3,4}$',
		'BL': r'^[0-9]{5}$',
		'BM': r'^[A-Z]{2}([0-9]{2}|[A-Z]{2})',
		'BN': r'^[A-Z]{2}[0-9]{4}$',
		'BO': r'^[0-9]{4}$',
		'BR': r'^[0-9]{5}(-[0-9]{3})?$',
		'BT': r'^[0-9]{3}$',
		'BY': r'^[0-9]{6}$',
		'CA': r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$',
		'CC': r'^[0-9]{4}$',
		'CH': r'^[0-9]{4}$',
		'CL': r'^([0-9]{7}|[0-9]{3}-[0-9]{4})$',
		'CN': r'^[0-9]{6}$',
		'CO': r'^[0-9]{6}$',
		'CR': r'^[0-9]{4,5}$',
		'CU': r'^[0-9]{5}$',
		'CV': r'^[0-9]{4}$',
		'CX': r'^[0-9]{4}$',
		'CY': r'^[0-9]{4}$',
		'CZ': r'^[0-9]{5}$',
		'DE': r'^[0-9]{5}$',
		'DK': r'^[0-9]{4}$',
		'DO': r'^[0-9]{5}$',
		'DZ': r'^[0-9]{5}$',
		'EC': r'^EC[0-9]{6}$',
		'EE': r'^[0-9]{5}$',
		'EG': r'^[0-9]{5}$',
		'ES': r'^[0-9]{5}$',
		'ET': r'^[0-9]{4}$','FI': r'^[0-9]{5}$',
		'FK': r'^[A-Z]{4}[0-9][A-Z]{2}$',
		'FM': r'^[0-9]{5}(-[0-9]{4})?$',
		'FO': r'^[0-9]{3}$',
		'FR': r'^[0-9]{5}$',
		'GA': r'^[0-9]{2}.*[0-9]{2}$',
		'GB': r'^[A-Z][A-Z0-9]{1,3}[0-9][A-Z]{2}$',
		'GE': r'^[0-9]{4}$',
		'GF': r'^[0-9]{5}$',
		'GG': r'^([A-Z]{2}[0-9]{2,3}[A-Z]{2})$',
		'GI': r'^GX111AA$',
		'GL': r'^[0-9]{4}$',
		'GP': r'^[0-9]{5}$',
		'GR': r'^[0-9]{5}$',
		'GS': r'^SIQQ1ZZ$',
		'GT': r'^[0-9]{5}$',
		'GU': r'^[0-9]{5}$',
		'GW': r'^[0-9]{4}$',
		'HM': r'^[0-9]{4}$',
		'HN': r'^[0-9]{5}$',
		'HR': r'^[0-9]{5}$',
		'HT': r'^[0-9]{4}$',
		'HU': r'^[0-9]{4}$',
		'ID': r'^[0-9]{5}$',
		'IL': r'^[0-9]{7}$',
		'IM': r'^IM[0-9]{2,3}[A-Z]{2}$$',
		'IN': r'^[0-9]{6}$',
		'IO': r'^[A-Z]{4}[0-9][A-Z]{2}$',
		'IQ': r'^[0-9]{5}$','IR': r'^[0-9]{5}-[0-9]{5}$',
		'IS': r'^[0-9]{3}$',
		'IT': r'^[0-9]{5}$',
		'JE': r'^JE[0-9]{2}[A-Z]{2}$',
		'JM': r'^JM[A-Z]{3}[0-9]{2}$',
		'JO': r'^[0-9]{5}$',
		'JP': r'^[0-9]{3}-?[0-9]{4}$',
		'KE': r'^[0-9]{5}$',
		'KG': r'^[0-9]{6}$',
		'KH': r'^[0-9]{5}$',
		'KR': r'^[0-9]{5}$',
		'KY': r'^KY[0-9]-[0-9]{4}$',
		'KZ': r'^[0-9]{6}$',
		'LA': r'^[0-9]{5}$',
		'LB': r'^[0-9]{8}$',
		'LI': r'^[0-9]{4}$',
		'LK': r'^[0-9]{5}$',
		'LR': r'^[0-9]{4}$',
		'LS': r'^[0-9]{3}$',
		'LT': r'^(LT-)?[0-9]{5}$',
		'LU': r'^[0-9]{4}$',
		'LV': r'^LV-[0-9]{4}$',
		'LY': r'^[0-9]{5}$',
		'MA': r'^[0-9]{5}$',
		'MC': r'^980[0-9]{2}$',
		'MD': r'^MD-?[0-9]{4}$',
		'ME': r'^[0-9]{5}$',
		'MF': r'^[0-9]{5}$',
		'MG': r'^[0-9]{3}$','MH': r'^[0-9]{5}$',
		'MK': r'^[0-9]{4}$',
		'MM': r'^[0-9]{5}$',
		'MN': r'^[0-9]{5}$',
		'MP': r'^[0-9]{5}$',
		'MQ': r'^[0-9]{5}$',
		'MT': r'^[A-Z]{3}[0-9]{4}$',
		'MV': r'^[0-9]{4,5}$',
		'MX': r'^[0-9]{5}$',
		'MY': r'^[0-9]{5}$',
		'MZ': r'^[0-9]{4}$',
		'NA': r'^[0-9]{5}$',
		'NC': r'^[0-9]{5}$',
		'NE': r'^[0-9]{4}$',
		'NF': r'^[0-9]{4}$',
		'NG': r'^[0-9]{6}$',
		'NI': r'^[0-9]{5}$',
		'NL': r'^[0-9]{4}[A-Z]{2}$',
		'NO': r'^[0-9]{4}$',
		'NP': r'^[0-9]{5}$',
		'NZ': r'^[0-9]{4}$',
		'OM': r'^[0-9]{3}$',
		'PA': r'^[0-9]{6}$',
		'PE': r'^[0-9]{5}$',
		'PF': r'^[0-9]{5}$',
		'PG': r'^[0-9]{3}$',
		'PH': r'^[0-9]{4}$',
		'PK': r'^[0-9]{5}$',
		'PL': r'^[0-9]{2}-?[0-9]{3}$','PM': r'^[0-9]{5}$',
		'PN': r'^[A-Z]{4}[0-9][A-Z]{2}$',
		'PR': r'^[0-9]{5}$',
		'PT': r'^[0-9]{4}(-?[0-9]{3})?$',
		'PW': r'^[0-9]{5}$',
		'PY': r'^[0-9]{4}$',
		'RE': r'^[0-9]{5}$',
		'RO': r'^[0-9]{6}$',
		'RS': r'^[0-9]{5}$',
		'RU': r'^[0-9]{6}$',
		'SA': r'^[0-9]{5}$',
		'SD': r'^[0-9]{5}$',
		'SE': r'^[0-9]{5}$',
		'SG': r'^([0-9]{2}|[0-9]{4}|[0-9]{6})$',
		'SH': r'^(STHL1ZZ|TDCU1ZZ)$',
		'SI': r'^(SI-)?[0-9]{4}$',
		'SK': r'^[0-9]{5}$',
		'SM': r'^[0-9]{5}$',
		'SN': r'^[0-9]{5}$',
		'SV': r'^01101$',
		'SZ': r'^[A-Z][0-9]{3}$',
		'TC': r'^TKCA1ZZ$',
		'TD': r'^[0-9]{5}$',
		'TH': r'^[0-9]{5}$',
		'TJ': r'^[0-9]{6}$',
		'TM': r'^[0-9]{6}$',
		'TN': r'^[0-9]{4}$',
		'TR': r'^[0-9]{5}$',
		'TT': r'^[0-9]{6}$','TW': r'^([0-9]{3}|[0-9]{5})$',
		'UA': r'^[0-9]{5}$',
		'US': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
		'UY': r'^[0-9]{5}$',
		'UZ': r'^[0-9]{6}$',
		'VA': r'^00120$',
		'VC': r'^VC[0-9]{4}',
		'VE': r'^[0-9]{4}[A-Z]?$',
		'VG': r'^VG[0-9]{4}$',
		'VI': r'^[0-9]{5}$',
		'VN': r'^[0-9]{6}$',
		'WF': r'^[0-9]{5}$',
		'XK': r'^[0-9]{5}$',
		'YT': r'^[0-9]{5}$',
		'ZA': r'^[0-9]{4}$',
		'ZM': r'^[0-9]{5}$',
		}

	def get_country(self):
		choices = list(Country.objects.values_list('id','name'))
		choices[0]=(0,'Please select Country')
		return choices

	def get_state(self):
		choices = list(State.objects.values_list('id','name'))
		choices[0]=(0,'Please select State')
		return choices

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["country"] = forms.TypedChoiceField(choices=self.get_country())
		self.fields["state"] = forms.TypedChoiceField(choices=self.get_state())
		fields_key_order = ['uid','address','pin_code','phone_number','country','state','date_of_birth']

		if 'keyOrder' in self.fields:
			self.fields.keyOrder = fields_key_order
		else:
			self.fields = OrderedDict((k, self.fields[k]) for k in fields_key_order)

	class Meta:
		model = Profile
		fields = ('address','pin_code','phone_number','profile_image','country','state','date_of_birth')
		widgets = { 'date_of_birth': DateInput(),}
