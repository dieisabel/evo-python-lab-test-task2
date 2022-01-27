# EVO Python Lab 2022 Test Tasks: Task 2

## Table of contents

1. [Description](#description)
2. [Installation](#installation)
3. [Deployment](#deployment)
4. [Production](#production)

### Description

A simple web-service that just welcomes you. Enter your name and see if service already known you.
If not, it just says hello to you. Also, you can see all names that are already known by service.

#### Technology stack

- FastAPI - web framework
- Uvicorn - server to handle HTTP requests
- Jinja2 - templating language

#### "State" solution

All names saved in a Python dictionary. 

#### Structure

All source code located in `src/` directory:
- `app/` - application root
- `static`/ - directory for static (css, javascript, fonts etc)
- `templates/` - directory for templates

### Installation

#### Manual

Clone project: 

```bash
$ git clone https://github.com/dieisabel/evo-python-lab-test-task2
```

Create and activate virtual environment:

```bash
$ python -m venv venv
# For Unix like OS
$ source venv/bin/activate
# For Windows
> .\venv\Scripts\activate
```

Install dependencies from `requirements.txt` using pip:

```bash
$ pip install -r ./requirements.txt
```

Cd to application root and start server using `server.py`:

```bash
$ cd ./src/app/ && python server.py
```

#### Docker

Clone project: 

```bash
$ git clone https://github.com/dieisabel/evo-python-lab-test-task2
```

Build Docker container:

```bash
$ docker build -t application:1.0.0 .
```

Run Docker container:

```bash
$ docker run -d --rm --name application -p 8000:8000/tcp application:1.0.0
```

### Deployment

Project uses Heroku to deploy code. To deploy project using Heroku proceed with instructions below:

1. Create new Heroku application [here](https://dashboard.heroku.com/apps).
2. Download [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
3. Login to [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
4. Add Heroku git remote:
```bash
$ heroku git:remote -a <Heroku app name>`
```
5. Push your branch to a Heroku remote:
```bash
$ git push heroku master
# If you want to push a particular branch
$ git push heroku <branch>:master
```
6. Go to a Heroku application page `<Heroku app name>.herokuapp.com/`. 

### Production

To see a production version of project go [here](https://evo-python-lab-say-my-name.herokuapp.com/).
