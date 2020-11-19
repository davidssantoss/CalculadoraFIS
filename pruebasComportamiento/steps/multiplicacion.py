from behave import *
from calculadora import Calculadora

@given('a {values} to multiply')
def step_imp(context, values):
    context.calc = Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc multiply the values')
def step_imp(context):
        context.total = context.calc.multiplicar(context.values[0], context.values[1])

@then('{total:d} of multiply is ok')
def step_imp(context, total):
    assert (context.total == total)
