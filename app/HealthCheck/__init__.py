from flask import Flask,jsonify

app = Flask(__name__) 

from HealthCheck import views