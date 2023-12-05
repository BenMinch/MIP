#PFAM description scraper

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys,os,subprocess,argparse

argparser = argparse.ArgumentParser(description='Get PFAM descriptions from PFAM accension numbers')
argparser.add_argument('-i', '--input', help='Input csv file (Must have a column called AC with PFAM accession numbers)', required=True)
argparser.add_argument('-o', '--output', help='Output csv file', required=True)
argparser.add_argument('-cd', '--chromedriver', help='Path to chromedriver', required=True)
args = argparser.parse_args()

protein_file = pd.read_csv(args.input)
output_file = args.output
chromedriver = args.chromedriver

def fetch_pfam_desc(protein_id):
    base_url='https://www.ebi.ac.uk/interpro/entry/pfam/'
    url=base_url+protein_id
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service=Service(chromedriver)
    driver=webdriver.Chrome(service=service,options=chrome_options)
    print(url)
    driver.get(url)
    driver.implicitly_wait(5)

    try:
        description_element=driver.find_element(By.CLASS_NAME,'description')
        description=description_element.text
    except Exception as e:
        description='Not found'
    driver.quit()
    return description

#iterate through this for every entry in a dataframe and store the description in a description column
#split AC column at . and take the first part of the string
#only keep bins with evalue_y < 1e-5
protein_file['AC']=protein_file['AC'].str.split('.').str[0]
protein_file['Description']=protein_file['AC'].apply(fetch_pfam_desc)


protein_file.to_csv(output_file,index=False)
