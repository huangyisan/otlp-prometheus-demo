# Monitor-Flask-App-metrics-with-Prometheus-format

## Steps to run Flask app
1. Activate your virtual environment (if not already activated)
```
source venv/bin/activate   # On macOS or Linux
```
2. Install required packages
```
python -m pip install flask prometheus_flask_exporter
python -m pip install requests
```
3. Start the flask application
```
python app.py
```
4. In a new terminal, start the generator
```
python app-generator.py
```
It will be used in generating request for the Flask application at the different endpoints.

5. Send the metrics to a monitoring tool for visualization. You can do this with OpenTelemetry and SigNoz, read the article here.