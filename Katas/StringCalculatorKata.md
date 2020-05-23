# String Calculator
- [String Calculator](#string-calculator)
  - [Objective](#objective)
  - [Requirements](#requirements)
    - [Feature: Add zero, one, or two numbers](#feature-add-zero-one-or-two-numbers)
    - [Feature: Add a list of numbers of an unknown length](#feature-add-a-list-of-numbers-of-an-unknown-length)
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

**Note: Don't forget to refactor between tests!**

---

### Feature: Add a list of numbers of an unknown length 

    As a library user  
    I want to call an Add method with any number of arguments
    So that I can make calculations on data of an arbitrary length
    -------------------------------------------------------
    Given the calculator is running
    When I enter $args
    Then the calculator returns $result

**Test Cases**

| args        | result |
| ----------- | ------ |
| "1,2,10"    | 13     |
| "1,2,3,4,5" | 15     |
