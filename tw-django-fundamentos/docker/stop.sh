#!/bin/bash

CONTAINERS_DOCKER=$(docker ps -q)

echo "Parando containers..."
docker container stop $CONTAINERS_DOCKER

echo "Removendo containers..."
docker container rm $CONTAINERS_DOCKER