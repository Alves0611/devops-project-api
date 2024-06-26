module "kubernetes" {
  source       = "/home/gabriel/projects/terraform-aws-eks"
  cidr_block   = "10.34.0.0/16"
  service_name = "restapi"
  aws_region   = "us-east-1"
}
