from seleniumbase import BaseCase
import time

class Pruebas(BaseCase):
    # sign-in information
    sign_in_btn = "//*[@id='page']/header/div/div[7]/nav/a[1]"
    email = "paunatareadelacollege@gmail.com"
    password = "ineedtowriteapassword123"
    email_input = "#emailOrUsername"
    password_input = "#password"
    sign_in_submit = "#sign-in"

    # search information
    discover_new_btn = "//*[@id='root']/div/div/header/div[1]/a[4]"
    search_input = "//*[@id='pgn-searchfield-input-11']"
    search_submit = "#search-landing-search-submit"
    search_value = "python"
    search_url = "https://www.edx.org/search?q=python"

    # resume course
    resume_btn = "//*[@id='card-0']/div/div/div[1]/div/div[3]/div/a[2]"
    course_title = "//*[@id='root']/div/header/div/div[1]/span[2]"

    # change language
    language_select = "#site-footer-language-select"
    spanish_option = "//*[@id='site-footer-language-select']/option[2]"
    apply_btn = "#site-footer-language-submit"

    # see records
    user_menu = "//*[@id='user']"
    profile_option = "//*[@id='root']/div/div/header/div[2]/div/a[3]"
    view_records = "//*[@id='main']/div/div[2]/div[1]/div[2]/div[2]/a"
    learner_records_title = "//*[@id='main-content']/h1"

    def setUp(self, **kwargs):
        super().setUp()
        self.open("https://www.edx.org")

    def test_sign_in(self):
        # puts information into the input fields
        self.click(self.sign_in_btn)
        self.send_keys(self.email_input, self.email)
        self.send_keys(self.password_input, self.password)
        # sends information of the input fields
        self.click(self.sign_in_submit)
        # checks for the title of the actual page
        time.sleep(5)
        self.assert_title("Learner Home")
        self.save_screenshot("sign_in_test", "screenshoots")

    def test_search(self):
        # sign-in to the account
        self.test_sign_in()
        # goes to the search page
        self.click(self.discover_new_btn)
        # puts information into the input field
        time.sleep(5)
        self.assert_title("edX Courses | View all online courses on edX.org")  # waits to get to the new page
        self.send_keys(self.search_input, self.search_value)
        # sends information of the input field
        self.click(self.search_submit)
        self.save_screenshot("search_test", "screenshoots")

    def test_resume_course(self):
        # sign in
        self.test_sign_in()
        # clicks a button to resume a course
        self.click(self.resume_btn)
        time.sleep(5)
        # checks that the course was accesed to
        self.assert_element(self.course_title)
        self.save_screenshot("resume_course_test", "screenshoots")

    def test_change_language(self):
        self.scroll_to_bottom()
        self.click(self.language_select)
        self.click(self.spanish_option)
        self.save_screenshot("change_language_test", "screenshoots")

    def test_view_records(self):
        self.test_sign_in()
        self.click(self.user_menu)
        self.click(self.profile_option)
        self.click(self.view_records)
        time.sleep(5)
        self.assert_element(self.learner_records_title)
        self.save_screenshot("view_records_test", "screenshoots")
