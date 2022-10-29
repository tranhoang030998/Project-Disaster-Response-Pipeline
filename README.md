# Disaster Response Pipeline Project

# Project: Disaster Response Pipeline

- I've learned and developed my data engineering abilities in this course, which will increase my possibilities and potential as a data scientist. In order to create a model for an API that categorizes disaster messages, I'll use these abilities in this project to evaluate disaster data from Appen.

## Project Structure:

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- DisasterResponse.db   # database to save clean data to

- models
|- train_classifier.py

- README.md

## Instruction:

- Run the following commands in the project's root directory to set up your database and model.

	+ To run ETL pipeline that cleans data and stores in database ```python data/process_data.py``` data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
	+ To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
- Go to app directory: cd app

- Run your web app: python run.py

- Go to http://0.0.0.0:3000/
