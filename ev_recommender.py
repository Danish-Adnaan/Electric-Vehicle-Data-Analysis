class EVRecommender:
    def __init__(self,data):
        self.data = data.copy()

    #Filter Dataset by user criteria
    def recommend (self, budget, min_range, min_battery):
        filtered = self.data[(self.data["Minimal price (gross) [PLN]"] <= budget) & (self.data["Range (WLTP) [km]"] >= min_range) & (self.data["Battery capacity [kWh]"] >= min_battery)]
        
        top_ev = filtered.sort_values(by = "Range (WLTP) [km]", ascending = False)

    #Returns Top 5 results
        return top_ev[["Car full name","Make","Minimal price (gross) [PLN]","Range (WLTP) [km]","Battery capacity [kWh]"]].head(3)
        