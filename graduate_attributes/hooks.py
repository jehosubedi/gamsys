app_name = "graduate_attributes"
app_title = "APC GA"
app_publisher = "Team Tacos"
app_description = "APC GA Develop by Team Tacos"
app_email = "jbsubedi@student.apc.edu.ph"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "graduate_attributes",
		"logo": "/assets/graduate_attributes/icons/GA.svg",
		"title": "APC Graduate Attributes",
		"route": "/app/overview",
		# "has_permission": "graduate_attributes.api.permission.has_app_permission"
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/graduate_attributes/css/graduate_attributes.css"
# app_include_js = "/assets/graduate_attributes/js/graduate_attributes.js"

# include js, css files in header of web template
# web_include_css = "/assets/graduate_attributes/css/graduate_attributes.css"
# web_include_js = "/assets/graduate_attributes/js/graduate_attributes.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "graduate_attributes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "graduate_attributes/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "graduate_attributes.utils.jinja_methods",
# 	"filters": "graduate_attributes.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "graduate_attributes.install.before_install"
# after_install = "graduate_attributes.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "graduate_attributes.uninstall.before_uninstall"
# after_uninstall = "graduate_attributes.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "graduate_attributes.utils.before_app_install"
# after_app_install = "graduate_attributes.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "graduate_attributes.utils.before_app_uninstall"
# after_app_uninstall = "graduate_attributes.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "graduate_attributes.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"graduate_attributes.tasks.all"
# 	],
# 	"daily": [
# 		"graduate_attributes.tasks.daily"
# 	],
# 	"hourly": [
# 		"graduate_attributes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"graduate_attributes.tasks.weekly"
# 	],
# 	"monthly": [
# 		"graduate_attributes.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "graduate_attributes.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "graduate_attributes.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "graduate_attributes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "graduate_attributes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["graduate_attributes.utils.before_request"]
# after_request = ["graduate_attributes.utils.after_request"]

# Job Events
# ----------
# before_job = ["graduate_attributes.utils.before_job"]
# after_job = ["graduate_attributes.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"graduate_attributes.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
