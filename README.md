# Monitor-Flask-App-metrics-with-Prometheus-format
This is a simple Flask application that exposes metrics in Prometheus format using the [prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter).
To run the app, you need to have Python and pip installed on your machine, then install the required dependencies.

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
The different endpoints for the application are `127.0.0.1:5000/one`, `127.0.0.1:5000/two`, `127.0.0.1:5000/three`, `127.0.0.1:5000/four` and `127.0.0.1:5000/error`.

4. In a new terminal, start the generator
```
python app-generator.py
```
It will be used in generating request for the Flask application at the different endpoints.

5. Send the metrics to a monitoring tool for visualization. You can do this with OpenTelemetry and SigNoz, read the article [here](https://signoz.io/blog/opentelemetry-collector-prometheus-receiver/).

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cbzf58qelvvm2tmb4mn6.png)
