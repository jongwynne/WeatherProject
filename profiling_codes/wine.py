import pandas as pd
characternames = ['character_id', 'name', 'normalize','gender']
character = pd.read_table(r'C:\data\simpsons\simpsons_characters.csv', sep=',', header=None,names=characternames)
episodenames = ['episode_id', 'title', 'air_date', 'production_code', 'season', 'number_in_season', 'number_in_series', 'us_views', 'views', 'imbd_rating', 'imbd_votes', 'imageurl', 'videourl']
episode = pd.read_table(r'C:\data\simpsons\simpsons_episodes.csv', sep=',', header=None,names=episodenames)
locationnames = ['location_id', 'name', 'normalize']
location = pd.read_table(r'C:\data\simpsons\simpsons_locations.csv', sep=',', header=None,names=locationnames)
scriptnames = ['script_id', 'episode_id', 'number',	'raw_text', 'timestamp_in_ms', 'speaking_line', 'character_id', 'location_id', 'raw_character_text', 'raw_location_text', 'spoken_words', 'normalized_text', 'word_count']
script = pd.read_table(r'C:\data\simpsons\simpsons_script_lines.csv', sep=',', header=None,names=scriptnames)
print character
print episode
print script