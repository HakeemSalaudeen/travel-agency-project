import logging
import awswrangler as wr
from Airflow.includes.boto3session import aws_sesion
from Airflow.includes.transform_data import transform_country_data

def push_transform_data_to_S3():  
    data = transform_country_data()
    wr.s3.to_parquet(
            df=data,
            path="s3://cde-hakeem-bucket/travel-agency-transformed",
            boto3_session=aws_sesion(),
            mode='overwrite',
            dataset=True,
        )
    return ("Data successfully written to S3")

logging.info('Data successfully written to S3')