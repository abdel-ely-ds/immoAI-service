# ImmoAI <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/5da8796b-07d6-4db2-9121-6c451e739a9e" width="35">
<p align="center">
  <i align="center">ImmoAI aims to help you search you dream house 🏠, do real estate market research, get trends <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/a8dda30f-1cf2-4673-a339-5099f63ac3e6" width="20">
 using natural language.</i>
</p> 

![Image Alt Text](assets/immo.PNG)


## Requirements 
1) You need to have OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV. You need to create a file .env and put the keys there.
2) AWS CLI configured.
3) Ask to get access to the data.
   
## Getting Started <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/34c25f95-f2e6-4311-8807-50b7f356bfa0" width="35">

### Installation
------------

    $ git clone https://github.com/abdel-ely-ds/immoAI-service.git
    $ cd immoai-service
    
### Run the service  <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/a8f44441-1b19-4398-ac6f-ea8707366f01" width="25">
------------
    $ pip install -e .
    $ uvicorn immo.app:app

### Run with Docker <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/5b321dcb-0c6a-4185-ac47-b1259603545e" width="25">
------------
    $ docker-compose up
    
## RoadMap <img src="https://github.com/abdel-ely-ds/immoAI-service/assets/76486913/9564ea11-cfc2-488e-9679-0a0ef0865a42" width="35">

1) Add visualization.
2) Possibility to visualize the relationship between price and some other variables.
3) Add dashboard to give a global overwiew of the market.
