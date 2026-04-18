from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from protocol import AeroCarbonTollgate

app = FastAPI(title="OAC Web3 Settlement Infrastructure")
tollgate = AeroCarbonTollgate()

class FlightData(BaseModel):
    flight_id: str
    fuel_kg: float
    fuel_type: str
    payout_address: str # Web3 Wallet for asset liquidation

@app.get("/")
async def root():
    return {
        "status": "ONLINE",
        "standard": "GSS-v1.0.0-REFERENCE",
        "protocol": "OAC-V1.1-WEB3",
        "message": "Code is Law.Efficiency is the only audit."
    }

@app.post("/mint")
async def mint_credit(data: FlightData):
    try:
        asset_value = tollgate.mint_carbon_credit(data.fuel_kg, data.fuel_type)
        # Generate the digital fingerprint
        tx_hash = tollgate.generate_tx_hash(data.payout_address, asset_value)
        
        return {
            "flight_id": data.flight_id,
            "minted_value_usd": asset_value,
            "payout_wallet": data.payout_address,
            "on_chain_tx_hash": tx_hash,
            "status": "SETTLED_ON_CHAIN"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
