resource "aws_s3_bucket" "travel-agency-datalake" {
  bucket = "cde-hakeem-datalake-bucket"

  tags = {
    Name        = "travel-agency"
    Environment = "travel-agency"
  }
}


# resource "aws_s3_bucket" "travel-agency-backend" {
#   bucket = "cde-hakeem-backend-bucket"

#   tags = {
#     Name        = "travel-agency"
#     Environment = "travel-agency"
#   }
# }