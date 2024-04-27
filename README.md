# Try fastapi

## about env

Python 3.9, venv... etc.

- please ref requirements.txt
- if using vscode, please install [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)


## Developing in local

```
cd ~./
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```jsonc
cd app
uvicorn main:app --reload

// or 

uvicorn app.main:app --reload

// or run with ssl cert
uvicorn app.main:app --reload --ssl-keyfile credential/example.key --ssl-certfile credential/example.crt
```

visit swagger index

```
http://127.0.0.1:8000/docs
```


## Developing in docker

### Generate ssl cert, key and csr under "credential" folder

```
# just example cli:
cd credential
openssl req -new -newkey rsa:4096 -nodes -keyout example.key -out example.csr   
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt
```

### build image and container

```
docker-compose up --build
```

```
# run
docker-compose up
```

```
# if you make some changes in compose.yaml

docker-compose build [nginx|fastapiweb]
```

### Visit web which is served by uvicorn

* http://localhost:9443/ 

### Visit web which is proxy by Nginx

edit /etc/hosts

```
127.0.0.1 fastapi.winwu.dev
```

Both 80 and 443 port are available:

* visit http://fastapi.winwu.dev/ (http://localhost)
* visit https://fastapi.winwu.dev/
