from datetime import date, timedelta

class Covid_19(object):
    def __init__(self, client):
        self.client = client
        self.bucket = self.client.get_bucket("covid-19-sibling")
        
    def get_json(self):
        
        try:
            covid_file = self.get_blobname(1)
            blob = self.bucket.get_blob(covid_file)
            if (blob.exists() == False):
                day = 2
                covid_file = self.get_blobname(day)
                blob = self.bucket.get_blob(covid_file)
        except:
            return None
        return blob

    def get_blobname(self, day=1):
        today_date = date.today() - timedelta(days=day)
        today_aslist = (str(today_date)).split('-')
        year, month, day = today_aslist
        covidfilename = month + "-" + day + "-" + year + ".json"
        return covidfilename
        