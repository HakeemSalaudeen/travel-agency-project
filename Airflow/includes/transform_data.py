from Airflow.includes.read_parquet_from_s3 import read_data_from_s3
import numpy as np
import logging

def transform_country_data():
    df = read_data_from_s3()
    
    # 1. Extract 'common' name - safely handle None values
    df['country_name'] = df['name'].apply(lambda x: x.get('common') if isinstance(x, dict) else None)
    
    # 2. Extract Official_country_name - safely handle None values
    df['Official_country_name'] = df['name'].apply(lambda x: x.get('official') if isinstance(x, dict) else None)

    # 3. Extract country code from 'idd' - safely handle None values
    def generate_country_codes(idd):
        if isinstance(idd, dict):
            root = idd.get('root', '')
            suffixes = idd.get('suffixes', [])
            if isinstance(suffixes, (list, np.ndarray)):
                return " ".join([root + suffix for suffix in suffixes])
        return None
    
    df['country_code'] = df['idd'].apply(lambda x: generate_country_codes(x))

    # 4. Extract capital safely
    df['capital'] = df['capital'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else x)

    # 5. Extract other required fields with safe fallbacks
    df['region'] = df['subregion']
    df['sub_region'] = df['subregion']
    df['area'] = df['area']
    df['population'] = df['population']
    df['continent'] = df['region']
    df['independence'] = df['independent']
    df['un_member'] = df['unMember']
    df['start_of_week'] = df['startOfWeek']

    # 6. Extract currency information safely
    def extract_first_non_none_currency(currencies):
        if not isinstance(currencies, dict):
            return None, None, None
        for code, details in currencies.items():
            if isinstance(details, dict):
                return code, details.get('name'), details.get('symbol')
        return None, None, None

    currency_info = df['currencies'].apply(extract_first_non_none_currency)
    df['currency_code'] = currency_info.apply(lambda x: x[0])
    df['currency_name'] = currency_info.apply(lambda x: x[1])
    df['currency_symbol'] = currency_info.apply(lambda x: x[2])

    # 7. Extract language information safely
    def extract_first_non_none_language(languages):
        if not isinstance(languages, dict):
            return None
        for lang, name in languages.items():
            if name is not None:
                return name
        return None

    df['language'] = df['languages'].apply(extract_first_non_none_language)

    # 8. Select only the relevant columns
    transformed_df = df[[
        'country_name', 'Official_country_name', 'country_code', 'capital',
        'region', 'sub_region', 'area', 'population', 'continent',
        'independence', 'un_member', 'start_of_week', 'currency_code',
        'currency_name', 'currency_symbol', 'language'
    ]]
    
    return transformed_df

logging.info(" data is transformed")
