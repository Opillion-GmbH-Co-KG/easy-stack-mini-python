# EASY STACK PYTHON

## Introduction
This application is a versatile and comprehensive solution that provides a framework for various Docker containers. It can include different types of services, such as backends in Java or PHP, any kind of frontend, or even a complete Docker stack. Modify it to suit your needs. Check out our upcoming Easy-Stacks soon.
With this simple stack, you can build your own Docker images and publish them either locally or through GitHub pipelines. For your own Docker containers, you will need a registry such as Docker Hub or a similar option, like GitHub's container registry.

#### Caution! Caution! This stack is intended for development use only and is not configured for production. Please make sure to change all passwords immediately. You can override the values from the .env.dist file with a custom .env file. For production use, please refer to the "Easy-Stack-Prod" stack - comming soon.

## Installation and Starting the Application
### Prerequisites
- Docker and Docker Compose must be installed on the system.

#### Before you run this project, ensure the following are installed on your host system:

- Git
- Docker
- Docker Compose
- Make

#### Build this stack


Clone this Project

```sh
git clone git@github.com:Opillion-GmbH-Co-KG/easy-stack-python.git

cd ./easy-stack-python

 ```

To start and install this stack:

```sh
make start
 ```
or

```sh
make restart
```

## The stack up and running:
#### Simple Python App
![Alt text](.makefile/assets/python.png?raw=true" "Simple Python App")

### Docker Container
By default, the stack consists of a single Docker container. However, you can easily add additional containers to provide various services and extend the functionality of the stack. The main container and any additional containers you configure are described below:

### **Python**
- **Image:** `python:3.10`
- **Description:** A simple Python container based on a fixed Docker image with a preconfigured environment.
- **Ports (preconfigured):**
   - **${PYTHON_EXTERNAL_PORT}:${PYTHON_INTERNAL_PORT}** (Default: 8862:5000)
- **Name:** `python`
- **Volumes:**
   - `./python/app:/home/python`
- **User:** `python`


## This Stack is based on Easy Stack Mini

[![Easy Stack Mini - DALL-E Image](.makefile/assets/easy-stack-mini.jpg?raw=true)](https://github.com/Opillion-GmbH-Co-KG/easy-stack-mini)


