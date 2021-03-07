import pickle

with open('trainBodies.pickle','rb') as handle:
    trainBodies = pickle.load(handle)
    
with open('testBodies.pickle','rb') as handle:
    testBodies = pickle.load(handle)
   
with open('trainStances.pickle','rb') as handle:
    trainStances = pickle.load(handle)
   
with open('testStances.pickle','rb') as handle:
    testStances = pickle.load(handle)
   