import requests
from datetime import date, timedelta
import json
from google.cloud import storage
from coordinates import co

def create_url_name():
    """
       input: none
       output: returns the raw url path to CSSEGIS covid-19 data on github
    """
    today_date = date.today() - timedelta(days=1)
    today_aslist = (str(today_date)).split('-')
    year, month, day = today_aslist
    covidfilename = month + "-" + day + "-" + year
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    currentUrl = url + covidfilename + ".csv"
    return currentUrl

def create_json_file():
    """
       input: 
       output:

       creates a json file and save to path on the current directory
    """
    covid_19_csv = requests.get(create_url_name())
    covid_19_rowOfRegions = covid_19_csv.text.split('\n')

    if (len(covid_19_rowOfRegions) > 1):
        csv_table_header = covid_19_rowOfRegions[0].split(',')
        csv_table_header_size = len(csv_table_header)
        final_region_list = []

        for regions in covid_19_rowOfRegions[1:]:
            each_region = [x.strip('"') for x in regions.split(',')]
            try:
               regions_as_dict = {
                csv_table_header[j] : each_region[j] for j in range(2, (csv_table_header_size-1)) if csv_table_header[j] != "Last_Update"
            } 
            except IndexError:
                continue 
            if regions_as_dict["Lat"] == "":
                try:
                    regions_as_dict["Lat"] = co[regions_as_dict["Province_State"]][0]
                    regions_as_dict["Long_"] = co[regions_as_dict["Province_State"]][1]
                except KeyError:
                    print(regions_as_dict["Province_State"])
                    continue
            
            if regions_as_dict["Province_State"] == "Bonaire":
                continue

            if regions_as_dict["Country_Region"] == "Korea":
                try:
                    regions_as_dict["Lat"] = regions_as_dict["Long_"]
                    regions_as_dict["Long_"] = regions_as_dict["Confirmed"]
                    regions_as_dict["Confirmed"] = regions_as_dict["Deaths"]
                    regions_as_dict["Deaths"] = regions_as_dict["Recovered"]
                    regions_as_dict["Recovered"] = regions_as_dict["Active"]
                    regions_as_dict["Active"] = int(regions_as_dict["Confirmed"]) - (int(regions_as_dict["Recovered"]) + int(regions_as_dict["Deaths"]))
                except ValueError:
                    print("Value error in Korea data")
                    continue
            
            final_region_list.append(regions_as_dict)

        with open("./04-05-2020.json", 'w') as jsonFile:
            json.dump({"data": final_region_list}, jsonFile)
            print("finished creating file")


def app():
    create_json_file()

if __name__ == "__main__":
    app()
    