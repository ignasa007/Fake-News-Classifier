from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import pickle

transformer = "msmarco-distilbert-base-v2"
encoder = SentenceTransformer(transformer)

train_bodies = pd.read_csv("validate\data\processed\\test_bodies.csv", header=0)
train_stances = pd.read_csv("validate\data\processed\\train_stances.csv", header=0)
test_bodies = pd.read_csv("validate\data\processed\\test_bodies.csv", header=0)
test_stances = pd.read_csv("validate\data\processed\\test_stances.csv", header=0)

def encodeTweet(tweet):
    tweet_encoding = encoder.encode(tweet)
    return tweet_encoding

def encodeArticle(article):
    sentences = article.split(", ")
    encoded_input = np.array([encoder.encode(sentence) for sentence in sentences])
    return encoded_input

train_bodies_dict = {}
for index,row in train_bodies.iterrows():
    train_bodies_dict[int(row['Body ID'])] = encodeArticle(row['articleBody'])
with open('trainBodies.pickle','wb') as handle:
    pickle.dump(train_bodies_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
  
    
test_bodies_dict = {}
for index,row in test_bodies.iterrows():
    test_bodies_dict[int(row['Body ID'])] = encodeArticle(row['articleBody'])  
with open('testBodies.pickle','wb') as handle:
    pickle.dump(test_bodies_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


train_stances_list = []
for index,row in train_stances.iterrows():
    # train_stances_dict[int(row['Body ID'])] = {'Headline':encodeTweet(row['Headline']), 'Stance':row['Stance']}
    train_stances_list.append(int(row['Body ID']),encodeTweet(row['Headline']), row['Stance'])
with open('trainStances.pickle','wb') as handle:
    pickle.dump(train_stances_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

test_stances_list = []
for index,row in test_stances.iterrows():
    # test_stances_dict[int(row['Body ID'])] = {'Headline':encodeTweet(row['Headline']), 'Stance':row['Stance']}
    test_stances_list.append(int(row['Body ID']),encodeTweet(row['Headline']), row['Stance'])
with open('testStances.pickle','wb') as handle:
    pickle.dump(test_stances_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

