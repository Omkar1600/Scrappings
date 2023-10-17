import csv
from bs4 import BeautifulSoup
import requests
import re

# Getting the links from the previous code
links = [ '/jobs/q-Web+Developer-jobs', '/jobs/q-Product+Manager-jobs', '/jobs/q-Full+Stack+Developer-jobs', '/jobs/q-Android+Developer-jobs', '/jobs/q-Program+Manager-jobs', '/jobs/q-SQL+Developer-jobs', '/jobs/q-Frontend+Developer-jobs', '/jobs/q-Network+Engineer-jobs', '/jobs/q-Systems+Administrator-jobs', '/jobs/q-Solution+Architect-jobs', '/jobs/q-DevOps+Engineer-jobs', '/jobs/q-Game+Developer-jobs', '/jobs/q-Network+Administrator-jobs', '/jobs/q-Salesforce+Developer-jobs', '/jobs/q-Backend+Developer-jobs', '/jobs/q-Machine+Learning+Engineer-jobs', '/jobs/q-.Net+Developer-jobs', '/jobs/q-PHP+Developer-jobs', '/jobs/q-Python+Developer-jobs', '/jobs/q-Mobile+Developer-jobs', '/jobs/q-Linux+Administrator-jobs', '/jobs/q-C-jobs', '/jobs/q-Cryptocurrency-jobs', '/jobs/q-Blockchain-jobs', '/jobs/q-Docker-jobs', '/jobs/q-JavaScript-jobs', '/jobs/q-SQL-jobs', '/jobs/q-Artificial+intelligence-jobs', '/jobs/q-Big+data-jobs', '/jobs/q-Chef-jobs', '/jobs/q-MATLAB-jobs', '/jobs/q-Django-jobs', '/jobs/q-MongoDB-jobs', '/jobs/q-TensorFlow-jobs', '/jobs/q-Agile-jobs', '/jobs/q-Machine+learning-jobs', '/jobs/q-Kanban-jobs', '/jobs/q-C%23-jobs', '/jobs/q-GraphQL-jobs', '/jobs/q-Data+mining-jobs', '/jobs/q-Neural+networks-jobs', '/jobs/q-Scala-jobs', '/jobs/q-Deep+learning-jobs', '/jobs/q-Groovy-jobs', '/jobs/q-Apache+Kafka-jobs', '/jobs/q-SAP+HANA-jobs', '/jobs/q-Erlang-jobs', '/jobs/q-Objective%26%2345C-jobs', '/jobs/q-Part+Time-jobs', '/jobs/q-Azure-jobs', '/jobs/q-Selenium-jobs', '/jobs/q-ServiceNow-jobs', '/jobs/q-Splunk-jobs', '/jobs/q-Work+From+Home-jobs', '/jobs/q-Remote-jobs', '/jobs/q-ETL-jobs', '/jobs/q-Mulesoft-jobs', '/jobs/q-Business+Analyst-jobs', '/jobs/q-Xamarin-jobs', '/jobs/q-Cognos-jobs', '/jobs/q-Telecommute-jobs', '/jobs/q-Pega-jobs', '/jobs/q-Startup-jobs', '/jobs/q-SDET-jobs', '/jobs/q-DoD-jobs', '/jobs/q-SAP+ABAP-jobs', '/jobs/q-.NET-jobs', '/jobs/q-Java-jobs', '/jobs/q-Python-jobs', '/jobs/q-Oracle-jobs', '/jobs/q-Spring-jobs', '/jobs/q-Tableau-jobs', '/jobs/q-Cloud-jobs', '/jobs/q-Linux-jobs', '/jobs/q-Ruby-jobs', '/jobs/q-AngularJS-jobs', '/jobs/q-Spark-jobs', '/jobs/q-C%2B%2B-jobs', '/jobs/q-Cyber+security-jobs', '/jobs/q-MySQL-jobs', '/jobs/q-Data+Scientist-jobs', '/jobs/q-Swift-jobs', '/jobs/q-Amazon+Web+Services-jobs', '/jobs/q-DevOps-jobs', '/jobs/q-Hadoop-jobs', '/jobs/q-QA-jobs', '/jobs/q-Elasticsearch-jobs', '/jobs/q-Kotlin-jobs', '/jobs/q-React.js-jobs', '/jobs/q-Business+Analyst-jobs', '/jobs/q-Developer-jobs', '/jobs/q-Perl-jobs', '/jobs/q-UX-jobs', '/jobs/q-iOS+Developer-jobs']

for i in links:

    # Initalizing empty list for storage of data
    job_titles=[]
    company_names = []
    locations = []
    summaries = []
    posting_dates = []

    # Generating Links
    url = 'https://www.dice.com{}'.format(i)
    response = requests.get(url) 
        
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        div_tag = soup.find('div', class_='sc-dhi-seds-pagination')
            
        # For multipage jobs    
        if div_tag:
            span_tag = div_tag.find_all('span')[1]
            text_content = span_tag.get_text()

            # Getting the number of page for the job type
            integer_value = int(text_content.split()[-1])
            print(integer_value)
                
            for j in range(1, integer_value+1):
                # Creating the modified url
                mod_url = url + '?page={}'.format(j)
                response = requests.get(mod_url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'lxml')

                    # Finding all job cards within the "jobs-container" class
                    job_cards = soup.find_all('dhi-job-search-job-card', class_='dhi-job-search-job-card sc-dhi-job-search-job-card-h hydrated')
                    for job_card in job_cards:

                        # Scrapping the required Data
                        anchor_tag = soup.find('header', class_='card-header sc-dhi-job-search-job-card-layout-full').find('a', class_='link-label job-title-link util-interactive sc-dhi-job-search-job-card-layout-full')
                        job_title = anchor_tag.contents[1].strip()

                        company_name = job_card.find('h3', class_='jcl-company-name sc-dhi-job-search-job-card-layout-full').text.strip()

                        location = job_card.find('main', class_='card-body')
                        job_location = location.find('p', class_='location-display').get_text(strip=True)

                        summary = job_card.find('span', class_='job-summary-full p-reg-100 sc-dhi-job-search-job-card-layout-full').text.strip()

                        date_of_posting = job_card.find('div', class_='p-reg-75 sc-dhi-time-ago').text.strip()

                        # Appending data to lists
                        job_titles.append(job_title)
                        company_names.append(company_name)
                        locations.append(job_location)
                        summaries.append(summary)
                        posting_dates.append(date_of_posting)
                print(j)
        
        # For Single page jobs
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            job_cards = soup.find_all('dhi-job-search-job-card', class_='dhi-job-search-job-card sc-dhi-job-search-job-card-h hydrated')

            for job_card in job_cards:
            
                # Scrapping the required Data
                anchor_tag = soup.find('header', class_='card-header sc-dhi-job-search-job-card-layout-full').find('a', class_='link-label job-title-link util-interactive sc-dhi-job-search-job-card-layout-full')
                job_title = anchor_tag.contents[1].strip()

                company_name = job_card.find('h3', class_='jcl-company-name sc-dhi-job-search-job-card-layout-full').text.strip()

                location = job_card.find('main', class_='card-body')
                job_location = location.find('p', class_='location-display').get_text(strip=True)

                summary = job_card.find('span', class_='job-summary-full p-reg-100 sc-dhi-job-search-job-card-layout-full').text.strip()

                date_of_posting = job_card.find('div', class_='p-reg-75 sc-dhi-time-ago').text.strip()

                # Appending data to lists
                job_titles.append(job_title)
                company_names.append(company_name)
                locations.append(job_location)
                summaries.append(summary)
                posting_dates.append(date_of_posting)
    
    # Getting the required text from the link
    val=re.search(r'q-(.+)-jobs', i)
    csvname = val.group(1).replace('+', ' ')

    # Creating a Unique file name
    csv_filename = '{}.csv'.format(csvname)

    # Creating a CSV file and adding the data
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Job Title','Company Name', 'Location', 'Summary', 'Posting Date'])
        for i in range(len(company_names)):
            writer.writerow([job_titles[i],company_names[i], locations[i], summaries[i], posting_dates[i]])
    
    
    print("Data has been saved to", csv_filename)

                    
    