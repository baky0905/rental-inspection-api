

![](https://images.unsplash.com/photo-1563831816793-3d32d7cc07d3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1267&q=80)

<br />
<p align="center">

  <h3 align="center">Vehicle Rental Inspection Data Modelling and REST API </h3>

  <p align="center">
    <br />
    <br />
    <a href="https://github.com/baky0905/rental-inspection-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/baky0905/rental-inspection-api/issues">Request Feature</a>
  </p>
</p>



- [About The Project](#about-the-project)
- [Backend Requirements](#backend-requirements)
- [Backend - local development](#backend---local-development)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Entity Relationshop Diagram (ERD)](#entity-relationshop-diagram-erd)
- [Initialization of the Database](#initialization-of-the-database)
- [Available REST API endpoints](#available-rest-api-endpoints)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)




## About The Project

In this project, I developed a backend for the vehicle inspection web application (web application will not be a part of this project). 

The project included tasks as follows:
  - Data modelling for the vehicle inspection process.
  - Implementation of the data model into a PostgreSQL relational database, initialized  with mandatory data tables for a functional application.
  - Development of data REST API, using Python and [FastAPI](https://fastapi.tiangolo.com/) framework on top of the PostgreSQL database, enabling relevant CRUD operations for the vehicle inspection application. 

The end result can be visualised and tested via API documentation locally when the stack is running (more info on how to later in the readme).

![](img/docs.gif)

All API endpoints need a JWT token for authorized accessed. For the time being, there is a dummy admin user who has privileges to get authorized, and therefore able to request resources from all available endpoints.

![](img/authorize.gif)

Below, there is an example of a crud operation wherein the inspection process, inspector (user) can answer the inspection question vai the POST answer endpoint.

![](img/answer.gif)

## Backend Requirements

**Note that I am developing in WSL2 (Windows Subsystem for Linux), Ubuntu 20.04 distribution, using my favourite code editor - Visual Studio Code, and its set of extensions  from which I would especially recommend [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) for easy creation, management and debugging of containerized applications.**

- [Docker](https://www.docker.com/).
- [Docker Compose](https://docs.docker.com/compose/install/).

## Backend - local development

- Start the stack with Docker Compose:

```bash
docker-compose up -d
```

Now you can open your browser and interact with these URLs:

- ackend, JSON based web API based on OpenAPI: http://localhost:8000/openapi.json

- Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost:8000/docs

- Alternative documentation with ReDoc (from the OpenAPI backend): http://localhost:8000/redoc

- PGAdmin, PostgreSQL web administration: http://localhost:5050/browser/

  - login: 
    - username: admin@example.com
      - password: admin
  - database password: 1234

Since the app is for learning purposes, `.env` with all the passwords and secrets has been version controlled. **Do not do this in real life :)**

To check the logs, run:

```bash
docker-compose logs
```

To check the logs of a specific service, add the name of the service, for example to check the server(api), run:

```bash
docker-compose logs server
```

If your Docker is not running in `localhost` (the URLs above wouldn't work).

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the server waits for the database to be ready and configures everything, you can check the logs to monitor it.


## Getting Started


To start the stack of services, database, pgadmin and server(api), run:

```console
$ docker-compose up -d
```

and then `exec` inside the running container:

```console
$ docker-compose exec server bash
```

You should see an output like:
```console
root@7f2607af31c3:/app#
```

I personally, like to user VS Code's Docker extension and if yo uare doing the same, you can just right-click on the `docker-compose.yml` and command `Compose Up`.

## Project Structure

Below is a structure of the project. I will briefly describe most important python files under the app directory:

```
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── load.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes
│   │   ├   └──v1.py
│   │   ├── schemas.py
│   │   └── utils
│   ├── entrypoint.sh
│   ├── requirements.txt
│   └── venv
├── db_init
│   ├── __init__.py
│   ├── data
│   │   ├── answer.csv
│   │   ├── category.csv
│   │   ├── category_question.csv
│   │   ├── check_log.csv
│   │   ├── driver.csv
│   │   ├── question.csv
│   │   ├── signature.csv
│   │   └── vehicle.csv
│   ├── db-drop-create-load-csvs.py
│   └── sql_queries
│       ├── create-tables.sql
│       ├── drop-tables.sql
│       ├── example_query.sql
│       └── sql_queries.py
├── docker-compose.yml
├── img
└── servers.json
```


- `database.py`
  - imports sqlalchemy part and engine, SessionLocal and Base as declarative_base()
- `models.py`
  - Creates SQLAlchemy models from the Base class
  - These classes are SQLAlchemy models
  - The __tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models.
  - Creates model attributes/columns
  - Creates the relationships via relationship provided by SQLAlchemy ORM. 
- `schemas.py`
  - These Pydantic models define more or less a "schema" (a valid data shape).
- `crud.py`
  - In this file, we will have reusable functions to interact with the data in the database.
  - * CRUD comes from: Create, Read, Update, and Delete.
- `routes/v1.py`
  - contains all the api endpoints for the api version 1
- `main.py`
  - integrates and uses all the other parts from above
  - contains middleware with login endpoints, all endpoints require jwt token
- `utils/security.py`
  - authentication, jwt token creation and verification related functions.
## Entity Relationshop Diagram (ERD)

![](img/erd.png)

ERD has been designed in [https://dbdiagram.io/](https://dbdiagram.io/), and I highly recommend it. Schema can be found in the [local folder](./db_init/erd/erd_dbdiagram.txt), and diagram can easily be reconstructed from it via the website.

![](img/erd_website.png)


## Initialization of the Database

By default, the dependencies are managed with `requirements.txt` and `pip`.

Open your editor at `./backend/` (instead of the project root: `./`). Create a virtual environment while in ./backend folder.

Run following command:
```bash
python3 -m venv venv
```

and activate the env:

```bash
python3 venv/bin/activate
```

Install packages from requirements.txt with pip3:

```bash
pip3 install -r requirements.txt
```

Finally, run a python script `db-drop-create-load-csvs.py` located in db_init folder:

```bash
python3 db_init/db-drop-create-load-csvs.py 
```

The `db-drop-create-load-csvs.py` script will do the following:

- **drops all tables** in postgres database - [script](./backend/db_init/sql_queries/sql_queries.py)
- **creates all tables** in postgres database - [script](./backend/db_init/sql_queries/sql_queries.py)
- populates created tables with data / CSVs, located in [data_init folder](./backend/db_init/)


## Available REST API endpoints

These are the available API endpoints:

![](img/endpoints.png)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/baky0905/rental-inspection-api/issues) for a list of proposed features (and known issues).


**To do:**

- validate with data types, regex and enums at the API layer
- replace dummy admin user with users in the databases, with respective roles
- cache with redis
- test endpoints
- load testing
- deploy API to production environment
- load balancers
- get a domain, reverse proxy, https, Auth 2.0


<!-- LICENSE -->
## License

Distributed under the MIT License.

## Contact

Kristijan Bakaric - [twitter.com/kbakaric1](https://twitter.com/kbakaric1) 



