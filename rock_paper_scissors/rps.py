#!/usr/bin/python

import sys



def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  result = []
  players= [0]*n 
  create_rock_paper_scissors(players,0, result)
  return result




def create_rock_paper_scissors(array,index, outcome):


    if index == len(array):
        outcome.append(list(array))
        return array

    for item in ("rock","paper","scissors"):
        array[index] =item
        create_rock_paper_scissors(array,index+1, outcome)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')