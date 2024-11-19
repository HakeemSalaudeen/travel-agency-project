
import pandas as pd 
import logging


def download_data():
    url = "https://restcountries.com/v3.1/all"
    
    # Download the JSON data into a DataFrame
    df = pd.read_json(url)
    
    print("Data downloaded successfully.")
    return df

logging.info(f"API data downloaded successfully")
