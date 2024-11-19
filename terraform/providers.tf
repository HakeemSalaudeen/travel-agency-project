# Configure the AWS Provider
provider "aws" {
  region     = "eu-central-1"
}


terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
    }
  }
}

provider "snowflake" {
  organization_name = "VAKMCIY"
  account_name      = "MM09247"
  user              = "Hakeem"
  password          = "Salaudeen001"

  // optional
  role      = "ACCOUNTADMIN"
  warehouse = "compute_warehouse"
}