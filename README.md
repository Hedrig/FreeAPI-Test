# FreeAPI-Test
Some code to test FreeAPI's functionality in conjunction with Docker Compose. Both are new to me, so I need to start somewhere.

## Installation
This particular test application uses Docker Compose, everything is already there. Simply run
~~~
docker compose up --build
~~~
and it should build both the database and the application containers.

However, it should be noted that the containers will probably only run on Ubuntu-based OS or WSL due to the usage of "apt-get" command in the compose.yaml file.  

## Usage
The application receives GET and POST requests on port 8000 and forms a JSON formatted response. The responses contain quiz questions that are subsequently fetched from quiz distributing API located [here](https://jservice.io/api/random). POST requests must also send the number of questions the application is required to fetch, wrapped in JSON like this: "{questions_num: \<number of questions\>}". The questions fetched will be stored in the database, and the GET request will display questions currently saved there. The POST request returns the last question added to the database.
