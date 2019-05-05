from selenium import webdriver

WEB_SITE = "https://www.google.com"

POSITIVE_MESSAGE = '{web_browser} browser works correctly!'
NEGATIVE_MESSAGE = 'There are problems with {web_browser} browser'


# Chrome
def test_chrome_browser():
    chrome_browser = webdriver.Chrome(executable_path='drivers/chrome/74/chromedriver.exe')
    chrome_browser.get(WEB_SITE)
    chrome_browser.quit()


# Firefox
def test_firefox_browser():
    firefox_browser = webdriver.Firefox(executable_path='drivers/gecko/0_24/geckodriver.exe')
    firefox_browser.get(WEB_SITE)
    firefox_browser.quit()


# Opera
def test_opera_browser():
    opera_browser = webdriver.Opera(executable_path='drivers/opera/2_45/operadriver.exe')
    opera_browser.get(WEB_SITE)
    opera_browser.quit()


# Test Edge (MS Explorer)
def test_edge_browser():
    # No path needed. Execute following command
    # DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0
    edge_browser = webdriver.Edge()
    edge_browser.get(WEB_SITE)
    edge_browser.quit()


try:
    test_chrome_browser()
except:
    print(NEGATIVE_MESSAGE.format(web_browser="Chrome"))
else:
    print(POSITIVE_MESSAGE.format(web_browser="Chrome"))

try:
    test_firefox_browser()
except:
    print(NEGATIVE_MESSAGE.format(web_browser="Firefox"))
else:
    print(POSITIVE_MESSAGE.format(web_browser="Firefox"))

try:
    test_edge_browser()
except:
    print(NEGATIVE_MESSAGE.format(web_browser="Edge"))
else:
    print(POSITIVE_MESSAGE.format(web_browser="Edge"))

try:
    test_opera_browser()
except:
    print(NEGATIVE_MESSAGE.format(web_browser="Opera"))
else:
    print(POSITIVE_MESSAGE.format(web_browser="Opera"))
