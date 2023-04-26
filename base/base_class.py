from datetime import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    # Method get current url
    def get_current_url(self):
        url = self.driver.current_url
        print("Current url " + url)
        return url

    # Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.now().strftime('%m.%d.%Y - %H:%M:%S')
        name_screenshot = f'screenshot[{now_date}].png'
        self.driver.save_screenshot('screen/' + name_screenshot)

    # Method assert url
    def assert_url(self, result: str):
        url = self.get_current_url()
        assert url == result
        print('Good value url')