import torch
import torch.nn as nn


class Model(nn.Module):
    
    
    def __init__(self, embedding_dim = 300,  \
                       n_hidden = 256,       \
                       pool_kernel_size = 2, \
                       dropout_rate = 0.5):
        
        super(Model, self).__init__()
        
        in_channels = [embedding_dim, n_hidden, n_hidden, n_hidden*2, n_hidden*2]
        out_channels = [n_hidden, n_hidden, n_hidden*2, n_hidden*2, n_hidden*3]
        filter_sizes = [3, 3, 3, 3, 3]
        strides = [1, 1, 1, 1, 1]
        paddings = [3, 3, 3, 1, 1]
        dense_sizes = [n_hidden*3*2, n_hidden*4, n_hidden*4, n_hidden*4, 4]
        
        conv_layers = [nn.Conv1d(*params) for params in \
                       zip(in_channels, out_channels, filter_sizes, strides, paddings)]
        pool_layers = [nn.MaxPool1d(pool_kernel_size) for _ in range(3)]
        relu = nn.ReLU()
        dropout = nn.Dropout(dropout_rate)
        
        self.cnn = nn.Sequential(conv_layers[0], relu, pool_layers[0], \
                                 conv_layers[1], relu, pool_layers[1], \
                                 conv_layers[2], relu, pool_layers[2], \
                                 conv_layers[3],                       \
                                 conv_layers[4])
        
        self.dnn = nn.Sequential(*[nn.Linear(in_size, out_size) \
                                   for in_size, out_size in     \
                                   zip(dense_sizes[:-1], dense_sizes[1:])])
        
        self.softmax = nn.Softmax(dim = -1)

    def forward(self, headlines, articles):
        
        headlines = self.cnn(headlines)
        headlines, _ = torch.max(headlines, axis = -1)
        
        articles = self.cnn(articles)
        articles, _ = torch.max(articles, axis = -1)
        
        dense_vec = torch.cat((headlines, articles), axis = -1)
        out = self.dnn(dense_vec)
        probs = self.softmax(out)
        
        return probs