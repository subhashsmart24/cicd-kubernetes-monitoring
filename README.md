# End-to-End CI/CD Pipeline and Kubernetes Monitoring

## Overview

This project demonstrates a CI/CD pipeline for a Flask application using Docker, GitHub Actions, Amazon ECR, Kubernetes (Minikube), Prometheus, and Grafana.

It automates application testing, security scanning, Docker image building, and pushing images to Amazon ECR. The application runs on Minikube, with Prometheus and Grafana providing monitoring and visualization.

## Architecture

**CI/CD Pipeline:**

Developer → GitHub → GitHub Actions → Automated Tests → Trivy Security Scan → Docker Build → Amazon ECR

**Deployment and Monitoring:**

Amazon ECR → Kubernetes (Minikube) → Prometheus → Grafana

**Note:** The current GitHub Actions workflow does not automatically deploy new images to Kubernetes. Kubernetes deployment and updates are managed separately.

## Technologies

* Python and Flask
* Docker
* Git and GitHub
* GitHub Actions
* Trivy vulnerability scanning
* Amazon Elastic Container Registry (ECR)
* Kubernetes and Minikube
* Helm
* Prometheus
* Grafana
* AWS IAM and GitHub OIDC

## Application Endpoints

| Endpoint   | Purpose                                    |
| ---------- | ------------------------------------------ |
| `/`        | Displays application information           |
| `/health`  | Provides a health check                    |
| `/metrics` | Exposes application metrics for Prometheus |

## CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

1. Checks out the source code.
2. Installs dependencies and runs application tests.
3. Performs a Trivy filesystem security scan.
4. Authenticates to AWS using GitHub OIDC.
5. Logs in to Amazon ECR.
6. Builds the Docker image.
7. Pushes the image to Amazon ECR using commit-based and `latest` tags.

The pipeline runs on pushes and pull requests to the `main` branch. The image-publishing job runs only on pushes to `main`, after the test job succeeds.

## Kubernetes Deployment

Kubernetes manifests are maintained in `kubernetes/base/`.

The Flask application is deployed to Minikube and exposed through a Kubernetes NodePort service.

The deployment includes health checks to help Kubernetes determine whether the application is ready and running correctly.

**Deployment limitation:** The current GitHub Actions workflow publishes Docker images to Amazon ECR but does not automatically update the Minikube deployment. Deploying a new image requires a separate Kubernetes update process.

## Monitoring

Prometheus collects application metrics, including:

* Total HTTP requests
* HTTP request duration
* Application target availability

Grafana uses Prometheus as its data source to visualize application performance through a dashboard containing:

* Application HTTP request counts
* HTTP request rate
* 95th-percentile response time
* Application target health

## Run Locally

### Prerequisites

* Docker Desktop
* Minikube
* kubectl
* Helm
* Git

### Start Minikube

```powershell
minikube start --driver=docker
```

### Check Kubernetes Pods

Check the application pods:

```powershell
kubectl get pods
```

Check the monitoring pods:

```powershell
kubectl get pods -n monitoring
```

### Access Prometheus

Run this command in a terminal and keep the terminal open:

```powershell
kubectl port-forward -n monitoring service/prometheus-server 9090:80
```

Open the following address in your browser:

`http://localhost:9090`

### Access Grafana

Run this command in a separate terminal and keep it open:

```powershell
kubectl port-forward -n monitoring service/grafana 3000:80
```

Open the following address in your browser:

`http://localhost:3000`

Sign in using your configured Grafana credentials.

## Important Notes

* AWS resources may incur charges depending on usage and account eligibility.
* Prometheus and Grafana persistence is disabled in this local demonstration. Monitoring data may not survive pod recreation or restarts.
* Port-forwarding sessions must remain active while accessing Prometheus and Grafana through the local addresses.
* Do not commit AWS credentials, passwords, access tokens, or other secrets.
* The Kubernetes deployment is managed separately from the current GitHub Actions image-publishing workflow.

## Project Outcome

This project demonstrates practical experience with:

* CI/CD pipeline implementation
* Automated application testing
* Containerization with Docker
* Vulnerability scanning with Trivy
* AWS authentication using GitHub OIDC
* Docker image publishing to Amazon ECR
* Kubernetes application deployment using Minikube
* Prometheus metrics collection
* Grafana dashboard creation and monitoring
