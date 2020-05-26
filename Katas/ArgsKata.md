# Args
- [Args](#args)
  - [Objective](#objective)
  - [Requirements](#requirements)
    - [Flags, Values and Schema](#flags-values-and-schema)
    - [Default Values](#default-values)
    - [Error Handling](#error-handling)
    - [Extension](#extension)
    - [Notes](#notes)
  - [Additional Requirement](#additional-requirement)
## Objective
Write a program to parse command-line arguments.

## Requirements
### Flags, Values and Schema
Parsing command-line arguments is a common requirement of command-line applications. Command line arguments consist of **flags** and **values**. Flags take the form of a single character prepended with a minus sign. Each flag should have zero or one value associated with it. Your program will need a way to describe the arg **schema**. The **schema** specifies the number and type of flags and values.

For example, consider a program called with these arguments:  
    
    -v -p 8080 -d /usr/logs

The schema is indicated as having 3 flags (v, p, d). The 'v' flag does not have any values associated with it - it's a boolean value,  ```true``` if present, ```false``` if not. The 'p' flag (port in this case) should be supplied with an integer value. The 'd' flag (directory in this case) should be supplied with a string value. 

Once the schema has been specified, your args parser should accept the argument list. It should validate the args. Finally, your parser should expose a method that accepts a flag as a parameter and returns the corresponding value (ensuring it's the correct type).

### Default Values
If a flag mentioned in the schema is not present in args passed to the command line, your program should return a default according to the specified type (0 for integer, "" for string, ```false``` for boolean).

### Error Handling
Your program should take care to validate the provided args against the schema.

### Extension
Your program should make it staightforward and obvious how to add new types of values.

### Notes

1. The schema definition is left intentionally vague in this kata description. Designing a concise schema syntax is an important part of the exercise.
2. The order of the arguments does not need to match the order provided in the schema.

## Additional Requirement
Modify your program to support parsing lists. 

For example, if the schema specifies an integer list with a -l flag, it could be called as follows:

    -l 1,-2,3

Your parser should then return [1,-2,4] when the values for the -l flag are requested.