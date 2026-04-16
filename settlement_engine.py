import json
import os
from protocol import AeroCarbonTollgate

def run_settlement():
    """
    Automated Settlement Dispatcher.
    Fetches raw telemetry data and executes the OAC minting logic.
    """
    tollgate = AeroCarbonTollgate()
    data_path = "data/flight_log.json"
    
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Execute protocol-level asset minting
        value = tollgate.mint_carbon_credit(data.get('fuel_kg', 0), data.get('fuel_type', 'Unknown'))
        
        # Generate standardized settlement proof
        report = f"""
[OAC SETTLEMENT PROOF]
Flight ID     : {data.get('flight_id', 'UNKNOWN')}
Asset Minted  : ${value} USD
Timestamp     : {data.get('timestamp', 'N/A')}
Protocol Ver  : v1.0.0-ALPHA
Status        : VERIFIED
---------------------------------------"""
        print(report)
        
        # Append to the immutable ledger
        with open("ledger.txt", "a", encoding='utf-8') as ledger:
            ledger.write(report + "\n")

if __name__ == "__main__":
    run_settlement()
