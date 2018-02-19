from behave import given, when, then


@given("the app is running")
def step_impl(context):
    pass


@given("I open the app")
def step_impl(context):
    print("Passing this step: I open the app")
    pass


@when("I search for '{search}'")
def step_impl(context, search):
    assert len(search) != 0
    pass


@then("I see the gaming subreddit")
def step_impl(context):
    pass
