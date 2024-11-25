import csv
import json

d1 = []

with open('data.csv','r') as file:
    csvFile = csv.DictReader(file)
    for i in csvFile:
        d1.append(i)
dt = {}

print(d1)

for i in d1:
    if i['Entity'] not in dt:
        dt[(i['Entity'])] = {
            'Code': i['Code'],
            i['Year']:{
                    'Other':i['Other renewables excluding bioenergy - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Bioenergy':i['Electricity from bioenergy - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Solar':i['Electricity from solar - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Wind':i['Electricity from wind - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Hydro':i['Electricity from hydro - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Nuclear':i['Electricity from nuclear - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Oil':i['Electricity from oil - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Gas':i['Electricity from gas - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Coal':i['Electricity from coal - TWh (adapted for visualization of chart electricity-prod-source-stacked)']
            }
        }
    else:
        dt[i['Entity']][i['Year']] = {'Other':i['Other renewables excluding bioenergy - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Bioenergy':i['Electricity from bioenergy - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Solar':i['Electricity from solar - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Wind':i['Electricity from wind - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Hydro':i['Electricity from hydro - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Nuclear':i['Electricity from nuclear - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Oil':i['Electricity from oil - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Gas':i['Electricity from gas - TWh (adapted for visualization of chart electricity-prod-source-stacked)'],
                    'Coal':i['Electricity from coal - TWh (adapted for visualization of chart electricity-prod-source-stacked)']}

with open('data.json','w') as wfile:
    json.dump(dt,wfile,indent = 4)