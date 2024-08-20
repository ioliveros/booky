#!/bin/bash

TOKEN=$(curl --location 'http://localhost:8000/api/token/' \
--form 'username="testuser"' \
--form 'password="foobar"' \
--form 'email="testuser@foobar.com"' | jq -r '.access')

curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'name="Dan Brown"' \
--form 'biography="American author best known for his thriller novels, including the Robert Langdon novels Angels & Demons (2000), The Da Vinci Code (2003), The Lost Symbol (2009), Inferno (2013), and Origin (2017). His novels are treasure hunts that usually take place over a period of 24 hours."'

curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'name="J. K. Rowling"' \
--form 'biography="Born in Yate, Gloucestershire, Rowling was working as a researcher and bilingual secretary for Amnesty International in 1990 when she conceived the idea for the Harry Potter series."'

curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'name="J. R. R. Tolkien"' \
--form 'biography="John Ronald Reuel Tolkien CBE FRSL was an English writer and philologist. He was the author of the high fantasy works The Hobbit and The Lord of the Rings."'

curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'name="George Orwell"' \
--form 'biography="Orwell is best known for his allegorical novella Animal Farm (1945) and the dystopian novel Nineteen Eighty-Four (1949), although his works also encompass literary criticism, poetry, fiction, and polemical journalism."'

curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'name="Frank Herbert"' \
--form 'biography="Franklin Patrick Herbert Jr. (October 8, 1920 – February 11, 1986) was an American science-fiction author, best known for his 1965 novel Dune and its five sequels. He also wrote short stories and worked as a newspaper journalist, photographer, book reviewer, ecological consultant, and lecturer."'
