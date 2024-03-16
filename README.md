# llm_service

## Overview
The `llm_service` is a FastAPI service that uses OpenAI's Language Model (LLM) to generate JSON data based on the requirements specified in an OpenAPI schema.

## Features
- Takes a text and an OpenAPI schema as input.
- Uses the LLM from OpenAI to generate a JSON.
- The generated JSON adheres to the requirements specified in the OpenAPI schema.

## Getting Started

### Prerequisites
- OpenAI API key

### Installation
# install dependencies
```bash
pip install -r requirements.txt
```
# set OpenAI api key as environment variable
```bash
export OPENAI_API_KEY={your openai key}

```
OPTIONAL FOR TESTING set constant response mode like this it will always return the same query and you dont need the openai token

```bash
export TEST_MODE=constant_response
```
# run llm service
```bash
uvicorn app.main:app --log-config=log_conf.yaml --port 8888
```



### Intallation with docker
# build image
From root directory
```bash
docker build -t llm_service .
```

# run image on port 8888
```bash
docker run -e OPENAI_API_KEY={your OpenAI api key} -p 8888:8888 llm_service
```

# run image on port 8888 for Testing with constant response
docker run -e TEST_MODE=constant_response -p 8888:8888 llm_service
