from selenium.webdriver import Chrome


class Cookies:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def add(self, name, domain, value):
        '''
        add cookie
        :param name: take name of cookie
        :param domain: take domain of cookie
        :param value: take value of cookie
        :return: none
        '''
        self.driver.add_cookie({"name": name,
                                "domain": domain,
                                "value": value})

    def get(self, name):
        '''
        get cookie by name
        :param name: take name of cookie
        :return: cookie
        '''
        result = self.driver.get_cookie(name)
        return result


