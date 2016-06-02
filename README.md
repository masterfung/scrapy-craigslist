Scrapy for Craigslists Apartments
===========

A project by: Tsung Hung [@masterfung](twitter.com/masterfung)

Scrapy is the open-source web scrapper and it is used to power
this library. Please visit [this link](http://scrapy.org/)
for more information.

## Purpose:
The purpose of Scrapy Craigslist (CL) is
to obtain useful CL apartment data for application-
specific data analysis and representation.

A model example that utilizes the data from this project is
located [here](https://github.com/masterfung/scrapilious). This
project is a Django-powered project.

## Requirements:
You will need:

* Python 2.x or 3.x
* pip
* Scrapy (`pip install scrapy`)

## Project:

Clone the project with `git clone git@github.com:masterfung/scrapy-craigslist.git`

## Craigslist City Codes:

If you need to change the city on the project to harvest
a different city, please reference [this link](https://sites.google.com/site/clsiteinfo/city-site-code-sort)
for more information. Once you change that component, you would
 be able to obtain the data from the city of interest.

## Running the Project

Here are the steps to take to modify the the returning city data of interests:

* Look into the spiders folder and click on the `craigslist_scrapy.py`
* Click on the city codes and replace link with the city of your interest.
There are three areas this appears.
* Run the code and use this command: `scrapy crawl craigslist -o FILENAME.json`

**NOTE**: This may take awhile, depends on how many listings are on Craigslist
and how many parameters you selected.

Outputted JSON files should be saved on the applicational level of this project.

If there are any issues or request, please let me know. I am happy to help.
All the feedback are welcomed. Let us learn and build things together!

Happy Scraping!

## User Agent

Visit [this link] (http://api.useragent.io/) to obtain newly generated user agent
to run your this Scrapy. You can change the User Agent in the `settings.py` file.

The link was a project by the wonderful [Randall Degges] (https://github.com/rdegges).
He is awesome!!


## Others

Beware of IP ban from Craigslist.
