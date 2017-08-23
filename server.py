import os
import sys
import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/events', methods=['POST'])
def events():
    
    location = request.form['location']
    events = requests.get(
        "https://www.eventbriteapi.com/v3/events/search/?token=GVWIY2SUJRAJJQJFVKP4&expand=venue,start,logo&location.within=5km&location.address=" + location

    )

    data = events.json()
    return data['events'][0]['name']['text']


    # return render_template('events.html')

@app.route('/')
def index():

    return render_template('index.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
