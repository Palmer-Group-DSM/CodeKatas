# Reversi

## Objective
Write a program that accepts an arbitrary Reversi board and a player as input, and determines all legal moves for that player.

## Background
> Learn more at [Wikipedia](https://en.wikipedia.org/wiki/Reversi)
> 
Reversi is a board game played by two players on an 8x8 board. Players take turn placing discs with their color (white or black) on open squares. A move is legal when a player places a disc with his color in a position where there is at least one straight (horizontal, vertical, or diagonal) occupied line between the new disc and another disc of your colour, with one or more contiguous pieces of the opponent’s colour between them. For example if we have a board like this:

> ```.``` represents an empty square  
> ```W``` represents a white disc  
> ```B``` represents a black disc
<pre>
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . W B . . .
. . . B W . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
</pre>
Then the legal moves for black are shown here with '*'
<pre>
. . . . . . . .
. . . . . . . .
. . . * . . . .
. . * W B . . .
. . . B W * . .
. . . . * . . .
. . . . . . . .
. . . . . . . .
</pre>
### Input Format
> **Note:** You may assume good input. Your program does not need to check the 
> board to determine if it's in a valid state.

Your program should input in the form of an 8x8 grid. A ```.``` character represents an empty square, a ```W``` character represents a square controlled by white, and ```B``` represents a square controlled by black. The current player will be given on the final line (W in the example).
<pre>
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . W B . . .
. . . B W . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
W
</pre>
### Output Format
Your program doesn't necessarily need to output data as shown in the examples above. Feel free to output coordinates, or to design some other data visualization format. 

