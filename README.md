# CalcPal---Flask-Application

## Build the Docker Image
docker build -t dyscalculia-flask-app .

## Run the Docker Container
docker run --name dyscalculia-flask-container -p 5001:5001 dyscalculia-flask-app

## Sending a POST request to the Verbal model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 9, \"IQ\": 5, \"Q1\": 0, \"Q2\": 0, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/verbal

## Sending a POST request to the Lexical model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/lexical

## Sending a POST request to the Sequential model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/sequential

## Sending a POST request to the Visual model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/visual

## Sending a POST request to the Ideognostic model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/ideognostic

## Sending a POST request to the Operational model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/operational

## Sending a POST request to the Graphical model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/graphical

## Sending a POST request to the Practognostic model prediction endpoint
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 10, \"IQ\": 4, \"Q1\": 1, \"Q2\": 1, \"Q3\": 1, \"Q4\": 1, \"Q5\": 0, \"Time Seconds\": 287}" http://localhost:5001/practognostic