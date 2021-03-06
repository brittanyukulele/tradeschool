from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.core.urlresolvers import reverse
from datetime import *
from tradeschool.models import *


class RegistrationSeleniumTestCase(LiveServerTestCase):
    """
    """
    fixtures = ['email_initial_data.json',
                'teacher-info.json',
                'sample_data.json'
                ]

    @classmethod
    def setUpClass(self):
        """ Start Selenium.
        """
        # start Firefox websdriver
        self.selenium = WebDriver()

        # call super setup method
        super(RegistrationSeleniumTestCase, self).setUpClass()

    def setUp(self):
        # change the language to english for language-based assertations
        self.branch = Branch.objects.all()[0]
        self.branch.language = 'en'
        self.branch.save()

        # approve a scheduled class so it appears on the website
        self.course = Course.objects.filter(branch=self.branch)[0]
        self.course.status = 'approved'
        self.course.save()

        self.timeout = 2

    def test_registration_toggle_button(self):
        """ Tests that clicking the title of a scheduled class
            on the website expands the div.
        """
        # construct server url
        course_list_url = reverse(
            'course-list', kwargs={'branch_slug': self.branch.slug})
        live_url = "%s%s" % (self.live_server_url, course_list_url)

        # load page
        self.selenium.get(live_url)

        # find a scheduled class title and click on it
        toggle_button = self.selenium.find_element_by_class_name('toggle')

        self.assertTrue(toggle_button.is_displayed())
        toggle_button.click()

    def test_registration_join_button(self):
        """ Tests that clicking on the join button sends an ajax request.
        """
        # construct server url
        course_register_url = reverse('course-register', kwargs={
            'branch_slug': self.branch.slug,
            'course_slug': self.course.slug
        })

        live_url = "%s%s" % (self.live_server_url, course_register_url)

        # load page
        self.selenium.get(live_url)

        # find a scheduled class join button
        join_button = self.selenium.find_element_by_class_name('join')

        self.assertTrue(join_button.is_displayed())

        join_button.click()

    def tearDown(self):
        """ Delete Branch files.
        """
        # delete branches' files
        for branch in Branch.objects.all():
            branch.delete_files()

    @classmethod
    def tearDownClass(self):
        # stop selenium
        self.selenium.quit()

        # call super teardown method
        super(RegistrationSeleniumTestCase, self).tearDownClass()
