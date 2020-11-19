Feature: calculadora

Scenario Outline: get suma total
Given a <values> to sum
When the calc sum the values 
Then <total> of sum is ok

Examples: values
|   values  |   total   |
|   5,7     |   12      |
|   8,3     |   11      |
|   51,7    |   58      |
|   20,11   |   31      |
|   -19,-4  |   -23     |