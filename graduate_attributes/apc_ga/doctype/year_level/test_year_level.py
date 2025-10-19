# Copyright (c) 2025, Team Tacos and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


<<<<<<< HEAD

<<<<<<< HEAD:graduate_attributes/apc_ga/doctype/self_assessment/test_self_assessment.py
class IntegrationTestSelfAssessment(IntegrationTestCase):
=======
=======
>>>>>>> 14d33e5 (ui: added new charts for program analysis)
class IntegrationTestYearLevel(IntegrationTestCase):
>>>>>>> 223fcdc (ui: updated self assessment doctypes and fixed bugs):graduate_attributes/apc_ga/doctype/year_level/test_year_level.py
	"""
	Integration tests for YearLevel.
	Use this class for testing interactions between multiple components.
	"""

	pass
