# Terraform



## How to set it:
* [Part 1: DE Zoomcamp 1.3.1 - Introduction to Terraform Concepts & GCP Pre-Requisites](https://youtu.be/Hajwnmj0xfQ)

* [Part 2: DE Zoomcamp 1.3.2 - Creating GCP Infrastructure with Terraform](https://youtu.be/dNkEgO-CExg)

### References: 
* [Hashicorp - Build Infrastructure - Terraform GCP Example](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build)
* [Terraform - Getting Started with the Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)

### Project variables:
* Set ***provider "google" credentials*** -> Indicate path to json with GCP access key
* Set ***data_lake_bucket*** -> Bucket name
* Set ***variable "project" description*** -> Your GCP Project ID
* Set ***variable "region" default*** -> Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations
* Set ***variable "BQ_DATASET" default*** -> BigQuery Dataset that raw data (from GCS) will be written to


## Execution steps:

1. terraform init: 
   - Initializes & configures the backend, installs plugins/providers, & checks out an existing configuration from a version control
2. terraform plan: 
   - Matches/previews local changes against a remote state, and proposes an Execution Plan.
3. terraform apply: 
   - Asks for approval to the proposed plan, and applies changes to cloud
4. terraform destroy [^1]
   - Removes your stack from the Cloud
   
[^1]: Use ***terraform destroy*** at the end of sessions and the next time use ***terraform apply*** to continue. This avoids unsolicited costs.







