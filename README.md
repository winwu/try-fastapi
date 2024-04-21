# Try fastapi

```
cd ~./
python3 -m venv .venv
```

```
source .venv/bin/activate
```


```
cd app
uvicorn main:app --reload
```

visit swagger index

```
http://127.0.0.1:8000/docs
```



## run with docker

```
# build image
docker build -t myimage .

# start container
docker run -d --name mycontainer -p 80:80 myimage
```