import datetime
from LoanDbDao import *
from model import Loan
class LoanService:
    def __init__(self,source="db"):
        if source == "db": self.repo = LoanMySQLService()
    def introduce(self,no,name,type,elig,up,roi,amount):
        loan = Loan(no)
        loan.schemeName=name
        loan.schemeType=type
        loan.schemeEligibility=elig
        loan.schemeRoi=roi
        loan.schemeMaxAmount=amount
        loan.schemeUpdated=up
        self.repo.introduceScheme(loan)
    def view(self): 
        self.repo.viewScehemes()
    def modify(self, **kwargs):
        if "schemeNo" in kwargs.keys():
            loan = Loan(kwargs["schemeNo"])
            fields = [each for each in kwargs.keys()]
            values = [each for each in kwargs.values()]
            for index in range(len(fields)):
                if fields[index] == "name": loan.schemeName=values[index]
                elif fields[index] == "type": loan.schemeType=values[index]
                elif fields[index] == "elig": loan.schemeEligibility=values[index]
                elif fields[index] == "updated": loan.schemeUpdated=values[index]
                elif fields[index] == "roi": loan.schemeRoi=values[index]
                elif fields[index] == "amount": loan.schemeMaxAmount=values[index]
            self.repo.modifySchemes(loan)
        else: print(self.repo.getMessage("MSG_UPDATE_FAIL"))
    def discontinue(self,schemeNo):
        self.repo.discontinue(schemeNo)
        
      
# service = LoanService()
# # service.introduce(121121,"PNJAY","Personal","Salaried",17.1,200000)
# # service.view()
# service.modify(**{"schemeNo":1212,"name":"STARTUPIN","roi":9.2})
# service.modify(**{"schemeNo":121121,"name":"STARTUPIN","roi":9.2,"amount":12900})
# service.modify(**{"name":"STARTUPIN","roi":9.2,"amount":12900})
# service.discontinue(121121)