import re
import string
import os

import torch

from .contractions import contractions_dict
from .vectors import GoogleVec
from .model import Model

cwd = os.getcwd()
path_to_states = '.\model\model_states'
path_to_vecs = '.\model\data'

model = Model()
model.load_state_dict(torch.load(os.path.join(cwd, path_to_states, 'state_dict.pt')))
vecs = GoogleVec(path = os.path.join(cwd, path_to_vecs, 'GoogleNews-vectors-negative300.bin'))


def process(tweet, articles):

    tweet = clean(tweet)
    tweet_transformed = vecs.transform(list(tweet))
    
    output = []

    for a in articles:

        article = clean(a['text'])
        del a['text']
        article_transformed = vecs.transform(list(article))

        probs = model(tweet, article).squeeze().tolist()
        a['probs'] = probs
        output.append(a)

    return output


def clean(tweet):

    tweet = ' '.join(re.sub('(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)', ' ', tweet).split())
    tweet = ' '.join(re.sub('(\w+:\/\/\S+)', ' ', tweet).split())
    tweet = ' '.join(re.sub(string.punctuation, ' ', tweet).split())
    tweet = tweet.lower()
    tweet = ' '.join([word 
                      if word not in contractions_dict \
                      else                             \
                      contractions_dict[word]          \
                      for word in tweet.split()])
    tweet = tweet.encode(encoding = 'utf-8').decode()

    return tweet