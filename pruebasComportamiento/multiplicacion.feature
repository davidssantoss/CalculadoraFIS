Feature: calculadora

Scenario Outline: get multiplicacion total
Given a <values> to multiply
When the calc multiply the values 
Then <total> of multiply is ok

Examples: values
|   values  |   total   |
|   5,7     |   35      |
|   8,3     |   24      |
|   51,7    |   357     |
|   20,11   |   220     |
|   -19,-4  |   76     |