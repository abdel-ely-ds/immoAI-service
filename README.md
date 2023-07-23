## About The Project
This project aims to help you Search you dream house, do real estate market research using natural language.

## Requirements 
1) You need to have OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV. You need to create a file .env and put the keys there
2) AWS CLI configured
## Getting Started
Installation
------------

    $ git clone https://github.com/abdel-ely-ds/immoAI-service.git
    $ cd immoai-service
    
Run the service
------------
    $ pip install -e .
    $ uvicorn immo.app:app

Run with Docker
------------
    $ docker-compose up


