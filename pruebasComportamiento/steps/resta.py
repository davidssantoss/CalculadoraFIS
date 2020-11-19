from behave import *
from calculadora import Calculadora

@given('a {values} to substract')
def step_imp(context, values):
    context.calc = Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc substract the values')
def step_imp(context):
        context.total = context.calc.restar(context.values[0], context.values[1])

@then('{total:d} of substract is ok')
def step_imp(context, total):
    assert (context.total == total)
