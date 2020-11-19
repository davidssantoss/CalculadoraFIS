Feature: calculadora

Scenario Outline: get division total
Given a <values> to divide
When the calc divide the values 
Then <total> of divide is ok

Examples: values
|   values  |   total   |
|   120,2   |   60      |
|   9,3     |   3       |
|   49,7    |   7       |
|   20,0    |   No se puede dividir por cero    |
|   -20,-4  |   5       |
