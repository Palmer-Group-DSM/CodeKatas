# Minesweeper

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
The player selects the square on a board. Board size is usually determined by level of difficulty. The selected square will reveal a number. This number represents how many mines are adjacent to the selected square.

> If a mine is revealed (detonated), then it is **game over**.

**Example: **

```
. . . . .
. * . . .
. . . . .
. . . . .
. . * . .

```