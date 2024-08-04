CREATE TABLE boardDB.boardinfo
(
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  matchId INTEGER NOT NULL AUTO_INCREMENT,
  roomId TEXT,
  player TEXT,
  boardNum TEXT,
  vul TEXT,
  auction TEXT,
  hands TEXT,
  play TEXT
)DEFAULT CHARACTER
  SET=utf8;

CREATE TABLE boardDB.matchinfo
(
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name TEXT,
  round TEXT,
  player TEXT,
  startBoard TEXT,
  lastBoard TEXT,
  teamOpen TEXT,
  teamOpenImp TEXT,
  teamClose TEXT,
  teamCloseImp TEXT,
)DEFAULT CHARACTER
  SET=utf8;