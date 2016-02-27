# Idea: 
word clouds of tagged politician images using Clarifai by political candidate

# TODO

1. Image Scraper
  !- scrape web for images of political candidates
  !- query google images for picture of each political candidate, save urls of each candidate into text file
  !- ex: donald_trump.txt


2. Candidate Classifier
  - classify candidates using Clarifai API
  - parse classifications
  - data structure: dictionary of dictionaries, key = candidateName, value = dictionary { key = word, value = count }
  - then output each candidate's dictionary to a text file of words


3. Generate Wordclouds [http://www.wordle.net/]
  - for each candidate, generate a text file of words
  - for each word, print the word n times where n is count, save to text file


4. Present Results
  - simple website, choose a candidate (dropdown), see that wordcloud image file
