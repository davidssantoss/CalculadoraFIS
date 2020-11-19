from behave import *
from calculadora import Calculadora

@given('a {values} to divide')
def step_imp(context, values):
    context.calc = Calculadora()
    context.values = [int(x) for x in values.split(",")]

@when('the calc divide the values')
def step_imp(context):
        context.total = context.calc.dividir(context.values[0], context.values[1])

@then('{total:d} of divide is ok')
def step_imp(context, total):
    assert (context.total == total)
