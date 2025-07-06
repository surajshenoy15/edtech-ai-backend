from fastapi import FastAPI, HTTPException
from models.user_models import AdaptiveRequest
from services.ai_agentic import generate_adaptive_content
from services.granite_guard import validate_with_granite

app = FastAPI()

@app.post("/adaptive-learning")
async def adaptive_learning(request: AdaptiveRequest):
    try:
        raw_content = generate_adaptive_content(request.user_id, request.topic)
        validated_content = validate_with_granite(raw_content)
        return {"personalized_content": validated_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
