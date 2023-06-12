# Run without Docker
Run `database.py` to make a testing database:
```
python3 database.py
```
Then activate virtual environment:
```
. .venv/bin/activate
```

After that you can run the application with:
```
flask run
```


# Run inside a docker container
To run the application inside of docker container you firstly need to create docker image using `Dockerfile`. Run the next command:
```
docker build -t flask-app .
```
After you succesfully create the image you need to run it (it is important to specify the port):
```
docker run -p 5000:5000 flask-app
```
### ! IMPORTANT !
By my testing the docker version does not work. I believe that the problem is on my side, maybe something with firewall... (my curl command return empty reply from container)

# Testing
Tested on WSL2 Ubuntu 22.04.2 LTS using command curl.

For example:
```
curl -X GET http://localhost:5000/movies
```
```
curl -X GET http://localhost:5000/movies/3
```
```
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Movie 1", "description": "Something about this movie", "release_year":"1999"}' http://localhost:5000/movies
```
```
curl -X PUT -H "Content-Type: application/json" -d '{"description": "Something new about this movie"}' http://localhost:5000/movies/6
```