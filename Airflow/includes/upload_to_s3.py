import logging
import awswrangler as wr
from Airflow.includes.boto3session import aws_sesion
from Airflow.includes.download_API_data import download_data

data = download_data()

def upload_to_s3():
    wr.s3.to_parquet(
        df=data,
        path="s3://cde-hakeem-bucket/travel-agency",
        boto3_session=aws_sesion(),
        mode='overwrite',
        dataset=True,
    )
logging.info("Data successfully uploaded to S3")