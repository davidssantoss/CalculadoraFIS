Feature: calculadora

Scenario Outline: get resta total
Given a <values> to substract
When the calc substract the values 
Then <total> of substract is ok

Examples: values
|   values  |   total   |
|   5,7     |   -2      |
|   8,3     |   5       |
|   51,7    |   44      |
|   20,11   |   9       |
|   -19,-4  |   -15     |