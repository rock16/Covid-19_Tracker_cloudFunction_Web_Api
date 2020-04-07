from flask import Flask, abort
from flask_restplus import Resource, Api
from covid_19_file import Covid_19
from google.cloud import storage 
import ndjson

app = Flask(__name__)
api = Api(app)



@api.route('/v1/covid-19-json')
class Covid_19_json_endpoint(Resource):
    def get(self):
        covid_19 = Covid_19(storage.Client())
        covid_19_blob = covid_19.get_json()
        if(covid_19_blob != None and covid_19_blob.exists() == False):
            abort(400, "No such data found")
        elif(covid_19_blob == None):
            return "Error fetching file"
        return ndjson.loads(covid_19_blob.download_as_string())

if __name__ == '__main__':
    app.run()