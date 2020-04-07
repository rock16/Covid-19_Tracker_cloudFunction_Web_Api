


def downloadcsvtojson(event, context):
    import requests
    from datetime import date, timedelta
    import json
    from google.cloud import storage
    print("starting.......\n")
    #create csv file name
    today_date = date.today() - timedelta(days=1)
    today_aslist = (str(today_date)).split('-')
    year, month, day = today_aslist
    covidfilename = month + "-" + day + "-" + year
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    currentUrl = url + covidfilename + ".csv"

    covid_19_data = ""
    all_regional_data = []
    len_data = 0
    try:
        covid_19_data = requests.get(currentUrl)
    except:
        print("Error fetching Covid-19 data")

    # split text (covid_19_data) to a list (all_regional_data)
    if (covid_19_data == ""):
        return
    else:
        all_regional_data = covid_19_data.text.split('\n')
        len_data = len(all_regional_data)

    if (len_data > 2):
        data_keys = all_regional_data[0].split(',')
        len_data_keys = len(data_keys)
        final_list_data = []
        print("loading.........\n")

        for region in all_regional_data[1:(len_data - 1)]:
            data_values = region.split(',')
            region_dict = {
                data_keys[j]: data_values[j]
                for j in range(0, len_data_keys)
            }
            final_list_data.append(region_dict)

        final_dict_data = {"data": final_list_data}
        with open('/tmp/cov.json', 'w') as outfile:
            json.dump(final_dict_data, outfile)

        storage_client = storage.Client()
        bucket = storage_client.get_bucket("covid-19-sibling")
        blob = bucket.blob(covidfilename + ".json")

        if (blob.exists() == False):
            with open('/tmp/cov.json', 'r') as json_file:
                blob.upload_from_file(json_file)
            print("finished")
            return "success"
    else:
        print("File not found")

    return "Failure"
