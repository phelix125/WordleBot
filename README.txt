The repo contains WordleBot, an automatic bot that beats the game wordle for you, it's made using request and selenium to scrape the text, and send 
words to the site. This folder contains 3 files.

Words.txt -> All 5 letter words, which we'll use as our corpus

WordleAPI -> This connects to the site and handles sending/recieving traffic from it. This file is mainly responsible for interacting with the site.

WordlePy ->  This loads our data, and recieves traffic from WordleAPI, which then it uses hueristics to remove certain words from our list. This file recieves character's and their statuses and filters them.
