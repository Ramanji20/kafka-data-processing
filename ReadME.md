# Kafka Data Processing Application

## Overview

This application is designed to consume messages from a Kafka topic (`user-login`), process the data, and produce the processed data to another Kafka topic (`processed-user-login`). The application is containerized using Docker and orchestrated with Kubernetes to ensure scalability and reliability in a production environment.

## Table of Contents

- [Kafka Data Processing Application](#kafka-data-processing-application)
  - [Architecture](#architecture)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Configuration](#configuration)
    - [Run Docker](#run-docker)
    - [Run Python Consumer](#run-python-consumer)
  - [Conclusion](#conclusion)

## Architecture

- **Kafka**: Message broker to handle the streaming data.
- **Zookeeper**: Service that manages and coordinates Kafka brokers.
- **Python Consumer**: Consumes messages from `user-login`, processes the data, and produces the processed data to `processed-user-login`.
- **Docker**: Containerization platform to package the application.
- **Kubernetes**: Orchestration platform to manage and scale the containers.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Kubernetes (Minikube, k3s, or a cloud provider's Kubernetes service)
- Confluent Kafka Python Client Library (`confluent_kafka`)

### Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/Ramanji20/kafka-data-processing.git
   cd kafka-data-processing
   ```

2. **Install Python Dependencies**:

   ```sh
   pip install confluent_kafka
   ```

## Configuration

Ensure the environment variables for Kafka brokers and topics are set correctly. Update the `docker-compose.yml` and Kubernetes manifests as needed.

### Run Docker

- Make sure docker is up and running
- Go to terminal on the cloned folder

  ```sh
  docker-compose up
  ```

### Run Python Consumer

- As we are done with docker run which produces the data flow, lets run python consumer
- Run Python consumer from the terminal as follows

  ```sh
  python3 kcp.py
  ```

## Conclusion

After running docker and python, we can observe in the terminal that `kcp.py` is streamlining the data as follows

