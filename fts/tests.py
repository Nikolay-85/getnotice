from django.test import LiveServerTestCase
from selenium import webdriver
import requests
from pyvirtualdisplay import Display

class MessageTest(LiveServerTestCase):
    """
    Testing whole message sending/receiving parts

    """

    def setUp(self):
        """
        On start

        """
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """
        On test stop

        """
        self.browser.quit()
        self.display.stop()

    def test_can_send_and_receive_broadcast_messages(self):
        """
        User can send message through API and see it in browser (less than 10 seconds after)

        """
        from selenium.webdriver.support.wait import WebDriverWait
        # User open dashboard
        self.browser.get(self.live_server_url + '/')
        # He see dashboard welcome text
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Some dashboard text', body.text)

        # He can send message via API (with 3-rd party utility)
        payload = {'text': 'checkit', 'level': 'info'}
        requests.post(self.live_server_url + '/messages/', data=payload)
        WebDriverWait(self.browser, 10).until(
            lambda driver: driver.find_element_by_css_selector('.wsmsg'))

        message = self.browser.find_element_by_css_selector('.wsmsg')
        self.assertIn('checkit', message.text)

    def test_cannot_send_invalid_messages(self):
        """
        User cannot send invalid message

        """
        self.browser.get(self.live_server_url + '/')
        # He see dashboard welcome text
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Some dashboard text', body.text)

        # He cannot send message via API (with 3-rd party utility)
        payload = {'text': 'c'*10000, 'level': 'info'}
        r = requests.post(self.live_server_url + '/messages/', data=payload)
        self.assertEqual(400, r.status_code)

        payload = {'text': '', 'level': 'info'}
        r = requests.post(self.live_server_url + '/messages/', data=payload)
        self.assertEqual(400, r.status_code)

        payload = {'text': 'test', 'level': 'somenewlevel'}
        r = requests.post(self.live_server_url + '/messages/', data=payload)
        self.assertEqual(400, r.status_code)