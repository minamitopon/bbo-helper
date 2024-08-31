import re
from collections import deque

def room(board):
  if room := re.search('(?<=qx\|).(?=[0-9])', board):
    return room.group()
  else:
    return ''

def board_number(board):
  if num := re.search('(?<=\|[o|c])[0-9]+', board):
    return num.group()
  else:
    return ''

def hands(board):
  if hands := re.search('(?<=md\|)(.+?)(?=\|sv)', board):
    hand_list = hands.group().split(',')
    return list(map(sort, hand_list))
  else:
    return []

def sort(hand):
  irregal_char = re.compile('^.(?=[S|H|D|C])')
  trimIrregal_chars = irregal_char.sub('', hand)
  sorted_hand = deque(re.split('(?=[S|H|D|C])', trimIrregal_chars))
  sorted_hand.popleft()

  def symbol(suit):
    return re.sub('[S|H|D|C]', '', suit)

  return list(map(symbol, sorted_hand))

def auction(board):
  if auction := re.search('(?<=mb\|)(.+?)(?=\|pc)', board):
    return auction.group()
  else:
    return ''

def play(board):
  if play := re.search('(?<=pc\|)(.+?)(?=mc|pg\|\|pg)', board):
    return play.group()
  else:
    return ''

def total_trick(board):
  if tricks := re.search('(?<=mc\|)(.+?)(?=\|pg\|\|)', board):
    return tricks.group()
  else:
    return ''

def generate_board_record(board):
  return {
    'room': room(board),
    'board_num': board_number(board),
    'auction': auction(board),
    'play': play(board),
    'totalTrick': total_trick(board),
    'hands': hands(board)
  }