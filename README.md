# Chips Programming Language
 
Chips is an esoteric programming language with gambling and resource management mechanics.

## Memory

## Bank

## Gambling

The only way to acquire more chips is by gambling on a simple dice game. The `WAGER` command will consume the entire stack of chips pointed to by the stack pointer. The total value of this stack will be your wager. Three seven-sided dice will be rolled, with the goal of rolling all sevens. The payouts for this game are as follows:

| # of Sevens | Probability | Payout      |
| :---------: | ----------- | ----------- |
| 0           | ~63.0%      | N/A         |
| 1           | ~31.5%      | WAGER × 2   |
| 2           | ~5.2%       | WAGER × 7   |
| 3           | ~0.3%       | WAGER × 777 |

Payouts are added directly to the bank.

## I/O
