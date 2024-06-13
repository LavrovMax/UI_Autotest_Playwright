from playwright_framework.pages.base_page import BasePage as BP


class BasePage(BP):
    def __init__(self, page):
        super().__init__(page)

    def press_page_down_multiply(self, count, button):
        for i in range(count):
            self.page.keyboard.press(button)

