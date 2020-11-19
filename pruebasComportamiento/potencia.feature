Feature: calculadora

Scenario Outline: get potencia total
Given a <values> to pow
When the calc pow the values 
Then <total> of pow is ok

Examples: values
|   values  |   total   |
|   5,2     |   25      |
|   8,3     |   512     |
|   51,1    |   51      |
|   20,0    |   1      |
|   -19,2   |   361     |