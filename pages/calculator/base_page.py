from playwright_framework.pages.base_page import BasePage as BP


class BasePage(BP):
    def __init__(self, page):
        super().__init__(page)
