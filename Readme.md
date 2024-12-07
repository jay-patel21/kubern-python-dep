# GKE Deployed Application with NGINX Frontend, Flask Backend, GCP Bucket, and PostgreSQL DB

## Project Overview

This project consists of a frontend application served by NGINX and a backend powered by Flask. Both services are deployed on **Google Kubernetes Engine (GKE)**. The application also integrates the functionality to upload files to a **Google Cloud Storage Bucket**, and it connects to a **PostgreSQL** database hosted on **Google Cloud Platform (GCP)**.

### Key Features

- **Frontend**: A static frontend served by NGINX.
- **Backend**: A Flask API to handle business logic.
- **File Upload**: Users can upload files to a GCP bucket via the Flask backend.
- **Database**: PostgreSQL database hosted on GCP for persistent data storage.

## Architecture

The application is composed of the following components:

1. **Frontend (NGINX)**:
   - Serves static assets for the application.
   - Runs inside a Docker container.
   
2. **Backend (Flask)**:
   - Provides APIs for the frontend and handles file upload requests.
   - Handles interactions with GCP services (Cloud Storage and PostgreSQL).
   - Runs inside a Docker container.

3. **Google Cloud Storage Bucket**:
   - Used to store uploaded files.
   
4. **PostgreSQL Database**:
   - Stores structured application data.
   
5. **Google Kubernetes Engine (GKE)**:
   - Hosts the frontend and backend services in containers.
   - Manages scaling and networking.

## Technologies Used

- **Frontend**: NGINX
- **Backend**: Flask (Python)
- **File Storage**: Google Cloud Storage
- **Database**: PostgreSQL (GCP)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (GKE)

## Prerequisites

- Google Cloud Platform account
- `gcloud` CLI installed
- Docker installed
- Kubernetes (`kubectl`) installed
- Access to a PostgreSQL instance on GCP
- A GCP Storage Bucket

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jay-patel21/kubernetes-python.git
cd kubernetes-python

