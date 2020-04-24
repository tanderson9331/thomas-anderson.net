# Import OS to get environment variables
import os
import datetime

# Get Flask and associated modules
from flask import Flask, request, jsonify, abort, render_template

# Import Google API Client
from googleapiclient.discovery import build

# Define the Flask app name from the filename
site = Flask(__name__)

# Get environment, and default to Development
env = os.environ.get('appenv', 'Local')
rev = os.environ.get('K_REVISION', 'No revision')

################
# Begin Routes #
################

# Root
@site.route('/')
def main():
    return render_template('index.html')
