# Minesweeper

## Table of Contents
- [Minesweeper](#minesweeper)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Objective](#objective)
  - [How it works](#how-it-works)
  - [Requirements](#requirements)
    - [Acceptance test input:](#acceptance-test-input)
    - [Output:](#output)
## Background
Minesweeper is a puzzle game for a single-player. It originated in the 1960s and has been adapted for many computing platforms since then. Some of the adaptations have boards that will never reveal a mine on the first square chosen. 

Originally, there were three levels of difficulty with corresponding board sizes.

| Difficulty | Board Size |
|----------- | ---------- |
| Beginner | 8 x 8 |
| Intermediate | 9 x 9 |
| Expert | 10 x 10 |


## Objective

The objective of the game is to find all of the mines within the board without detonating them. 

## How it works
The player selects the square on a board. Board size is usually determined by level of difficulty. The selected square will reveal a number hint. This number represents how many mines are adjacent to the selected square.

> If a mine is revealed (detonated), then it is **game over**.

**Example:**

```
A 5x5 board with two mines( mine = *): 

. . . . .
. * . . .
. . . . .
. . . . .
. . * . .

```
```
The same board with number hints: 

1 1 1 0 0
1 * 1 0 0
1 1 1 0 0
0 1 1 1 0
0 1 * 1 0

```

## Requirements
**Input requirements:**
- Input consists of an arbitrary number of fields.
- The first line of each field contains two integers: **n and m**.
  - Represent the number of lines and columns respectively.
  - 0 < n, m <= 100
- The next **n** lines contain exactly **m** characters.
  - Represent the field.
- Safe square (no mine found there) = **.** ( dot character )
- Mine square = **\*** ( asterisk )
- First field line where **n = m = 0** 
  - Signals end of input.
  - Should not be processed.

**Output Requirements:**
- Message printed in a line alone for each field:
  - **Field <sup>#</sup>x**
  - x represents the number of the field (beginning at 1).
  - The following n lines should contain the field with the dot characters replaced by the number of adjacent mines to that square.
  - There must be an empty line between field outputs.

### Acceptance test input: 
```
5 5
. . . . .
. * . . .
. . . . .
. . . . .
. . * . .
3 5
. . * . .
. . . . .
* . . . .
0 0
```
###    Output:

```
Field #1
1 1 1 0 0
1 * 1 0 0
1 1 1 0 0
0 1 1 1 0
0 1 * 1 0

Field #2
0 1 * 1 0
2 2 1 1 0
* 1 0 0 0

```

**Note:** 
- Think about the benefits/detriments of the datastructure you choose to store the minefield in.


Good luck and have fun!