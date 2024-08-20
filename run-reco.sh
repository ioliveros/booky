#!/bin/bash

docker run -it --rm -d \
	--memory=6g --memory-swap=8g \
	-v $(pwd)/reco/dataset:/app/reco/dataset \
	-v $(pwd)/reco/models:/app/reco/models \
	-p 8001:5000 reco-service:latest
	
