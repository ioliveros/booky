#!/bin/bash

# docker run -it --rm -d \
# 	--memory=6g --memory-swap=8g \
# 	-v $(pwd)/reco/dataset:/app/reco/dataset \
# 	-v $(pwd)/reco/models:/app/reco/models \
# 	-p 8001:5000 reco-service:latest
	

# /app/models/

docker run -it -p 8888:8888 -d \
	-v /Users/ianoliveros/Dev/devjobs/spotter.io/booky/data/models:/app/models/ \
	-v /Users/ianoliveros/Dev/devjobs/spotter.io/booky/data/dataset:/app/dataset/ \
	--rm reco-service:latest