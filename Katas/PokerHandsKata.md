# Poker Hands
- [Poker Hands](#poker-hands)
  - [Objective](#objective)
  - [Background](#background)
    - [Hand Represenatation](#hand-represenatation)
    - [Poker Hands](#poker-hands-1)
    - [Input Format](#input-format)
    - [Output Format](#output-format)
  - [User Stories](#user-stories)
    - [Feature: Determine Winner Of A Poker Hand](#feature-determine-winner-of-a-poker-hand)
## Objective
Given input representing two poker hands, determine the winner.

## Background

### Hand Represenatation
We will use the following format to represent a poker hand:

    2C 3S 7H JC AH 

> (Two of Clubs, Three of Spades, Seven of Hearts, Jack of Clubs, Ace of Hearts)

The suit of the card is represented by one character:

|   H    |   S    |   C   |    D     |
| :----: | :----: | :---: | :------: |
| Hearts | Spades | Clubs | Diamonds |



The rank of the card is represented by one character - either the number on the card or one of the following special cases:
|   T   |   J   |   Q   |   K   |   A   |
| :---: | :---: | :---: | :---: | :---: |
|  Ten  | Jack  | Queen | King  |  Ace  |

### Poker Hands
Hands can be compared to determine a winner. This is done by categorizing each hand and seeing which hand has a higher rank. 

**The ranks are (in ascending order):**

- **High Card**: The value of the highest card in the hand. If the highest cards have the same value, the hands are ranked by the next highest, and so on. 
- **Pair**: 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair. If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order. 
- **Two Pairs**: The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair. Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining card. 
- **Three of a Kind**: Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards. 
- **Straight**: Hand contains 5 cards with consecutive values. Hands which both contain a straight are ranked by their highest card
- **Flush**: Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card. 
- **Full House**: 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.  
- **Four of a kind**: 4 cards with the same value. Ranked by the value of the 4 cards.
- **Straight flush**: 5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.

### Input Format
Your program should take a string containing ten cards as input: 

    2H 3D 5S 9C KD 2C 3H 4S 8C AH

The first five cards represent Player 1's hand, the second five cards represent Player 2's hand.

**NOTE**: You may assume good input. In other words, your program does not need to validate individual hands, nor does it need to validate the hands against eachother.

### Output Format
Your program should output one of the following: ```Player 1 Wins``` or ```Player 2 Wins```

## User Stories
### Feature: Determine Winner Of A Poker Hand
    As a library user  
    I want to know which player's hand has the higher rank
    So that I can determine the winner
    -------------------------------------------------------
    Given the hands are $cards
    Then the program output is $output

**Test Cases**

|             cards             |    output     |
| :---------------------------: | :-----------: |
| 2H 3D 5S 9C KD 2C 3H 4S 8C AH | Player 2 Wins |
| 2C 2H 4S 8C 8H QS 4D TC 4C KD | Player 1 Wins |
| 2H 9H 9S 9C 9D TH JH QH KH AH | Player 2 Wins |
| 2H 3H TH 9H QH 8C 3C 4C 6C 9C | Player 1 Wins |
