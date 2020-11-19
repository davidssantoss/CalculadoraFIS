from behave import *
from calculadora import Calculadora

@given('a {values} to sum')
def step_imp(context, values):
    context.calc = Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc sum the values')
def step_imp(context):
        context.total = context.calc.sumar(context.values[0], context.values[1])

@then('{total:d} of sum is ok')
def step_imp(context, total):
    assert (context.total == total)
