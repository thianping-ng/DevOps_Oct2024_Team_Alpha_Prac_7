from behave import *
from calculator import add, subtract, multiplication, division, cosine, sine, tangent

@given('the calculator is intialized')
def step_impl(context):
    context.result = None
    context.error = None

@when('I add {a:d} and {b:d}')
def step_when_add(context, a, b):
    context.result = add(a, b)

@when('I subtract {a:d} and {b:d}')
def step_when_subtract(context, a, b):
    context.result = subtract(a,b)
@when('I mutiply {a:d} and {b:d}')
def step_when_multiply(context, a,b):
    context.result = multiplication(a,b)

@when('I divide {a:d} and {b:d}')
def step_when_divide(context, a,b):
    context.result = division(a,b)

@when('I calculate the cosine of {x:d}')
def step_when_cosine(context, x):
    context.result = cosine(x)

@when('I calculate the sine of {x:d}')
def step_when_sine(contex, x):
    contex.result = sine(x)

@when('I calculate the tangent of {x:d}')
def step_when_tangent(context, x):
    context.result = tangent(x)

@then("the result should be {expected_result:d}")
def step_then_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"