# Introduction

This is a simple FastAPI application with a Primal Simplex algorithm.

# Deploying

To deploy this application we are using docker-compose to build a container image, then to deploy the project you need to follow these steps below:
* create a folder named "primal-simplex-api" in your Server;
* upload all files, except "testing.py" to the folder created;
* run the command "docker-compose up -d" from within the folder.

# Testing

If everything is okay, we can test our application, use the file "testing.py" to test, changing "localhost" for your server address.

