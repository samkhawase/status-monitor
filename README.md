# status-monitor
Flask project for monitoring Magnificient API endpoint

## Instructions to run the project
- (Optional) Initialize virtual environment and activate it.
- Install dependencies using `pip install -r requirements.txt`
- run the app using `flask run`

The app will continously monitor the availability of the API endpoint and will log the data to the file under `logs/app.log` file.

The app will also serve a status page at `http://localhost:5000` to show the latest status of the magnificient API endpoint.


