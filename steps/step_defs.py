from behave import given, when, then
from utils.driver_helper import driver
from page_objects import reddit_home_screen


@given("the app is installed")
def step_impl(context):
    assert(driver.is_app_installed("com.reddit.frontpage"))


@given("I open the app")
def step_impl(context):
    if not reddit_home_screen.is_open():
        raise Exception('Driver was unable to lead the apk')
    pass


@when("I search for '{search}'")
def step_impl(context, search):
    # Do something with driver....
    pass


@then("I see the gaming subreddit")
def step_impl(context):
    # Do something with driver....
    pass
