from appium import webdriver


def setup(host, port, appium_version, platform_name, platform_version,
          device_name, browser_name, test_name, app_uri, saucelabs_user,
          saucelabs_key):
    host = host
    port = port
    appium_version = appium_version
    platform_name = platform_name
    platform_version = platform_version
    device_name = device_name
    browser_name = browser_name
    test_name = test_name
    app_uri = app_uri
    saucelabs_user = saucelabs_user
    saucelabs_key = saucelabs_key
    driver = webdriver.Remote(
        command_executor='http://{}:{}/wd/hub'.format(host, port),
        desired_capabilities={
            'platformName': platform_name,
            'platformVersion': platform_version,
            'deviceName': device_name,
            'app': app_uri
        })


def teardown_driver():
    pass


def cleanup_driver():
    pass
