import math

class AeroCarbonTollgate:
    """
    Protocol: OpenAeroCarbon (v1.0.0-alpha)
    Description: Automated Carbon Credit Settlement System for Sustainable Aviation Fuel (SAF).
    Goal: Eliminate middlemen and monetize aviation decarbonization.
    """
    def __init__(self):
        # Current EU ETS (Emissions Trading System) benchmark price in USD
        self.carbon_tax_rate = 85.0  
        # Lifecycle reduction efficiency of SAF (Standard: 80%)
        self.saf_efficiency_gain = 0.8  

    def calculate_on_chain_credit(self, fuel_consumed_kg, fuel_type="JetA1"):
        """
        Input: Physical sensor data from engine (fuel mass flow)
        Output: Digital Carbon Credit (USD value)
        """
        # Standard Jet A-1 emission factor: 3.16kg CO2 per 1kg fuel
        raw_co2_emission = fuel_consumed_kg * 3.16
        
        if fuel_type == "SAF":
            # Quantifying actual environmental impact
            carbon_saved_tons = (raw_co2_emission * self.saf_efficiency_gain) / 1000
            # Financial settlement logic
            credit_value = carbon_saved_tons * self.carbon_tax_rate
            return round(credit_value, 4)
        
        return 0.0

# --- LIVE SETTLEMENT DEMO ---
# Simulate a long-haul flight consuming 50 tons of SAF
tollgate = AeroCarbonTollgate()
settlement_value = tollgate.calculate_on_chain_credit(50000, "SAF")

print(f"--- [Protocol Status: ONLINE] ---")
print(f"Verified Carbon Credits: ${settlement_value}")
print(f"Protocol Service Fee (1%): ${round(settlement_value * 0.01, 4)}")
print(f"Logic: Code is Law. Every drop of fuel is now a digital asset.")
