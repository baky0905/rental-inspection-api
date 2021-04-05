


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/baky0905/rental-inspection-api">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Vehicle Rental Inspection Data Modelling and REST API </h3>

  <p align="center">
    More info.
    <br />
    <a href="https://github.com/baky0905/rental-inspection-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="./">View Demo</a>
    ·
    <a href="https://github.com/baky0905/rental-inspection-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/baky0905/rental-inspection-api/issues">Request Feature</a>
  </p>
</p>



- [About The Project](#about-the-project)
- [Project Structure](#project-structure)
- [Backend Requirements](#backend-requirements)
- [Backend local development](#backend-local-development)
- [Backend local development, additional details](#backend-local-development-additional-details)
  - [General workflow](#general-workflow)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.


## Project Structure

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

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).

## Backend local development

* Start the stack with Docker Compose:

```bash
docker-compose up -d
```

- Now you can open your browser and interact with these URLs:

Backend, JSON based web API based on OpenAPI: http://localhost:8000/openapi.json

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost:8000/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost:8000/redoc

PGAdmin, PostgreSQL web administration: http://localhost:5050/browser/

  - login: 
    - username: admin@example.com
      - password: admin
  - database password: 1234


To check the logs, run:

```bash
docker-compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker-compose logs server
```

If your Docker is not running in `localhost` (the URLs above wouldn't work) check the sections below on **Development with Docker Toolbox** and **Development with a custom IP**.

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the backend waits for the database to be ready and configures everything. You can check the logs to monitor it.


## Backend local development, additional details

### General workflow

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

By default, the dependencies are managed with requirements.txt and pip.


Next, open your editor at `./backend/app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created.

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

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


