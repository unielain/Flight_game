CREATE TABLE story(ch_id int(11) auto_increment primary key, character_name varchar(40), event varchar(40), dialog varchar(111));
CREATE TABLE inventory(id int(11) auto_increment primary key, item_id int(11), player_id int(11), status int(11), inventory int(11)); 
CREATE TABLE weather(id int(11) auto_increment primary key, name varchar(40), event varchar(40));
CREATE TABLE reach_event(id int(11) auto_increment primary key, location varchar(11), weather_name varchar(11));
ALTER TABLE game
ADD COLUMN(highscore float, password varchar(40));
ALTER TABLE inventory ADD CONSTRAINT play_id FOREIGN KEY (player_id) REFERENCES game(id) ON DELETE CASCADE;
ALTER TABLE game ALTER co2_budget SET DEFAULT 5000;
