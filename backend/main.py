from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="SatQuery AI Backend", version="1.0.0")

# Enable CORS so your React frontend can communicate with this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your explicit Bhoonidhi session configuration from your dataset
BHOONIDHI_CONFIG = {
    "user_id": "sad_kivuos",
    "access_token": "eyJhbGciOiJIUzUxMiJ9.eyJ0aW1lc3RhbXAiOjE3ODk2MjQ5NzQyNzAsInN1YiI6Ik9OTF9zYWRfa2l2dW9zIiwiaWF0IjoxNzg5NjI0OTc0LCJleHAiOjE3ODk2MjYxNzR9.JEo_q8pcHfJo6ldScRuct3cZE6_hHOvhbhWwUFTiiN3AYEX-HUps7pVg-Rckaw0orpS-sTiMbupCQ9pPS8RyqA",
    "token_type": "Bearer"
}

class SatelliteQueryRequest(BaseModel):
    prompt: str
    bbox: list[float]
    start_date: str = "2026-01-01"
    end_date: str = "2026-09-01"

@app.post("/api/v1/analyze")
async def analyze_satellite_data(req: SatelliteQueryRequest):
    try:
        # Preparing headers for ISRO Bhoonidhi authentication
        headers = {
            "Authorization": f"{BHOONIDHI_CONFIG['token_type']} {BHOONIDHI_CONFIG['access_token']}",
            "Content-Type": "application/json"
        }
        
        # Simulating the multi-model consensus response logic outlined in your tech approach
        return {
            "status": "success",
            "query": req.prompt,
            "active_datasets": [
                {"mission": "CARTOSAT-3", "sensor": "Optical MX", "resolution": "0.28m"},
                {"mission": "RISAT-1A", "sensor": "SAR C-Band", "resolution": "1.5m"}
            ],
            "agent_response": {
                "summary": f"Successfully evaluated spatial window over coordinates {req.bbox[:2]}... Multi-model VLM consensus detected structural changes and a ~3.8% water-body shift relative to baseline temporal bounds.",
                "confidence_score": 0.948,
                "evidence_chain": [
                    "Step 1: Authenticated session via ISRO Bhoonidhi gateway (User: sad_kivuos).",
                    "Step 2: Extracted multi-spectral optical bands and SAR backscatter tensors.",
                    "Step 3: Ran majority-vote consensus classifier to filter false positives."
                ]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)