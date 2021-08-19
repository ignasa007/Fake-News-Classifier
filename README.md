# Fake News Classifier
Welcome to our project for iNTUition 2021. We have a mobile application (developed in Flutter) which takes in a tweet link as the input, retrieves the tweet, scans for keywords, retrieves related articles from reliable news websites and reports agreement between the news articles and the headlines using a (self architectured) neural network. We have four categories for outputs:
1. agree - agreement between the article and the tweet
2. disagree - disagreement between the article and the tweet
3. discuss - news articles discusses what is being talked about in the tweet, but doesn't exactly take a stance
4. unrelated - news article is unrelated to the tweet 

## Dataset 
We used the dataset used for the FNC-1 (Fake News Challenge). The goal of the Fake News Challenge was to explore how artificial intelligence technologies, particularly machine learning and natural language processing, might be leveraged to combat the fake news problem. Check out the competition [here](http://www.fakenewschallenge.org/). The dataset can be downloaded [here](https://github.com/FakeNewsChallenge/fnc-1).

## Model
We first encode the text using the [word2vec](https://code.google.com/archive/p/word2vec/) embeddings. Google has published pre-trained vectors trained on part of Google News dataset (about 100 billion words). The model contains 300-dimensional vectors for 3 million words and phrases. The phrases were obtained using a simple data-driven approach described by [Mikolov, et. al., 2013](http://arxiv.org/pdf/1310.4546.pdf). The archive is available here: [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing).
We then process the embedding sequences for headlines and articles using a Deep 1D-CNN. We concatenate the encodings for these inputs and pass it through a feed-forward NN.

## Results
We achieved a 73.29% accuracy on 4-class classification task for the training set, and 70.47% on the test set.
