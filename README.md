# Google Image Scraper
A library to scrap google images

## This Fork
Adds the ability to iterate over seach keys from a csv file in the following format:

| Species | Taxon | Disease name | Causative agent |
| ------- | ----- | ------------ | --------------- |
|Cedrus |.|Sirococcus blight|Sirococcus tsugae|
|Chamaecyparis |.|ceder root diease|Phytophthora lateralis|
|Chamaecyparis |.|Coryneum canker|Seiridium cardinale|
|Chamaecyparis |.|Phytophthora root rot|Phytophthora|
|Thuja plicata|.|Thuja blight|Didymascella thujina|
|Abies bornmuelleriana|.|.|.|

In this case I was searching for images of tree and crops species with and without disease. Hence, 'Healthy' and 'Diseased' in main.py and in the output diectory.
The healthy images will crome from the first two search keys in each row and the diseased images will come from all keys per row.

_n.b. This program is currentley set to utilise all cores on a given machine. If maxing out your abndwidth is likley to be an issue, edit the following line in main.py:_
n_processes = mp.cpu_count()

## Pre-requisites:
1. Pip install Selenium Library
2. Pip install PIL
3. multiprocessing
4. pandas
5. Download Google Chrome 
6. Download Google Webdriver based on your Chrome version

## Setup:
1. Open cmd
2. Clone the repository (or [download](https://github.com/ohyicong/Google-Image-Scraper/archive/refs/heads/master.zip))
    ```
    git clone https://github.com/ohyicong/Google-Image-Scraper
    ```
3. Install Dependencies
    ```
    pip install selenium, requests, pillow
    ```
4. Run the code
    ```
    python Google-Image-Scraper/main.py /search_keys.csv /final_image_dir
    _n.b. you may need to update the google driver in the Google-Image-Scraper dir
    ```
_The following structions refer to the original code and not this fork
## Usage:
```python
#Import libraries (Don't change)
from GoogleImageScrapper import GoogleImageScraper
import os
from patch import webdriver_executable

#Define file path (Don't change)
webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

#Parameters
number_of_images = 10
headless = True
min_resolution=(0,0)
max_resolution=(1920,1080)

#Main program
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)

```
## Youtube Video:
[![IMAGE ALT TEXT](https://github.com/ohyicong/Google-Image-Scraper/blob/master/youtube_thumbnail.PNG)](https://youtu.be/QZn_ZxpsIw4 "Google Image Scraper")

Do remember to like, share and subscribe!
