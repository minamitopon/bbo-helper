import os
import uuid
import re

def format_content(content):
  return re.sub("'", "", content)

def parse_match_info(content):
  """
  return datum to insert match table.

  Parameters
  ----------
  content: str
    context of vugraph file.

  Retruns
  -------
  result: tuple
    (
      name: str
      teamOpen: str
      teamClose: str
    )
  """

  match_info = content.split(',')
  name = re.sub('vg\|', '', match_info[0])
  team_open = match_info[5]
  team_close = match_info[7]
  return (name, team_open, team_close)

def parse_player_info(content):
  """
  return datum to insert player table.

  Parameters
  ----------
  content: str
    context of vugraph file.

  Retruns
  -------
  result: tuple
    (
      south_open: str,
      west_open: str,
      north_open: str,
      east_open: str,
      south_close: str,
      west_close: str,
      north_close: str,
      south_close: str
    )
  """
  players = re.search('(?<=pn\|)(.+?)(?=\|pg)', content)
  return tuple(players.group(0).split(','))

dir_path = '../sample/'
files = os.listdir(dir_path)

for file in files:
  with open(dir_path + file) as f:
    content = f.read()
    formated_content = format_content(content)
    # uuid = uuid.uuid4()

    print(parse_player_info(content))