# Recipe-App-API
## Description
The project is a backend REST API built with TDD (Test Driven Development) process approach. Project was also successfuly deployed on an AWS EC2 instance.

**Recipe-App-API handles:**

* User authentication

* Creating objects

* Filtering and sorting objects

* Uploading and viewing images

Technology stack used to create a project:

* **Development**

    Python, Django 4, Django Rest Framework, Docker

* **Database**

    PostgreSQL

* **Deployment**

    nginx, uWSGI, AWS EC2 Instance, Docker

* **Test and Lint**

    Django's unit tests, flake8 (PEP8), GitHub Actions

* **Documentation**

    drf-spectacular, Swagger
***

## Running the app

Requirements:

macOS, Linux or Windows machine capable of running Docker (This excludes Windows 10 Home)

To run the app, navigate to the project's root directory and run the following command:

    docker-compose up

When the app building process is finished you can access it at:

    http://127.0.0.1:8000/

***

## APIs
Quick overview about APIs and their endpoints.

 To get more details navigate to **/api/docs/** after deploying the app.

***Recipe API is allowed only for authenticated users. In order to create an account follow the instructions which can be found at Recipe-App-API home page.***


* **Health check**

    * GET /api/health-check/

* **User**

    * POST /api/user/create/

    * GET, PUT, PATCH /api/user/me/

    * POST /api/user/token/

* **Recipe**

    * GET, POST /api/recipe/recipes/

    * GET, POST, PATCH, DELETE /api/recipe/recipes/{id}/

    * POST /api/recipe/recipes/{id}/upload-image/

    * **Ingredients**

        * GET /api/recipe/ingredients/

        * PUT, PATCH, DELETE /api/recipe/ingredients/{id}/

    * **Tags**

        * GET /api/recipe/tags/

        * PUT, PATCH, DELETE /api/recipe/tags/{id}/

* **Schema**

    * GET /api/schema/

***
