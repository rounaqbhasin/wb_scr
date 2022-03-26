# 24th November, 2021
# Python Web Scraper
# This program is made so that we can find the job listings

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')
# ^ To get the contents of the site we're working on (In this case, we're using timesjobs.com)
soup = BeautifulSoup(html_text.text, 'lxml')

# We're using 'html_text.text' instead of 'html_text' because we need the values in str and not in docs (bytes)
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') # Jobs under 'Python' keyword

for job in jobs: # To iterate one-by-one
    published_date = job.find('span', class_='sim-posted').span.text  # Date of Publishing of the post

    if 'few' in published_date: # This iteration is used so that only recent and not outdated jobs are presented
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') # Companies wanting recruits good in Python
        skillset = job.find('span', class_='srp-skills').text.replace(' ', '') # Skillsets a candidate need to have other than Python.
        more_info = job.header.h2.a['href']

        print(f"Company Name: {company_name.strip()}" # strip() returns the string with leading and trailing characters removed 
              f"Skills Required: {skillset.strip()}")# strip() will make the information more organized
        print(f"More info: {more_info}")
        # ^ a string literal
        print('') # So that there can be a gap between two jobs
