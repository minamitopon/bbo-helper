import re
from collections import deque

def room(board):
  if room := re.search('(?<=qx\|)(.+?)(?=\|)', board):
    return room.group()

def board_number(board):
  if num := re.search('(?<=(qx\|[o|c]))(.+?)(?=\|st)', board):
    return num.group()

def hands(board):
  if hands := re.search('(?<=md\|)(.+?)(?=\|sv)', board):
    hand_list = hands.group().split(',')
    return list(map(sort, hand_list))

def sort(hand):
  irregal_char = re.compile('^.(?=[S|H|D|C])')
  trimIrregal_chars = irregal_char.sub('', hand)
  sorted_hand = deque(re.split('(?=[S|H|D|C])', trimIrregal_chars))
  sorted_hand.popleft()

  def symbol(suit):
    return re.sub('[S|H|D|C]', '', suit)

  return list(map(symbol, sorted_hand))