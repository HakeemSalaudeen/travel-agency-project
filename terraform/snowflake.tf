# Terraform configuration for Snowflake schema and database
resource "snowflake_database" "travel_agency_db" {
  name    = "TRAVEL_AGENCY_DB"
  comment = "Database for Travel Agency Project"
}

resource "snowflake_schema" "travel_agency_schema" {
  database = snowflake_database.travel_agency_db.name
  name     = "TRANSFORMED_STAGE"
  comment  = "Schema for transformed staged data"
}

# Create a file format for Parquet files
resource "snowflake_file_format" "parquet_file_format" {
  name     = "PARQUET_FILE_FORMAT"
  database = snowflake_database.travel_agency_db.name
  schema   = snowflake_schema.travel_agency_schema.name
  format_type   = "PARQUET"
  comment = "File format for Parquet files"
}

variable "TF_VAR_example_aws_key_id" {
    type        = string
}

variable "TF_VAR_example_aws_secret_key" {
    type        = string
}

resource "snowflake_stage" "s3_stage" {
    name        = "S3_TRAVEL_STAGE"
    database    = snowflake_database.travel_agency_db.name
    schema      = snowflake_schema.travel_agency_schema.name
    url         = "s3://cde-hakeem-datalake-bucket/travel-agency-transformed/04736265464247a9a2c193977ec3cc3c.snappy.parquet"
    credentials = <<EOF
    AWS_KEY_ID='${var.TF_VAR_example_aws_key_id}'
    AWS_SECRET_KEY='${var.TF_VAR_example_aws_secret_key}'
    EOF
}

resource "snowflake_table" "travel_agency_table" {
  database                    = snowflake_database.travel_agency_db.name
  schema                      = snowflake_schema.travel_agency_schema.name
  name                        = "TRAVELS"
  comment                     = "TRAVEL AGENCY TABLE."


   column {
    name     = "DATA"
    type     = "VARIANT"
    nullable = false
  }
}
