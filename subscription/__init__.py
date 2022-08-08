# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.sessions import Session, delete_session
__version__ = '0.0.1'

def validate_license():
	license = frappe.db.get_value("License Subscription Settings", "License Subscription Settings", "license_id")
	user = frappe.session.user
	if user != "Administrator":	
	
		if not license:
			frappe.throw("License not found, Contact your Administrator")

		import requests

		url = "http://license.ribox.me/api/license/CheckLicense/"+license

		payload={}
		headers = {
		'authorization': 'Basic U01COlNNQkAyMDE5'
		}

		response = requests.request("GET", url, headers=headers, data=payload)

		if response.status_code == 200:
			data = response.json()
			if data['statusCode'] in ['A', 'B', 'C', 'F']:
				delete_session(frappe.session.sid, frappe.session.user)
				frappe.throw(data['message'])
			elif data['statusCode'] == 'D':
				frappe.msgprint(data['message'])
		else:
			frappe.throw("Something went wrong!, please try again later")

