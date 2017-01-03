import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(r'C:\Git\pydata-book\ch02\movielens\users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(r'C:\Git\pydata-book\ch02\movielens\ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(r'C:\Git\pydata-book\ch02\movielens\movies.dat', sep='::', header=None, names=mnames)
# print users[:5]
# print ratings[:5]
# print movies[:5]
data = pd.merge(pd.merge(ratings, users), movies)
mean_rating = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_rating = mean_rating.ix[active_titles]
mean_rating['diff'] = mean_rating['M']-mean_rating['F']
top_female_ratings = mean_rating.sort_values(by='F', ascending=False)
sorted_by_diff = mean_rating.sort_values(by='diff')
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
print rating_std_by_title.order(ascending=False)[:10]
