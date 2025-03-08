import pandas as pd

movies=pd.read_csv('movies.csv')
ratings=pd.read_csv('ratings.csv')

# print(mvs.head())
# print(rtgs.head())
# print(mvs.describe())
# print(rtgs.describe())

user_item_matrix=ratings.pivot_table(index='userId',columns='movieId',values='rating')
user_item_matrix=user_item_matrix.fillna(0)


#user similarity----Collaborative Filtering
from sklearn.metrics.pairwise import cosine_similarity
user_similarity=cosine_similarity(user_item_matrix)
user_similarity=pd.DataFrame(user_similarity,index=user_item_matrix.index,columns=user_item_matrix.index)


def recommmend_movies(user_id,used_similarity,user_item_matrix,movies,n_recommendations=5):
    sim_scores=user_similarity[user_id]
    similar_users=sim_scores.sort_values(ascending=False).index[1:n_recommendations+1]
    similar_users_ratings=user_item_matrix.loc[similar_users]
    target_user_ratings=user_item_matrix.loc[user_id]
    unrated_movies=target_user_ratings[target_user_ratings==0].index
    recommendations=similar_users_ratings[unrated_movies].mean().sort_values(ascending=False)
    return movies[movies['movieId'].isin(recommendations.index)].head(n_recommendations)
user_id=1
print(recommmend_movies(user_id,user_similarity,user_item_matrix,movies))

#Content Based Filtering
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
tfidf=TfidfVectorizer(stop_words='english')
movies['genres']=movies['genres'].fillna('')
tfidf_matrix=tfidf.fit_transform(movies['genres'])
cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx=movies[movies['title']==title].index[0]
    sim_scores=list(enumerate(cosine_sim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores=sim_scores[1:11]
    movie_indices=[i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]
print(get_recommendations('Toy Story (1995)'))
import joblib
joblib.dump(user_similarity,'user_similarity.pkl')
joblib.dump(user_item_matrix,'user_item_matrix.pkl')

