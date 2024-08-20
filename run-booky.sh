#!/bin/bash

docker run -it --rm -d \
	--memory=1g \
	-p 8000:8000 booky-service:latest
	
