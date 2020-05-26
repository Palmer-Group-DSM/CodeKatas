# Yatzy

## Background
Yatzy is a simple dice game that can be played by one or more players. Each player takes turns rolling five, 6-sided dice. After the first roll, each player can re-roll all or some of the dice up to two more times. After the roll is complete, the player assigns the roll in a category. According to the rules, if the roll is compatible with the category, then a score applies. If not, then the score for that roll is zero. 

**See below for the complete list of categories and scoring rules.** 

A full game consists of one go for each category. This means that once a roll is assigned to a category, the player cannot add or change that category for the remainder of that game. The last turn in the game has to be assigned to the remaining category.

*[Click here](http://en.wikipedia.org/wiki/Yatzy) for additional background information about the game.

## Your Task
Write a program that will score a *given* roll in a *given* category.

**\*Note:** 
- You do **not** need to program random dice rolling.
- The computer should **not** be choosing the highest scoring category for a given roll.

### Feature: Player rolls dice
```
As a player rolling the dice,
I want to place the roll in a category.
So that I can get a score.
```
```
Given player $roll
When assigned to $category
Then result is $score

```
## Categories & Scoring Rules

| Category | Rule | Example |
| -------- | ---- | ------- |
| Chance | Player scores the sum of all dice, regardless of what they read. | Roll : 5,4,1,4,2 placed on "chance" scores 16 (5+4+1+4+2). |
| Yatzy | All dice have the same number = 50 points | Roll : 5,5,5,5,5 placed on "yatzy" scores 50. <br><br>Roll : 5,5,5,5,**4** placed on "yatzy" scores 0. |
| Ones, Twos, Threes, Fours, Fives, Sixes | Player scores the sum of dice corresponding to the category it was placed on.| Roll : 5,4,1,4,2 placed on "fours" scores 8 (4 + 4). <br><br>The same roll placed on "threes" would score 0 because there are no threes in that roll.|
| Pair | Player scores the sum of the two highest matching dice. | Roll : 5,2,2,5,2 placed on "pair" scores 10 (5+5). <br><br>Roll : 2,2,3,2,2 placed on "pair" scores 4 (2+2).|
 | Two Pairs | Player rolls **two** pairs of dice with the same number - scores the sum of both pairs. If there are not two pairs of matching dice, and the roll is placed in this category, then the player scores 0. | Roll : 5,2,2,5,2 placed on "two pairs" scores 14 (5+5+2+2).<br><br> Roll : 2,2,3,2,2 placed on "two pairs" scores 0 (only one pair present). |
| Three of a kind | Player rolls three dice with same number - scores sum of the those three dice. If there are no three of a kind and the roll is placed in this category, then the player scores 0.| Roll : 5,2,2,5,2 placed on "three of a kind" scores 6 (2+2+2).<br><br> Roll : 2,2,2,5,2 placed on "three of a kind" scores 6 (2+2+2). |
| Four of a kind |  Player rolls four dice with same number - scores sum of the those four dice. If there are no four of a kind and the roll is placed in this category, then the player scores 0. | Roll : 3,3,3,5,3  placed on "four of a kind" scores 12 (3+3+3+3).<br><br> Roll: 3,3,3,3,3 placed on "four of a kind" scores 12 (3+3+3+3). |
| Small straight | Player rolls 1,2,3,4,5. Placed on "small straight" scores the sum of all dice. | Roll : 1,2,3,4,5 placed on "small straight" scores 15. |
| Large straight | Player rolls 2,3,4,5,6. Placed on "large straight" scores the sum of all dice. | Roll : 2,3,4,5,6 placed on "large straight" scores 20. |
| Full House | If the rolled dice are two of a kind and three of a kind, the player scores the sum of all the dice. | Roll : 3,3,4,4,4 placed on "full house" scores 18.<br><br> Roll : 1,1,2,2,3 placed on "full house" scores 0. <br><br>Roll : 1,1,1,1,1 placed on "full house" scores 0.