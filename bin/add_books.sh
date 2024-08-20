#!/bin/bash

TOKEN=$(curl --location 'http://localhost:8000/api/token/' \
--form 'username="testuser"' \
--form 'password="foobar"' \
--form 'email="testuser@foobar.com"' | jq -r '.access')

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Harry Potter and the Order of the Phoenix"' \
--form 'author="2"' \
--form 'genre="fiction"' \
--form 'description="Harry Potter and the Order of the Phoenix is a fantasy novel written by British author J. K. Rowling and the fifth novel in the Harry Potter series. It follows Harry Potters struggles through his fifth year at Hogwarts School of Witchcraft and Wizardry, including the surreptitious return of the antagonist Lord Voldemort, O.W.L. exams, and an obstructive Ministry of Magic."' \
--form 'publish_date="2003-04-02"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Harry Potter and the Prisoner of Azkaban"' \
--form 'author="2"' \
--form 'genre="fiction"' \
--form 'description="Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author J. K. Rowling and is the third in the Harry Potter series. The book follows Harry Potter, a young wizard, in his third year at Hogwarts School of Witchcraft and Wizardry. Along with friends Ronald Weasley and Hermione Granger, Harry investigates Sirius Black, an escaped prisoner from Azkaban, the wizard prison, believed to be one of Lord Voldemorts old allies."' \
--form 'publish_date="1999-07-08"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Harry Potter and the Philosophers Stone"' \
--form 'author="2"' \
--form 'genre="fiction"' \
--form 'description="Harry Potter and the Philosophers Stone is a fantasy novel written by British author J. K. Rowling. The first novel in the Harry Potter series and Rowlings debut novel follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry. "' \
--form 'publish_date="1997-06-26"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Digital Fortress"' \
--form 'author="1"' \
--form 'genre="techno-thriller"' \
--form 'description="Digital Fortress is a techno-thriller novel written by American author Dan Brown. The book explores the theme of government surveillance of electronically stored information on the private lives of citizens, and the possible civil liberties and ethical implications of using such technology."' \
--form 'publish_date="1998-06-26"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Angels & Demons"' \
--form 'author="1"' \
--form 'genre="mystery-thriller"' \
--form 'description="The novel introduces the character Robert Langdon, who recurs as the protagonist of Browns subsequent novels. "' \
--form 'publish_date="2000-05-26"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Angels & Demons"' \
--form 'author="1"' \
--form 'genre="mystery-thriller"' \
--form 'description="The novel introduces the character Robert Langdon, who recurs as the protagonist of Browns subsequent novels. "' \
--form 'publish_date="2000-05-26"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Origin"' \
--form 'author="1"' \
--form 'genre="mystery"' \
--form 'description="Origin is a 2017 mystery thriller novel by American author Dan Brown and the fifth installment in his Robert Langdon series following Inferno. The book is predominantly set in Spain and features minor sections in Sharjah and Budapest."' \
--form 'publish_date="2017-10-03"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="The Lord of the Rings: The Fellowship of the Ring"' \
--form 'author="3"' \
--form 'genre="fantasy"' \
--form 'description="The action takes place in the fictional universe of Middle-earth. The book was first published on 29 July 1954 in the United Kingdom. "' \
--form 'publish_date="1954-07-29"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Animal Farm: A Fairy Story"' \
--form 'author="4"' \
--form 'genre="political sature"' \
--form 'description="Animal Farm is a satirical allegorical novella, in the form of a beast fable, by George Orwell, It tells the story of a group of anthropomorphic farm animals who rebel against their human farmer, hoping to create a society where the animals can be equal, free, and happy."' \
--form 'publish_date="1945-08-17"'

curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer '$TOKEN \
--form 'title="Dune"' \
--form 'author="5"' \
--form 'genre="science fiction"' \
--form 'description="Dune is set in the distant future in a feudal interstellar society, descended from terrestrial humans, in which various noble houses control planetary fiefs. "' \
--form 'publish_date="1965-08-17"'