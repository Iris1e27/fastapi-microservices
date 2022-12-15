# fastapi-microservices

You need to open many terminals.

- cd inventory
- pip install -r requirements.txt
- uvicorn main:app --reload

- cd payment
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8001

- cd user
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8002

- cd inventory-frontend
- npm install package.json
- npm start

- cd inventory
- python consumer.py

- cd payment
- python consumer.py
