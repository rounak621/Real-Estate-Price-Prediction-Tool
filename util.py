import json
import pickle
import numpy as np

# Global variables to store model, columns, and locations
__locations = None
__data_columns = None
__model = None

def get_location_names():
    """
    Returns the list of locations from the dataset.
    """
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    """
    Predicts the estimated price for a given set of parameters.
    """
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    # Create the feature array with zeros for all columns
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # Predict the price and round it
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    """
    Loads the saved model and column information from artifacts.
    """
    global __data_columns
    global __locations

    # Load columns information (for locations and feature columns)
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Locations are stored from index 3 onwards

    # Load the saved model (the pre-trained machine learning model for price prediction)
    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
