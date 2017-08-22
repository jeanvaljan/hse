// Copyright (c) 2016, Ionut Dumitrescu and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SOR Reporting"] = {
	"filters": [
{
			"fieldname":"site",
			"label": __("Site"),
			"fieldtype": "Link",
			"options": "Site",
			"reqd": 1
		},
		{
			"fieldname":"project",
			"label": __("Project"),
			"fieldtype": "Link",
			"options": "Projects",
			"reqd": 1
		}

	]
}
