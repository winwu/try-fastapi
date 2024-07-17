# Try FastAPI

A simple project to get started with FastAPI.

## Environment Setup


```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For VSCode users, install the extension [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).


## Running Locally

Navigate to the app directory and run the application:


```sh
cd app
uvicorn main:app --reload

# in root folder
# uvicorn app.main:app --reload
```

To use SSL certificates:

```sh
uvicorn app.main:app --reload --ssl-keyfile credential/example.key --ssl-certfile credential/example.crt
```

Access the API documentation(swagger) at http://127.0.0.1:8000/docs.

## Running with docker

Generate SSL certificates in the credential directory:


```sh
# just example cli
cd credential
openssl req -new -newkey rsa:4096 -nodes -keyout example.key -out example.csr   
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt
```

Build and run the Docker container:

```sh
docker-compose up --build
docker-compose up
```

If you modify compose.yaml, rebuild the containers:

```sh
docker-compose build [nginx|fastapiweb]
```

### Access the Application

* via Uvicorn: http://localhost:9443/ 
* Via Nginx (after editing /etc/hosts): http://{custom_host} or https://{custom_host}
    * e.g. http://fastapi.winwu.dev (http://localhost) or https://fastapi.winwu.dev
    * Both 80 and 443 port are available


### Edit /etc/hosts

```sh
127.0.0.1 custom_host
# example
# 127.0.0.1 fastapi.winwu.dev
```