import json
import pickle
import numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_price(locations,sqft,bhk,bath):
    loc_index=__data_columns.index(location.lower())
    x = np.zeros(len(x.columns))
    x[0]=sqft
    x[1]=bhk
    x[2]=bath
    if loc_index >= 0:
         x[loc_index]=1
    return __model.predict([x])

def get_location_names():
     return __locations

def load_saved_artifacts():
     print('loading saved artifacts . . . start')
     global __data_columns
     global __locations

     with open("./artifacts/columns.json", 'r') as f:
         __data_columns = json.load(f) ['data_columns']
         __locations = __data_columns[3:]

     with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
          __model = pickle.load(f)
    
     print('Loading the artifacts . . . done')
        

if __name__=="__main__":
     load_saved_artifacts()
     print(get_location_names())