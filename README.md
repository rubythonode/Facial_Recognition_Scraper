# Facial_Recognition_Scraper
Scraper, using facial recognition software. Written in python Uses the openCV module. Still barebones, but still started.

This scraper will look across all dating websites, after reaching a match on a facial image using websites like Facebook, Twitter, and Tumblr if they have all 3. This search engine assumes that the subject of the search has a Facebook at the very least.


Requirements:
Scapy
Requests
OpenCV
BeautifulSoup

Basic Functionality:
The basics of this search engine are, have images that need to be hashed set in the folder ImagesToBeHashed, after each image is hashed, it will store the has of that image and image name into a CSV file(todo).

It will download images gathered from the specified Xpath based off of public and private profiles, still need to do digging to see where the Xpath is for the other listed sites and add those paths to the scraper logic.

The scraper will also search the Xpath listed for relationship status, to check and see if the person is in a relationship or not, it can report back on what it finds either in an HTML file for the specified subject or into a CSV file. purely choice of the user.

Lots more work is needed, need to add in alot more fucntionality. I am looking to impliment this into a backend framework of a website and offer it as a service for people to use, who do not know how to program. I am looking for contributers, any and all positive help is openly accepted.
