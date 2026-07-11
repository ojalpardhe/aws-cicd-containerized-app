# Automated CI/CD Deployment of a Containerized Application on AWS

## Project Overview

This project demonstrates a complete DevOps CI/CD pipeline that automatically builds, tests, containerizes, and deploys a web application to a Kubernetes cluster.

The pipeline uses Jenkins to automate the software delivery process. Whenever code is pushed to GitHub, Jenkins checks out the latest code, builds the application, runs tests, creates a Docker image, pushes it to Amazon ECR, and deploys the latest version to Kubernetes.

## Technologies Used

- AWS EC2
- Amazon ECR
- Jenkins
- Docker
- Kubernetes
- Git & GitHub
- Python Flask
- AWS CLI
- kubectl

## Project Workflow

1. Developer pushes code to GitHub.
2. Jenkins detects the changes.
3. Jenkins builds and tests the application.
4. Docker image is created.
5. Docker image is pushed to Amazon ECR.
6. Kubernetes pulls the latest image.
7. The application is deployed automatically.

## Project Structure

```
aws-cicd-containerized-app/
│
├── app/
├── Dockerfile
├── Jenkinsfile
├── kubernetes/
├── README.md
└── screenshots/
```

## Author

Ojal Pardhe

Final Year B.Tech Student

DevOps Internship Project
