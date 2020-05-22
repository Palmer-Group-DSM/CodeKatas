# Tennis Scoring Kata

## Objective
Write a program that keeps track of the score in a tennis game. The umpire will have a controller with 2 buttons: **Player One Scores** and **Player 2 Scores** 

You may assume that these buttons call a function in your code: ```playerScored("player1")``` or ```playerScored("player2")```

Your code should expose a method ```getScore()``` that returns a string representing the score.
## Background
*More at [Wikipedia](https://en.wikipedia.org/wiki/Tennis_scoring_system)*

| Point | Name    |
| ----- | ------- |
| 0     | Love    |
| 1     | Fifteen |
| 2     | Thirty  |
| 3     | Forty   |

The rules for scoring tennis are summarized below
1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent. The score is then “Win for player1” or “Win for player2”
2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as **“Love"**, **“Fifteen”**, **“Thirty”**, and **“Forty”** respectively. 
3. If at least three points have been scored by each player, and the scores are equal, the score is **“Deuce”**.
4.  If at least three points have been scored by each side and a player has one more point than his opponent,the score of the game is **“Advantage player1”** or **“Advantage player2”**.
## User Stories
### Feature: Winning a Point Increases Score Correctly
    As a library user  
    I want the score to increase when a player wins a point  
    So that I can display the current score correctly
    -------------------------------------------------------
    Given the score is $score
    When $player wins a point
    Then the score is $updatedScore
#### Test Cases
| score           | player  | updatedScore   |
| --------------- | ------- | -------------- |
| Love-Love       | player1 | Fifteen-Love   |
| Fifteen-Fifteen | player2 | Fifteen-Thirty |
| Thirty-Thirty   | player1 | Forty-Thirty   |
---
### Feature: Deuce and Advantage are Scored Correctly
    As a library user
    I want deuce and advantage to be scored correctly
    So that I can display the score correctly
    -------------------------------------------------------
    Given the score is $score
    When $player wins a point
    Then the score is $updatedScore
#### Test Cases
| score             | player  | updatedScore      |
| ----------------- | ------- | ----------------- |
| Thirty-Forty      | player1 | Deuce             |
| Forty-Forty       | player2 | Advantage player2 |
| Advantage player2 | player1 | Deuce             |
---
### Feature: Winning Points are Scored Correctly
    As a library user
    I want the winning point to be scored correctly
    So that I can display the winner
    -------------------------------------------------------
    Given the score is $score
    When $player wins a point
    Then the score is $updatedScore
#### Test Cases
| score             | player  | updatedScore    |
| ----------------- | ------- | --------------- |
| Thirty-Forty      | player2 | Win for player2 |
| Advantage player1 | player1 | Win for player1 |
