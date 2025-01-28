import pytest
import requests
import cloudscraper
import unittest
from utils.api_constants import *

class TestN11Login(unittest.TestCase):

    def test_valid_login(self):
        url = BASE_URL_API
        payload = {
            'email': VALID_USER_EMAIL,
            'password': VALID_USER_PASSWORD,
            'rememberMe': 'on',
            'returnUrl': '/hesabim/siparislerim'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # Bypassing Cloudflare Protection with Cloudscraper Python library
        # Issue: The Cloudflare system used by N11 checks whether incoming requests 
        # come from a bot or a real browser. The standard requests library cannot 
        # bypass these security checks, which resulted in a 403 (Forbidden) error.
        # Solution: We integrated the cloudscraper library, which automatically generates 
        # the required tokens and cookies to bypass Cloudflare's security mechanisms.
        scraper = cloudscraper.create_scraper()
        response = scraper.post(url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200,
                          f"The login was expected to succeed, but the status code was: {response.status_code}"
        )
