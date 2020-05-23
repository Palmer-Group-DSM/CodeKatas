# String Calculator

## Objective
Create a string calculator capable of handling increasingly complex input data

## Requirements
### Feature: Add zero, one, or two numbers

    As a library user  
    I want to call an Add method with 0, 1, or 2 arguments
    So that I can make calculations
    -------------------------------------------------------
    Given the calculator is running
    When I enter $args
    Then the calculator returns $result

**Test Cases**

| args  | result |
| ----- | ------ |
| ""    | 0      |
| "5"   | 5      |
| "1,2" | 3      |

---

