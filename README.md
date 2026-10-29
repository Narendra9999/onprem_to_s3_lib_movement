# Onprem to AWS S3 Library Movement using Jenkins CI/CD Pipeline
```

## Overview

Library Code Movement from Artifactory to S3 and Workspace is a framework build for deploying libraries and packages through Jenkins. It automates the entire process of deploying libraries and packages, ensuring consistency and reliability.

It uses a configuration-based approach for seamless deployment across work, non-production and production environments. By integrating with Jenkins for CI/CD, SonarQube for code quality checks, this framework ensures seamless deployment of libraries and packages across s3 buckets.

We need to make sure that we acquire SBC approval for the repective libraries and their version before migration.

```

# Scope
```

## Automation Scope

1. Developers make changes to the the config file and push the code to this BitBucket Repository
2. The Pipeline will be auto triggered once there is any PR merge
3. Code vulnerability and quality is monitored by SonarQube which is integrated with the Jenkins Pipeline
4. The repo code pull the libraries/packages from JFrog artifactory
5. The repo code will copy the libraries/packages on S3 bucket as per config file

```

# CI Configuration
```

## CI Config File Location

BitBucket Repo >> 103519-ONPREM-TO-S3-LIB-MOVEMENT/config/cicd-pipeline-config.json


## cicd-pipeline-config.json

sonar_project_version - version control for sonar
notification_mail_id - email id for notification email, it should be seperated by comma
destination_bucket_lib - target bucket name for libraries
destination_folder_lib_310 - target bucket location for libraries
destination_folder_lib_311 - target bucket location for libraries
destination_folder_lib_312 - target bucket location for libraries
destination_bucket_art - target bucket name for packages
destination_folder_art - target bucket location for packages

## cicd-runtime-config.json

run_artifact_migration - true if want to trigger artifact/package copy step in Jenkins pipeline
run_310_lib_migration - true if want to trigger 3.10 compatible library copy step in Jenkins pipeline
run_311_lib_migration - true if want to trigger 3.11 compatible library copy step in Jenkins pipeline
run_312_lib_migration - true if want to trigger 3.11 compatible library copy step in Jenkins pipeline

```

# Artifact/Library Specific Configuration
```

## files.json

Location: 103519-ONPREM-TO-S3-LIB-MOVEMENT/libraries_list/files.json
artifactory_full_path - Path of source artifact
extract - true if want to extract the file then copy

## python_310_package_registry.json

Location: 103519-ONPREM-TO-S3-LIB-MOVEMENT/libraries_list/python_310_package_registry.json
Libraries should be in the below format comma seperated. If want to overwrite then mention "overwrite": true. 
{
  "seaborn": { "version": "0.13.2", "overwrite": false }
}

## python_311_package_registry.json

Location: 103519-ONPREM-TO-S3-LIB-MOVEMENT/libraries_list/python_311_package_registry.json
Libraries should be in the below format comma seperated. If want to overwrite then mention "overwrite": true. 
{
  "tensorflow": { "version": "2.12.0", "overwrite": false },
  "torch": { "version": "1.13.0", "overwrite": false }
}

## python_312_package_registry.json

Location: 103519-ONPREM-TO-S3-LIB-MOVEMENT/libraries_list/python_312_package_registry.json
Libraries should be in the below format comma seperated. If want to overwrite then mention "overwrite": true. 
{
  "numpy": { "version": "2.3.1", "overwrite": false },
  "pandas": { "version": "2.3.0", "overwrite": false },
  "scipy": { "version": "1.16.0", "overwrite": false }
}



```
