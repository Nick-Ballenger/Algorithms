#!/usr/bin/python

import argparse



def find_max_profit(price):
  bought_price=0
  sold_price =0
  max_profit = 0
  
  for i in range(len(price)-1):
    
    if  bought_price == 0 and price[i] < price[i+1]:
      bought_price = price[i]

    elif bought_price != 0 and price[i] > price[i+1]:
      if sold_price < price[i]:
        sold_price =  price[i]

  if bought_price == 0:
    bought_price =  price[-1]
  max_profit = sold_price - bought_price

  return max_profit




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))