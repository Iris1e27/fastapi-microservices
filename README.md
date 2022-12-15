# fastapi-microservices

You need to open many terminals.
1. 
- cd inventory
- pip install -r requirements.txt
- uvicorn main:app --reload
2. 
- cd payment
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8001
3. 
- cd user
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8002
4. 
- cd inventory-frontend
- npm install package.json
- npm start
5. 
- cd inventory
- python consumer.py
6. 
- cd payment
- python consumer.py
