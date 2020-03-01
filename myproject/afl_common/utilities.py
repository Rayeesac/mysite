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

#####################################