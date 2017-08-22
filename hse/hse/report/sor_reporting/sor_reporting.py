# Copyright (c) 2013, Ionut Dumitrescu and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):

	sor_details = {}
	for sor in frappe.db.sql("""select site, project from tabsor""", as_dict=1):
		sor_details.setdefault(sor.site, sor)

	validate_filters(filters, sor_details)


	filters = set_account_currency(filters)

	columns = get_columns(filters)

	res = get_result(filters, sor_details)

	return columns, res	


def validate_filters(filters, sor_details):
	if not filters.get('site'):
		frappe.throw(_('{0} is mandatory').format(_('Contractor')))

	if filters.get("sor") and not sor_details.get(filters.sor):
		frappe.throw(_("SOR {0} does not exists").format(filters.sor))

	if filters.get("sor") and filters.get("group_by_account") \
			and sor_details[filters.sor].is_group == 0:
		frappe.throw(_("Can not filter based on Account, if grouped by Account"))

	if filters.get("voucher_no") and filters.get("group_by_voucher"):
		frappe.throw(_("Can not filter based on Voucher No, if grouped by Voucher"))

	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))
