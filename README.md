docker exec -i -t bridgeAppApi bash
pip install fastapi[all]
uvicorn main:app --reload --host 0.0.0.0
