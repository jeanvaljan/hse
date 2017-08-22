# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "HSE",
			"color": "grey",
			"icon": "assets/helmet.svg",
			"type": "module",
			"label": _("HSE")
		}
	]
