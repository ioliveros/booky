#!/bin/bash

docker run -it -p 8888:8888 -d \
	-v /Users/ianoliveros/Dev/devjobs/spotter.io/booky/data/models:/app/models/ \
	-v /Users/ianoliveros/Dev/devjobs/spotter.io/booky/data/dataset:/app/dataset/ \
	--rm reco-service:latest