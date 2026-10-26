# End-to-End CI/CD Pipeline and Kubernetes Monitoring

## Overview

This project demonstrates an end-to-end CI/CD workflow for a Flask application using Docker, GitHub Actions, Amazon ECR, Kubernetes (Minikube), Prometheus, and Grafana.

## Architecture

Developer → GitHub → GitHub Actions → Tests → Trivy Security Scan → Docker Build → Amazon ECR → Kubernetes (Minikube) → Prometheus → Grafana

## Technologies

* Python and Flask
* Docker
* Git and GitHub
* GitHub Actions
* Trivy vulnerability scanning
* Amazon ECR
* Kubernetes and Minikube
* Prometheus
* Grafana

## Application Endpoints

* `/` — Application information
* `/health` — Health check
* `/metrics` — Prometheus metrics

## CI/CD Pipeline

The GitHub Actions workflow:

1. Checks out the repository.
2. Runs application tests.
3. Performs a Trivy filesystem security scan.
4. Authenticates to AWS using GitHub OIDC.
5. Builds and pushes the Docker image to Amazon ECR.

## Kubernetes Deployment

Kubernetes manifests are stored in `kubernetes/base/`.

The application is deployed to Minikube and exposed through a Kubernetes NodePort service.

## Monitoring

Prometheus collects application metrics, including:

* Total HTTP requests
* Request duration
* Application target availability

Grafana visualizes application request counts, request rate, response time, and application health.

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

```powershell
kubectl get pods
kubectl get pods -n monitoring
```

### Access Prometheus

Run this command in a terminal and keep it open:

```powershell
kubectl port-forward -n monitoring service/prometheus-server 9090:80
```

Open `http://localhost:9090` in your browser.

### Access Grafana

Run this command in a separate terminal and keep it open:

```powershell
kubectl port-forward -n monitoring service/grafana 3000:80
```

Open `http://localhost:3000` in your browser.

## Important Notes

* AWS resources may incur charges depending on usage and account eligibility.
* Prometheus and Grafana persistence is disabled in this local demonstration.
* Do not commit AWS credentials, passwords, or other secrets.
