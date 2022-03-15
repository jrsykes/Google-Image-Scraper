# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable
import pandas as pd

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    #search_keys= ['cedrus cedar Sirococcus blight Sirococcus tsugae']

    #Parameters
    number_of_images = 1000
    headless = True
    min_resolution=(99,99)
    max_resolution=(9999,9999)

    data_base_path = '/home/jamiesykes/Downloads/Forestry_disease_data_Combined.csv'
    df = pd.read_csv(data_base_path, header=None)

    for index, row in df.iterrows():
            for i in ['Healthy', 'Diseased']:
                if i == 'Healthy':
                    search_keys = list(row[:2])
                else:
                    search_keys = list(row)
                
                image_path = '/home/jamiesykes/Downloads/images/' + (search_keys[0] + i).replace(' ', '_')            
                search_key = ' '.join(str(x) for x in search_keys)
    #Main program
                if i == 'Healthy' and os.path.isdir(image_path) == False:

                    url_lst = []
                    for i in range(10):
                        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,
                            headless,min_resolution,max_resolution)
                        url_lst.append(image_scrapper.find_image_urls())
                    
                    image_urls = [item for sublist in url_lst for item in sublist]
                    image_urls = list(dict.fromkeys(image_urls))
                        

                    image_scrapper.save_images(image_urls)
                    del image_scrapper
    
                if i == 'Diseased':

                    for i in range(10):
                        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,
                            headless,min_resolution,max_resolution)
                        url_lst = []
                        url_lst.append(image_scrapper.find_image_urls())
                    
                    image_urls = [item for sublist in url_lst for item in sublist]
                    image_urls = list(dict.fromkeys(image_urls))

                    image_scrapper.save_images(image_urls)
                #Release resources    
                    del image_scrapper
    