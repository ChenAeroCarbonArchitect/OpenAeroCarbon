from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from protocol import AeroCarbonTollgate
import uvicorn

# --- API Metadata ---
app = FastAPI(
    title="OAC Global Settlement API",
    description="Decentralized Carbon Credit Minting Engine for SAF.",
    version="1.0.0"
)

# --- Data Models ---
class FlightData(BaseModel):
    flight_id: str
    fuel_kg: float
    fuel_type: str
    operator: str = "Anonymous"

# Initialize our money-making logic
tollgate = AeroCarbonTollgate()

@app.get("/")
async def root():
    return {"status": "ONLINE", "protocol": "OAC-V1", "message": "Code is Law."}

@app.post("/mint")
async def mint_credit(data: FlightData):
    """
    The Money Endpoint:
    Receives flight data -> Validates via Protocol -> Returns Asset Value.
    """
    try:
        # Business Logic Execution
        asset_value = tollgate.mint_carbon_credit(data.fuel_kg, data.fuel_type)
        protocol_fee = round(asset_value * 0.01, 4) # Our 1% cut
        
        return {
            "flight_id": data.flight_id,
            "verification_status": "SUCCESS",
            "minted_value_usd": asset_value,
            "protocol_fee_usd": protocol_fee,
            "ledger_hash": "0x" + os.urandom(16).hex() # Simulated Proof of Custody
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
