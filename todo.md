# Idea: 
word clouds of tagged politician images using Clarifai by political candidate

# TODO

1. Image Scraper
  - scrape web for images of political candidates
  - how do we ensure that image is actually that candidate?


2. Candidate Classifier
  - classify candidates using Clarifai API
  - data structure: dictionary of dictionaries, key = candidateName, value = dictionary { key = word, value = count }


3. Generate Wordclouds
  - for each candidate, generate a text file of words
  - for each word, print the word n times where n is count, save to text file


4. Present Results
  - simple website, choose a candidate, see that wordcloud
