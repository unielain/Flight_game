CREATE TABLE story(ch_id int(11) auto_increment primary key, character_name varchar(40), event varchar(40), dialog varchar(111));
CREATE TABLE inventory(id int(11) auto_increment primary key, item_id int(11), player_id int(11), status int(11), inventory int(11)); 
CREATE TABLE weather(id int(11) auto_increment primary key, name varchar(40), event varchar(40));
CREATE TABLE reach_event(id int(11) auto_increment primary key, location varchar(11), weather_name varchar(11));
ALTER TABLE game
ADD COLUMN(highscore float, password varchar(40));
ALTER TABLE inventory ADD CONSTRAINT play_id FOREIGN KEY (player_id) REFERENCES game(id) ON DELETE CASCADE;
ALTER TABLE game ALTER co2_budget SET DEFAULT 5000;
INSERT INTO story (character_name, event, dialog) VALUES ('Melon_Dusk', 'startscreen', 'dialog1.txt'), ('Melon_Dusk', 'same_screen_name', 'dialog_same_name.txt'), ('Melon_Dusk', 'newgamepassword', 'dialog_create_password.txt'), ('Melon_Dusk', 'newgametutorial', 'dialog_nightstand.txt'), ('Narrator', 'newgametutorial', 'narration_shady_figure1'), ('Shady_figure', 'newgametutorial', 'dialog_shady_figure1.txt'), ('Melon_Dusk', 'game_over', 'you_are_fired.txt'), ('Melon_Dusk', 'game_won', 'dialog_won_ephiphany.txt');
ALTER TABLE objects 
ADD COLUMN hint varchar(40); 
INSERT INTO objects (name, iso_country, hint) VALUES ('Koskenkorva', 'FI', 'hint_kossu.txt'), ('Hamburger', 'US', 'hint_burger.txt'), ('Crown', 'SE', 'hint_crown.txt'), ('Vodka', 'RU', 'hint_vodka.txt'), ('Ice-Hockey','CA','hint_hockey.txt'), ('Kangaroo', 'AU', 'hint_kangaroo.txt'), ('Bull', 'ES', 'hint_bull.txt'), ('BMW', 'DE', 'hint_DE.txt'), ('Baguette', 'FR', 'hint_baguette.txt'), ('Armor', 'GB', 'hint_armor.txt'), ('Holy_cow', 'IN', 'hint_holycow.txt'), ('ice_cube', 'IS', 'hint_icecube.txt'), ('pizza', 'IT', 'pizza_hint.txt'), ('tequila', 'MX', 'hint_tequila.txt'), ('salmon', 'NO', 'salmon_hint.txt'), ('feta_cheese', 'GR', 'hint_fetacheese.txt'), ('dragon', 'CN', 'hint_dragon.txt'), ('beef', 'AR', 'hint_penguin1.txt'), ('mummy', 'EG', 'hint_mummy.txt'), ('elephant_statue', 'TH', 'hint_elephantstatue.txt'), ('Durian_candy', 'SG', 'hint_durancandy.txt'), ('sedge_hat', 'VN', 'hint_sedgehat.txt'), ('diamond', 'ZA', 'hint_diamond.txt'), ('coffee', 'BR', 'hint_coffee.txt'), ('penguin', 'AQ', 'hint_penguin.txt'), ('rolex', 'CH', 'hint_rolex.txt'), ('Lego', 'DK', 'hint_BMW.txt'), ('water pipe', 'TR', 'hint_TR.txt'), ('Beads', 'RO', 'hint_ROM.txt'), ('AK-47', 'SY', 'hint_ak.txt');
ALTER TABLE weather 
ADD COLUMN co2_effect float;
INSERT INTO weather (name, event, co2_effect) VALUES ('clouds', 'nothing special happens', 0.0), ('clear', 'sun powers your aeroplane', -1000), ('mist', 'landing delayed', +200), ('smoke', 'flight made difficult', +1000), ('rain', 'minor incovenience', +50); 
