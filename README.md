# portfolio-poc
This repository houses a POC - a simple portfolio website for a developer.
It users ContentStack's Python SDK to retrieve dynamic content from the CMS.

## Local setup
Please have Docker installed locally (Docker for Mac)

```
cp .env.sample .env
# Add your ContentStack API crendentials
docker-compose up
docker-compose run web python manage.py migrate
```

At [http://localhost:8000](http://localhost:8000) you will have a working version of the application

