from flask import Flask, render_template, Response
import threading
from lib import dht

class api:
    def __init__(self, dht: dht):
        self.dht = dht
        self.app = Flask(__name__)
        self.app.add_url_rule("/dht", "dht", self.get_dht_data)
        self.app.add_url_rule("/", "index", self.indexhtml)
    
    def run_async(self):
        threading.Thread(target=self.app.run, args=()).start()
        
    def indexhtml(self):
        return render_template('index.html') 

    def get_dht_data(self):
        return Response(self.dht.data.toJSON(), mimetype="application/json")