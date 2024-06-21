# Chips Programming Language
 
Chips is an esoteric programming language with gambling and resource management mechanics.

## Overview

### Memory

In Chips, data is represented by poker chips which are stored in an array of 777 unbounded stacks. Each chip stores one signed integer. There is also the hand, which can hold one chip, and can move chips between stacks.

### Bank

The bank is a finite resource used to create new chips. The bank has an initial value of 777. Creating a chip with the `DRAW n` command will reduce the value of the bank by abs(n). If the bank's value is ever negative, the program will immediately terminate.

### Gambling

The only way to acquire more chips is by gambling on a simple dice game. The `WAGER` command will consume the chip in hand. The value of this chip will be your wager. Three seven-sided dice will be rolled, with the goal of rolling all sevens. The payouts for this game are as follows:

| # of Sevens | Probability | Payout      |
| :---------: | ----------- | ----------- |
| 0           | ~63.0%      | N/A         |
| 1           | ~31.5%      | WAGER × 2   |
| 2           | ~5.2%       | WAGER × 7   |
| 3           | ~0.3%       | WAGER × 777 |

Payouts are added directly to the bank.

### I/O

A program can get input from stdin by using `DRAW ?`. This will get one character from stdin and create a chip with a value equal to the character's ASCII value.

The `EAT` command will consume the chip in the hand and output its ASCII value.

## Commands

| Name  | Parameters | Usage |
| ----- | ---------- | ----- |
| ADD   |       | Consume the chip in hand and the top of the active stack and create a chip in hand with their sum as a value. |
| BANK  |       | Return the chip in hand to the bank. |
| DRAW  | value | Creates a new chip in hand with the given value. If value is ?, get a character from stdin. |
| EAT   |       | Consume the chip in hand and output its ASCII value. |
| FLIP  |       | Negate the value of the chip in hand. |
| NEXT  |       | Increment the stack pointer. |
| POP   |       | Pop the top chip from the active stack and put it in the hand. |
| PREV  |       | Decrement the stack pointer. |
| PUSH  |       | Push the chip in hand onto the active stack. |
| SUB   |       | Consume the chip in hand and the top of the active stack and create a chip in hand with a value of (hand - top). |
| SWAP  |       | Swap the chip in hand with the top of the active stack. |
| WAGER |       | Gamble with the chip in hand as a wager. |
