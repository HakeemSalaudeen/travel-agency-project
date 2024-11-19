import logging
import awswrangler as wr
from Airflow.includes.boto3session import aws_sesion


def read_data_from_s3():
    df = wr.s3.read_parquet(
        path = 's3://cde-hakeem-bucket/travel-agency',
        boto3_session=aws_sesion()
    )  
    return df 

logging.info(f" data is opened from S3")


