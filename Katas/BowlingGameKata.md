# Bowling Game Kata
- [Bowling Game Kata](#bowling-game-kata)
  - [Objective](#objective)
  - [Background](#background)
    - [Scoring an Open Frame](#scoring-an-open-frame)
    - [Scoring a Spare](#scoring-a-spare)
    - [Scoring a Strike](#scoring-a-strike)
    - [Final Frame Strike/Spare](#final-frame-strikespare)
  - [Input Data Format](#input-data-format)
    - [Sample Test Cases](#sample-test-cases)
      - [Note: You may assume good input data. More speciically, your program does not need to check for valid rolls or correct number of rolls and frames. It also does not need to allow calculating scores of intermediate frames.](#note-you-may-assume-good-input-data-more-speciically-your-program-does-not-need-to-check-for-valid-rolls-or-correct-number-of-rolls-and-frames-it-also-does-not-need-to-allow-calculating-scores-of-intermediate-frames)
## Objective
Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game.

## Background

([Check here for more detail](https://www.pba.com/Resources/Bowling101))

One line of bowling is composed of 10 frames. Each frame consists of 1 or 2 rolls. The players final score is calculated as the sum of their frame scores.

**Each frame will have one of three outcomes:**
1. After 2 rolls, there are pins standing (open frame)
2. After 2 rolls, there are no pins standing (spare)
3. After the first roll, there are no pins standing (strike)

### Scoring an Open Frame
The score for an open frame is equal to the number of pins knocked down.
### Scoring a Spare
When a player rolls a spare, the score for that frame is equal to 10 + the number of pins the player knocks down with their next roll (the first roll of the next frame). For example, imagine a player knocks down 9 pins with his first roll and 1 pin with his second roll. At the beginning of his next turn, he knocks down 5 pins. His score for the previous frame will be equal to 10 + 5 or 15.
### Scoring a Strike
Scoring a strike is similar to scoring a spare, except the player's next **two** rolls are added to the frame. For example, imagine a player rolls a strike. In her next frame, she knocks down 4 pins with her first roll and 3 pins with her second. Her score will be equal to 10 + 4 + 3 or 17.

### Final Frame Strike/Spare
If a player manages to roll a spare or a strike in the final frame, they are allowed to roll one or two more balls, respectively. These bonus balls are considered part of the final frame. If the player scores a strike on a bonus roll, it is simply treated as a value of 10 -- the process does not continue.

## Input Data Format
The input data will come in the form of a scorecard, with 'X' representing a strike, '/' representing a spare, and '-' representing no pins bowled.  
### Sample Test Cases
| Input                | Output |
| -------------------- | ------ |
| XXXXXXXXXXXX         | 300    |
| 123451624/4315813262 | 73     |
| 9999999999           | 90     |
| 3-537224-/8143X53X62 | 104    |

#### Note: You may assume good input data. More speciically, your program does not need to check for valid rolls or correct number of rolls and frames. It also does not need to allow calculating scores of intermediate frames.
