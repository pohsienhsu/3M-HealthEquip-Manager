# 3M HealthEquip Manager

3M HealthEquip Manager is a project that helps manage healthcare equipment information using AWS services. This project includes AWS Lambda functions, an RDS database, S3 bucket, Step Function, and a PowerShell script for interaction.

## Project Overview

- **Lambda Functions**: Implemented several Lambda functions:
  - `AddEquipment`: Adds new equipment information to the database.
  - `UpdateStatus`: Updates the status of equipment in the database.
  - `GetEquipmentInfo`: Retrieves equipment information from the database.

- **RDS Database**: Created an Amazon RDS database to store equipment and status information. The database is powered by MySQL.

- **S3**: Created a S3 bucket to store Python code and dependencies for the Lambda functions.

- **Step Function**: Integrated a State Machine to process potential user operations and decision flow.

- **PowerShell Script**: Provided a PowerShell script for user interaction. Clients/Users can use it to invoke Lambda functions and perform various actions.

## Prerequisites

Before running the project, ensure you have the following:

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured with appropriate permissions.
- [AWS Tools for PowerShell](https://aws.amazon.com/powershell/) module installed.
- AWS Lambda functions, RDS database, and S3 buckets provisioned (follow the provided CloudFormation templates).

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/3m-healthequip-manager.git`
2. Navigate to the project directory: `cd 3m-healthequip-manager`

## Usage

- Use the PowerShell script `healthquip.ps1` to interact with the project.
- Follow the prompts to choose options and interact with Lambda functions or Step Functions.

## AWS Resources

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon RDS](https://aws.amazon.com/rds/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon S3](https://aws.amazon.com/s3/)

