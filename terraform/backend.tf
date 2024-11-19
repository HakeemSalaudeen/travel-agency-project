# terraform {
#   backend "s3" {
#     bucket = "cde-travel-agency-backend-bucket"
#     key    = "path/to/my/key"
#     region = "us-east-1"
#   }
# }


# to create a terraform state file and send it to s3 bucket
terraform {
  backend "s3" {
    bucket = "cde-hakeem-bucket"
    region = "eu-central-1"
    key    = "demo/tfstate"
  }
}
