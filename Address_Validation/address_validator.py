##############################################################
#### Written By: ANKHI PAUL                               ####
#### Written On: 2-MAR-2020                               ####
#### Modified On 20-MAR-2020                              ####
#### Objective: To call Google API and validate the       ####
####     		postal code	of a given file               ####
##############################################################

import requests
import csv
import config

# api-endpoint
URL = "https://maps.googleapis.com/maps/api/geocode/json"
f1 = r'C:\Users\H337845\Documents\Laptop to Drive\Studies\Python case studies\Python_Workspace\Problem - Address Validation\employee_demo.txt'
f2 = r'C:\Users\H337845\Documents\Laptop to Drive\Studies\Python case studies\Python_Workspace\Problem - Address Validation\employee_final.txt'
#API key
key = config.api_key

with open(f1, 'r') as f:
    with open(f2,'w+') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Address_line_1", "Postal_Code"])
        writer.writeheader()
        csvfile = csv.DictReader(f, delimiter =',')
        for row in csvfile:

            # defining a params dict for the parameters to be sent to the API
            PARAMS = {'address': row['Address_line_1'],'key': key}

            # sending get request and saving the response as response object
            r = requests.get(url=URL, params=PARAMS)

            # extracting data in json format
            output = r.json()
            correct_postal_code = output['results'][0]['address_components'][7]['long_name']
            row['Postal_Code'] = correct_postal_code
			#writing the correct postal code in an output file
            writer.writerow(row)




