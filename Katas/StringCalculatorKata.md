# String Calculator
- [String Calculator](#string-calculator)
  - [Objective](#objective)
  - [Requirements](#requirements)
    - [Feature: Add zero, one, or two numbers](#feature-add-zero-one-or-two-numbers)
    - [Feature: Add a list of numbers of an unknown length](#feature-add-a-list-of-numbers-of-an-unknown-length)
    - [Feature: Accept newline char as delimiter](#feature-accept-newline-char-as-delimiter)
    - [Feature: Allow configurable delimiters](#feature-allow-configurable-delimiters)
    - [Feature: Support error handling for negative numbers](#feature-support-error-handling-for-negative-numbers)
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

**Note:** Don't forget to refactor between tests!

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
| "1,2,4"     | 7      |
| "1,2,3,4,5" | 15     |

### Feature: Accept newline char as delimiter 

    As a library user  
    I want to call an Add method using newline characters to delimit my arguments
    So that I can use the program for a wider range of input data formats
    -------------------------------------------------------
    Given the calculator is running
    When I enter $args
    Then the calculator returns $result

**Test Cases**

| args       | result                            |
| ---------- | --------------------------------- |
| "1,30\n10" | 41                                |
| "1\n3\n5"  | 9                                 |
| "1,\n"     | invalid input (no need to handle) |


### Feature: Allow configurable delimiters 

 > To change a delimiter, the beginning of the string will contain a separate line that looks like this: ```“//[delimiter]\n[numbers…]”```

    As a library user  
    I want to specify the delimiter
    So that I can use the program for an even wider range of input data formats
    -------------------------------------------------------
    Given the calculator is running
    When I enter $args
    Then the calculator returns $result

**Test Cases**

| args         | result |
| ------------ | ------ |
| "//;\n1;2"   | 3      |
| "//#\n4#2#3" | 9      |

**Note:** delimiter specification is optional, thus your previous tests should all pass without modification after implementing this feature

### Feature: Support error handling for negative numbers

 > When the calculator receives arguments < 0, it should return an error in the form of "Error - negative numbers not allowed: [negative number(s)]"

    As a library user  
    I want to catch errors in my input data
    So that I can ensure the integrity of my results
    -------------------------------------------------------
    Given the calculator is running
    When I enter $args
    Then the calculator returns $result

**Test Cases**

| args            | result                                         |
| --------------- | ---------------------------------------------- |
| "7,8,-9"        | "Error - negative numbers not allowed: -9      |
| "//@\n-10@2@-3" | "Error - negative numbers not allowed: -10, -2 |