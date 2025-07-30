class Loan:
    def __init__(self,schemaNo, schemeName, schemeType, schemeEligibility, schemeUpdated, schemeRoi, schemeMaxAmount):
        self.schemeNo = schemaNo
        self.schemeName = schemeName
        self.schemeType = schemeType
        self.schemeEligibility = schemeEligibility
        self.schemeUpdated = schemeUpdated
        self.schemeRoi = schemeRoi
        self.schemeMaxAmount = schemeMaxAmount
    def __str__(self):
        return "Scheme Details: number: "+str(self.schemeNo)+" name: "+self.schemeName+" type: "+self.schemeType+" eligible: "+self.schemeEligibility+" updated: "+str(self.schemeUpdated)+" ROI: "+str(self.schemeRoi)+" max amount "+str(self.schemeMaxAmount)+"\n"
        