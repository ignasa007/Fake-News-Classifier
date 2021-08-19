import gensim
import torch
import string


class GoogleVec(object):
    

    def __init__(self, path = './GoogleNews-vectors-negative300.bin'):

        self.model = gensim.models.KeyedVectors.load_word2vec_format(path, unicode_errors = 'ignore', binary = True)
        self.vocab = set(self.model.index_to_key)
        self.dct = {c: '' for c in string.punctuation.replace('.', '')}

    def transform(self, X, pad = 0):

        embeddings = []
        max_len = 0

        for x in X:

            table = x.maketrans(self.dct)
            x = x.translate(table) 
            v = self.vectorize(x)
            max_len = max(max_len, v.shape[-1])
            embeddings.append(v)

        padded_embeddings = torch.full(size = (len(X), self.model.vector_size, max_len), \
                                       fill_value = pad,                                 \
                                       dtype = torch.float)

        for i, v in enumerate(embeddings):

            padded_embeddings[i, :, :v.shape[-1]] = v
            
        return padded_embeddings

    def vectorize(self, text):
    
        words = [word for word in text.split() if word]
        w_idx = 0
        vectorized = []

        while w_idx < len(words):

            w0 = words[w_idx]
            w1 = words[w_idx+1] if w_idx+1 < len(words) else False
            w2 = words[w_idx+2] if w_idx+2 < len(words) else False

            if w2:
                s = '_'.join([w0, w1, w2])
                if s in self.vocab:
                    vectorized.append(self.model[s])
                    w_idx += 3
                    continue

            if w1:
                s = '_'.join([w0, w1])
                if s in self.vocab:
                    vectorized.append(self.model[s])
                    w_idx += 2
                    continue

            if w0 in self.vocab:
                vectorized.append(self.model[w0])
            elif w0.lower() in self.vocab:
                vectorized.append(self.model[w0.lower()])
            else:
                vectorized.append(self.model['</s>'])
            w_idx += 1
        
        return torch.tensor(vectorized, dtype = torch.float).transpose(0, 1)


if __name__ == '__main__':

    v = GoogleVec()
    print(v.transform(['iNTUition project', 'fake news detection']))