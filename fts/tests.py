from django.test import LiveServerTestCase
from selenium import webdriver
import time
from django.conf import settings
import requests

class MessageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_send_and_receive_broadcast_messages(self):
        from selenium.webdriver.support.wait import WebDriverWait
        # User open dashboard
        self.browser.get(self.live_server_url + '/')
        # He see dashboard welcome text
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Some dashboard text', body.text)

        # He can send message via API (with 3-rd party utility)
        # url -X POST --data '{"text":"'"${MESSAGE}"'", "level": "'"${LEVEL}"'"}'  -H "Content-type: application/json;charset=UTF-8" http://${HOST}:${PORT}/messages/
        payload = {'text': 'checkit', 'level': 'gold'}
        r = requests.post(self.live_server_url + '/messages/', data=payload)
        WebDriverWait(self.browser, 10).until(
            lambda driver: driver.find_element_by_css_selector('.wsmsg'))

        message = self.browser.find_element_by_css_selector('.wsmsg')
        self.assertIn('checkit', message.text)

    def test_cannot_send_invalid_messages(self):
        from selenium.webdriver.support.wait import WebDriverWait
        # User open dashboard
        self.browser.get(self.live_server_url + '/')
        # He see dashboard welcome text
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Some dashboard text', body.text)

        # He cannot send message via API (with 3-rd party utility)
        payload = {'text': 'c'*10000, 'level': 'gold'}
        r = requests.post(self.live_server_url + '/messages/', data=payload)
        self.assertEqual(400, r.status_code)