#  Data Streaming

The aim of the project was to create a shard kinesis stream for a producer to push scraped real estate data from [loopghana](https://listings.loopghana.com/) every 30 seconds using the below schema.

## DataFrame structure
* description
* category
* beds
* baths
* price
* url
* area(mxm)
* broker
* listing_time
* amenities
* latitude
* longitude
* point_of_interest
* point_of_interestcategory
* distance_to_point_of_interest

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to run the script.

* Python: for the data manipulation.
* Gitbash: For pushing the files your repo.
* An IDE(VScode or Jupyter Notebook): To run and edit the codes 
* AWS(Kinesis): for the stream processing.

### Installing

A step by step series of examples that tell you how to get a development env running

* Install python on your system(macOS, windows or Linux)
* Create an account with AWS.
* Clone repo.

## Acknowledgments

* Hisham Osman
