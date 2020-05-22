# Tennis Scoring Kata

## Objective
Write a program that keeps track of the score in a tennis game. The umpire will have a controller with 2 buttons: **Player One Scores** and **Player 2 Scores** 

You may assume that these buttons call a function in your code: ```playerScored("player1")``` or ```playerScored("player2")```

Your code should expose a method ```getScore()``` that returns a string representing the score.
## Background
*More at [Wikipedia](https://en.wikipedia.org/wiki/Tennis_scoring_system)*

| Points | Name    |
| ------ | ------- |
| 0      | Love    |
| 1      | Fifteen |
| 2      | Thirty  |
| 3      | Forty   |

The rules for scoring tennis are summarized below
1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent. The score is then “Win for player1” or “Win for player2”
2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as **“Love"**, **“Fifteen”**, **“Thirty”**, and **“Forty”** respectively. 
3. If at least three points have been scored by each player, and the scores are equal, the score is **“Deuce”**.
4.  If at least three points have been scored by each side and a player has one more point than his opponent,the score of the game is **“Advantage player1”** or **“Advantage player2”**.
