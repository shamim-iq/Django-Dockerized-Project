# Django Dockerized Project

This project demonstrates the setup and Dockerization of a Django web application. The goal is to check the running application on the public IP using Nginx as a reverse proxy. Then the application will be containerized and pushed to the Docker Hub for easy deployment.

## Prerequisites

- Docker installed
- Python installed
- Python-Pip installed
- Nginx installed

## Steps of Implementation

### Step 1: Create a new Django project
    pip install django
    django-admin startproject myproject
    cd myproject
    python3 manage.py startapp myapp

### Step 2: Edit the Nginx configuration file for the Django project (e.g., /etc/nginx/sites-available/default)

1. Update the Nginx configuration file with the following content:

    ```nginx
    server {
        listen 80;
        server_name <public_ip>;

        location / {
            proxy_pass http://<public_ip>:8080;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
    ```

2. Test Nginx configuration:

    ```bash
    sudo nginx -t
    ```

3. Reload Nginx:

    ```bash
    sudo nginx -s reload
    ```

4. Access the application on the `<Public_ip>` using a browser.

### Step 3: Dockerize the Django app

1. Create a Dockerfile in the project root with the provided content.

    ```dockerfile
    FROM python:3.10-slim

    COPY myproject /myproject

    WORKDIR /myproject

    EXPOSE 8000

    RUN pip install -r requirements.txt

    CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
    ```

2. Build the Docker image.

    ```bash
    docker build -t myproject-image .
    ```

### Step 4: Push Docker image to a registry

3. Tag the image.

    ```bash
    docker tag myproject-image:latest your-registry/myproject-image:latest
    ```

4. Login to Docker Hub.

    ```bash
    docker login
    ```

5. Push to Docker Hub.

    ```bash
    docker push your-registry/myproject-image:latest
    ```

### Step 5: Run Docker container and expose on port 8080

1. Run the Docker container.

    ```bash
    docker run -p 8080:8000 your-registry/myproject-image
    ```

2. Access the application on the `<Public_ip>:8000` using a browser.
