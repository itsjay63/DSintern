"""

The columns contain information about that game:

score_phrase — how IGN described the game in one word.
This is linked to the score it received.
title — the name of the game.
url — the URL where you can see the full review.
platform — the platform the game was reviewed on (PC, PS4, etc).
score — the score for the game, from 1.0 to 10.0.
genre — the genre of the game.
editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
release_year — the year the game was released.
release_month — the month the game was released.
release_day — the day the game was released.


"""


import pandas as pd

df = pd.read_csv('ign.csv')


##### games released for the Xbox One that have a score of more than 7
xbox_one_filter = (df["score"] > 7) & (df["platform"] == "Xbox One")
filtered_reviews = df[xbox_one_filter]
games_list_xbox_one = filtered_reviews['title']
print (games_list_xbox_one)


# review distribution for the Xbox One
xbox_one = df['platform']=="Xbox One"
xbox_one_only_df = df[xbox_one]
xbox_one_reviews = xbox_one_only_df['score_phrase']
xbox_one_reviews.hist(bins=20, grid=False, xrot=90)

# review distribution for the PlayStation 4
ps4 = df['platform']=="PlayStation 4"
ps4_only_df = df[ps4]
ps4_reviews = ps4_only_df['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90)


