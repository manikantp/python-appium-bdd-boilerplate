from appium import webdriver

driver: webdriver.Remote = None
__driver_configs = {}


def driver_setup(host, port, appium_version, platform_name, platform_version,
                 device_name, browser_name, test_name, app_uri, saucelabs_user,
                 saucelabs_key, saucelabs_on):
    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['platform_name'] = platform_name
    __driver_configs['platform_version'] = platform_version
    __driver_configs['device_name'] = device_name
    __driver_configs['browser_name'] = browser_name
    __driver_configs['test_name'] = test_name
    __driver_configs['app_uri'] = app_uri
    __driver_configs['saucelabs_user'] = saucelabs_user
    __driver_configs['saucelabs_key'] = saucelabs_key
    __driver_configs['saucelabs_on'] = saucelabs_on


def start_driver():
    global driver
    # TODO: If 'saucelabs_on' is true, use sauce labs
    driver = webdriver.Remote(
        command_executor='http://{}:{}/wd/hub'.format(__driver_configs.get('host'), __driver_configs.get('port')),
        desired_capabilities={
            'platformName': __driver_configs.get('platform_name'),
            'platformVersion': __driver_configs.get('platform_version'),
            'deviceName': __driver_configs.get('device_name'),
            'app': __driver_configs.get('app_uri')
        })


def cleanup_driver():
    driver.dreset()


def teardown_driver():
    # The method 'driver.close()' is not yet implemented
    pass


def add_screenshot_failure_to_result(scenario):
    # Do some magic with scenario and driver.get_screenshot_as_png()
    pass
