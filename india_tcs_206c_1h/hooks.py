# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "india_tcs_206c_1h"
app_title = "India TCS 206C_1H"
app_publisher = "aerele"
app_description = "Implementing TCS - 206C(1H) Introduced by Finance Act, 2020 in India."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@aerele.in"
app_license = "GPL-3.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/india_tcs_206c_1h/css/india_tcs_206c_1h.css"
# app_include_js = "/assets/india_tcs_206c_1h/js/india_tcs_206c_1h.js"

# include js, css files in header of web template
# web_include_css = "/assets/india_tcs_206c_1h/css/india_tcs_206c_1h.css"
# web_include_js = "/assets/india_tcs_206c_1h/js/india_tcs_206c_1h.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "india_tcs_206c_1h.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "india_tcs_206c_1h.install.before_install"
# after_install = "india_tcs_206c_1h.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "india_tcs_206c_1h.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Sales Invoice": {
		"validate": "india_tcs_206c_1h.india_tcs_206c_1h.doctype.india_tcs_206c_1h_app_settings.india_tcs_206c_1h_app_settings.set_tcs"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"india_tcs_206c_1h.tasks.all"
# 	],
# 	"daily": [
# 		"india_tcs_206c_1h.tasks.daily"
# 	],
# 	"hourly": [
# 		"india_tcs_206c_1h.tasks.hourly"
# 	],
# 	"weekly": [
# 		"india_tcs_206c_1h.tasks.weekly"
# 	]
# 	"monthly": [
# 		"india_tcs_206c_1h.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "india_tcs_206c_1h.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "india_tcs_206c_1h.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "india_tcs_206c_1h.task.get_dashboard_data"
# }

