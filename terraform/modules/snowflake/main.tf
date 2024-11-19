resource "snowflake_database" "travel_agency_database" {
  name="travel-agency"
  drop_public_schema_on_creation=true
}

resource "snowflake_schema" "travel_agency_schema" {
  name     = "dboo"
  database = snowflake_database.travel_agency_database.name
}

resource "snowflake_file_format" "database_format" {
  name        = "parquet_file_format"
  database    = snowflake_database.travel_agency_database.name
  schema      = snowflake_schema.travel_agency_schema.name
  format_type = "parquet"
}