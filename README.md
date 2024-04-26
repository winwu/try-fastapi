# Try fastapi


## env requirement

Python 3.9, venv... etc.

- please ref requirements.txt
- if using vscode, please install [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)


## data source

<!--next phase: Please download [Airline dataset](https://www.kaggle.com/datasets/mohammadkaiftahir/airline-dataset)-->

## usage - for developing in local

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
```

visit swagger index

```
http://127.0.0.1:8000/docs
```



## run with docker

```
# start container
docker-compose up --build

# then visit https://localhost:9443/

# start container without build
docker-compose up
```

## TODO

* append complete owner data object in get /items response
* pagination response
* move from sqlite to mariadb (migration: https://alembic.sqlalchemy.org/en/latest/)
* authentication (JWT) (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
* error response handler
* serve static file

