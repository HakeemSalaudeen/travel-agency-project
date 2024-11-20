## Step 1 : Import module/operator
from airflow import DAG 
from airflow.utils.dates import datetime
from airflow.operators.python import PythonOperator
from Airflow.includes.upload_to_s3 import upload_to_s3
from Airflow.includes.transformed_data_to_S3 import push_transform_data_to_S3
import logging

  #Instantiate a DAG object;                                
with DAG(
    dag_id= "TravelAgency",        
    description = 'CDE Capstone Project',                               
    start_date= datetime(2024, 10, 13),                             
    schedule_interval= None,                                        
    catchup=False,
) as dag:
      
# python operator to upload to s3          
    S3Put = PythonOperator(
    task_id = 'S3Put',
    python_callable=upload_to_s3
    )
    
# python operator to pussh transformed data back to S3
    S3Push = PythonOperator(
    task_id = 'S3Push',
    python_callable=push_transform_data_to_S3
    )
    
    logging.info(" data pushed to S3 bucket")


S3Put >> S3Push 
