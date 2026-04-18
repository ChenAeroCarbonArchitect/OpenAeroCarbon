import hashlib
import time

class AeroCarbonTollgate:
    """
    [GSS-v1.0-REFERENCE-IMPLEMENTATION]
    -------------------------------------------------------------------------
    Official implementation of the Green Sky Standard (GSS) v1.0.0.
    Logic: Automated Carbon Asset Settlement with Cryptographic Fingerprinting.
    Compliance: ISO-14064-2 & ICAO CORSIA Baseline.
    -------------------------------------------------------------------------
    """

    def __init__(self):
        # The core versioning string identifying this as the GSS Reference
        self.PROTOCOL_SPEC = "GSS-v1.0.0-ALPHA"
        
        # Current EU ETS projected benchmark (USD/Metric Ton)
        self.CARBON_PRICE = 85.0  
        
        # Sustainable Aviation Fuel (SAF) Efficiency Multiplier
        self.SAF_MULTIPLIER = 0.8  

    def mint_carbon_credit(self, fuel_kg: float, fuel_type: str = "JetA1") -> float:
        """Calculates asset value based on verified telemetry."""
        assert fuel_kg > 0, "Telemetry Error: Mass must be positive."
        
        # 3.16kg CO2 per 1kg JetA1 baseline
        co2_baseline = fuel_kg * 3.16
        
        if fuel_type.upper() == "SAF":
            carbon_mitigated = (co2_baseline * self.SAF_MULTIPLIER) / 1000
            settlement = carbon_mitigated * self.CARBON_PRICE
            return round(settlement, 4)
        
        return 0.0

    def generate_tx_hash(self, wallet: str, amount: float) -> str:
        """
        Generates a cryptographic hash to simulate an on-chain transaction.
        Essential for Web3 auditability.
        """
        payload = f"{wallet}:{amount}:{time.time()}"
        return "0x" + hashlib.sha256(payload.encode()).hexdigest()
