# Bank Optical Character Recognition

## Objective
Design a system capable of reading characters, validating account numbers, and attempting to correct invalid data.

## Background
You are tasked with designing a program for reading and processing account numbers from a file. Your company has invested in a machine that reads account numbers from paper documents and outputs them in the following format:
<pre>
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
</pre>

## User Stories

### Feature: Reads Machine Output 
    
    As a bank manager 
    I want to parse the machine output
    So that I can automate the data-entry process

Each entry is 4 lines long, and each line has 27 characters.The first 3 lines of each entry contain an account number written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9. A normal file contains around 500 entries. 


### Feature: Validates Account Numbers
    
    As a bank manager 
    I want to validate account numbers
    So that I can ensure the integrity of the output data

The machine isn't perfect - it occasionally makes mistakes when parsing input. The next step is to validate the account numbers. A valid account number has a valid checksum - this is demonstrated below:

| Account Number |   3   |   4   |   5   |   8   |   8   |   2   |   8   |   6   |   5   |
| -------------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Position Name  |  d9   |  d8   |  d7   |  d6   |  d5   |  d4   |  d3   |  d2   |  d1   |

Checksum validation: ```(d1 + 2*d2 + 3*d3 + 4*d4 + 5*d5 + 6*d6 + 7*d7 + 8*d8 + 9*d9) mod 11 = 0```




### Feature: Writes Results to Output File

    As a bank manager 
    I want to output account numbers with pertinent information
    So that I can further process the data

Extend your program to support outputting data. Use the following format (one account numebr per row): 

    457508000 
    664371495 ERR 
    86110??36 IL

If you program detects illegible output, it should replace it with a ?. Your program should also validate the checksum of each account number. Additionally, if the checksum is invalid, you should append ```ERR``` to the account number,  and if the number has illegible characters, you should append ```ILL```

### Feature: Attempts to Correct Invalid Data

    As a bank manager
    I want to automate the process of attempting to correct invalid account numbers
    So that I can quickly handle common machine input errors

You realize that often when a number comes back as ERR or ILL, it's
because the scanner failed to pick up on a single pipe or underscore
for one of the figures. For example:

<pre>
    _  _  _  _  _  _     _
|_||_|| || ||_   |  |  ||_
  | _||_||_||_|  |  |  | _|
</pre>

The 9 could be an 8 if the scanner had missed one |. Or the 0 could be
an 8. Or the 1 could be a 7. The 5 could be a 9 or 6. You should expand your program so that it attempts to guess the correct accout number for entries that come back as ERR or ILL. Your program should make this guess by adding a single pipe or underscore. If there is only one possible number with a valid
checksum, then use that. If there are several options, the status
should be AMB. If you still can't work out what it should be, the status should be reported ILL.