"""
demo api testcase
"""

import pytest
import requests
import os
import json

class Test_api:
	global se
	se =requests.session()
	
	def test_demo_api(self):
		response=se.get("https://reqres.in/api/users?page=2")
		json_response =response.json()
		assert response.status_code ==200
		assert json_response['page'] == 2
		assert json_response[ "total_pages"] ==2
		print(json_response)
		
		
		