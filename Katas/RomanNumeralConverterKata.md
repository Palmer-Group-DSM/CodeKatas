# Roman Numeral Converter Kata
- [Roman Numeral Converter Kata](#roman-numeral-converter-kata)
  - [Objective](#objective)
    - [1. Write a program to convert Arabic numbers to Roman numerals](#1-write-a-program-to-convert-arabic-numbers-to-roman-numerals)
    - [2. Write a program to convert Roman Numerals to Arabic numbers](#2-write-a-program-to-convert-roman-numerals-to-arabic-numbers)
  - [Background](#background)
  - [Rules](#rules)
    - [Roman Numeral Symbols](#roman-numeral-symbols)
## Objective
### 1. Write a program to convert Arabic numbers to Roman numerals
    1     ->   I
    11    ->   XI
    394   ->   CCCXCIV
### 2. Write a program to convert Roman Numerals to Arabic numbers
    I       ->  1
    XIV     ->  14
    MDCCXCV ->  1795
**Note: There is no need to handle numbers larger than about 3000.**
## Background
Roman numerals are an ancient numeral writing system. They are still in common use today (e.g., Games of the XXXII Olympiad or *The Godfather Part III*). 
## Rules
### Roman Numeral Symbols
| Symbol | Decimal Value |
| :----: | :-----------: |
|   I    |       1       |
|   V    |       5       |
|   X    |      10       |
|   L    |      50       |
|   C    |      100      |
|   D    |      500      |
|   M    |     1000      |

In standard form, numeral symbols are placed in order of value, starting with the largest value. When smaller values precede larger values (e.g., IX), it indicates that the smaller values should be subtracted from the larger values, and the result is added to the total. **However, you can’t write numerals like “IM” for 999, there are some additional rules:**

- A number written in Arabic numerals can be broken into component digits. For example, 3906 is composed of 3 (three thousand), 9 (nine hundreds), 0 (zero tens), and 6 (six units). To write the Roman numeral, each of the nonzero digits should be treated separately. In the above example, 3,000 = MMM, 900 = CM, and 6=VI. Therefore, 3906 = MMMCMVI. 
  
- The symbols 'I', 'X', 'C', and 'M' can be repeated at most 3 times in a row. 
  
- The symbols 'V', 'L', and 'D' can never be repeated. 
  
- The '1' symbols ('I', 'X', and 'C') can only be subtracted from the 2 next highest values ('IV' and 'IX', 'XL' and 'XC', 'CD' and 'CM'). 
  
- Only one subtraction can be made per numeral ('XC' is allowed, 'XXC' is not). The '5' symbols ('V', 'L', and 'D') can never be subtracted. 

