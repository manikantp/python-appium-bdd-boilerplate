from utils.driver_helper import *

"""
before_all(context), after_all(context)
    These run before and after everything
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.
before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.
before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
"""


def before_all(context):
    print("Setup")
    context.config.setup_logging()
    driver_setup(context.config.userdata.get("appium_host", "unknown"),
                 context.config.userdata.get("appium_port", "unknown"),
                 context.config.userdata.get("appium_version", "unknown"),
                 context.config.userdata.get("platform_name", "unknown"),
                 context.config.userdata.get("platform_version", "unknown"),
                 context.config.userdata.get("device_name", "unknown"),
                 context.config.userdata.get("browser_name", "unknown"),
                 context.config.userdata.get("test_name", "unknown"),
                 context.config.userdata.get("app_uri", "unknown"),
                 context.config.userdata.get("saucelabs_user", "unknown"),
                 context.config.userdata.get("saucelabs_key", "unknown"),
                 context.config.userdata.get("saucelabs_on", "unknown"))
    start_driver()


def after_all(context):
    print("Tear down")
    teardown_driver()


def before_scenario(context, scenario):
    # Do some magic in case the scenario requires fresh start
    cleanup_driver()
    pass


def after_scenario(context, scenario):
    # Take screenshot if fails
    if scenario.status == 'failed':
        add_screenshot_failure_to_result(scenario)
