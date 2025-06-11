from com.utils.browserUtils import BrowserUtils


class DashboardPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)

    def dashboardPageUrl(self):
        return self.currentPageUrl("dashboard")



