#!/usr/bin/python

import sys

def making_change(amount, denominations):
  solutions = [0] * (amount + 1)
  solutions[0] = 1

  for coin in denominations:
    for bigger_coin in range(coin, amount + 1):
      leftover = bigger_coin - coin
      solutions[bigger_coin] += solutions[leftover]

  return solutions[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")