import pandas as pd
import torch

output_mapper = {"agree": 0, "disagree": 1, "discuss":2, "unrelated": 3}

def process_bodies(file_name):
    
    df = pd.read_csv(file_name, header = 0)
    dct = {row['Body ID']: row['Article Body'] for _, row in df.iterrows()}

    return dct

def process_stances(file_name):

    df = pd.read_csv(file_name, header = 0)
    lst = [tuple(row.tolist()) for _, row in df.iterrows()]

    return lst

def collate_fn(data, vecs = None):
    
    headlines = [x[0] for x in data]
    articles = [x[1] for x in data]
    stances = [x[2] for x in data]
    
    headlines_transformed = vecs.transform(headlines)
    articles_transformed = vecs.transform(articles)
    stances_transformed = torch.tensor([output_mapper[stance] for stance in stances])
    
    return headlines_transformed, articles_transformed, stances_transformed