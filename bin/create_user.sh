#!/bin/bash

curl --location 'http://localhost:8000/api/register' \
--form 'username="testuser"' \
--form 'email="testuser@foobar.com"' \
--form 'password="foobar"' \
--form 'first_name="Test"' \
--form 'last_name="User"'

