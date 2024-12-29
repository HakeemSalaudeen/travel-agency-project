# to create a terraform state file and send it to s3 bucket
terraform {
  backend "s3" {
    bucket = "cde-hakeem-backend-bucket"
    region = "eu-central-1"
    key    = "cde/tfstate"
  }
}