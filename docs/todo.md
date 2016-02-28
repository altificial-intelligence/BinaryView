# Idea: 
word clouds of tagged politician images using Clarifai by political candidate

# TODO

1. Image Scraper
  !- scrape web for images of political candidates
  !- query google images for picture of each political candidate, save urls of each candidate into text file
  !- ex: donald_trump.txt


2. Candidate Classifier
  !- classify candidate images using Clarifai API
  !- parse classifications
  !- data structure: dictionary of dictionaries, key = candidateName, value = dictionary { key = word, value = count }
  !- then output each candidate's dictionary to a text file of words


3. Generate Data Viz
  !- for each candidate, generate a text file of words
  !- for each word, print the word n times where n is count, save to text file
  - generate wordcloud / data visualization


4. Web app to dynamically generate data viz
  !- hello world flask on heroku
  !- make sure response from classify clarifai was OK, ensure classes is just a list, not nested! (try other)
  !- set clarifai environment variables in heroku
  - generate wordcloud from words, start by logging to console the words in JS
  - spice up with stylesheets


5. Devpost
  - write up, submit by 11am, start at 10:45am