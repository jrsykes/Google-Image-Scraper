# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: jrsykes

"""
#Import libraries
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable
import pandas as pd
import multiprocessing as mp
import sys


if __name__ == "__main__":
    #Define file path
    dataset = sys.argv[1] # Your dataset of search keys
    im_path = sys.argv[2] # Final image dataset path

    webdriver_path = os.path.join(os.getcwd(), 'Google-Image-Scraper/chromedriver')
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))


    #Parameters
    number_of_images = 1000
    headless = True
    min_resolution=(99,99)
    max_resolution=(9999,9999)

    def run(dat):
        for index, row in dat.iterrows():
            for i in ['Healthy', 'Diseased']:
                if i == 'Healthy':
                    search_keys = list(row[:2])
                else:
                    search_keys = list(row)
            
                image_path = os.path.join(im_path, (search_keys[0] + i).replace(' ', '_'))            

                search_key = ' '.join(str(x) for x in search_keys)
#Main program
                if i == 'Healthy' and os.path.isdir(image_path) == False:
                    url_lst = []
                    for i in range(10): # Do ten times to compensate for inconsistant results. A little hacky, I know but it still doesn't really work.
                        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,
                            headless,min_resolution,max_resolution)
                        url_lst.append(image_scrapper.find_image_urls())
                
                    image_urls = [item for sublist in url_lst for item in sublist]
                    image_urls = list(dict.fromkeys(image_urls))
                    
                    image_scrapper.save_images(image_urls)

                if i == 'Diseased':
                    url_lst = []
                    for i in range(10): 
                        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,
                            headless,min_resolution,max_resolution)
                        url_lst.append(image_scrapper.find_image_urls())
                
                    image_urls = [item for sublist in url_lst for item in sublist]
                    image_urls = list(dict.fromkeys(image_urls))
                    image_scrapper.save_images(image_urls)
            #Release resources    
            del image_scrapper
    
    # Multiprocessing
#    data_base_path = dataset
#    df = pd.read_csv(data_base_path, header=None)#

#    n_processes = mp.cpu_count()
#    chunk_size = int(df.shape[0]/n_processes)
#    chunks = [df.iloc[df.index[i:i + chunk_size]] for i in range(0, df.shape[0], chunk_size)]#

#    pool = mp.Pool(processes=n_processes)
#    result = pool.map(run, chunks)
#    pool.close() 
    run(df)