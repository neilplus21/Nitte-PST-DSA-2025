import os
from dotenv import load_dotenv
from model import Loan
from pickle import *

load_dotenv()

class LoanFileService:
    def __init__(self):
        self.file = os.getenv("DATA_FILE")
    def getMessage(self, key,**kwargs):
        return os.getenv(key,"").format(**kwargs)
    def loadLoans(self):
        loans = [] # temporay to hold list of loans from file
        if os.path.exists(self.file):
            with open(self.file,"rb") as current:
                received = load(current)
                loans.extend(each for each in received)
        return loans
    def alterLoans(self,loans=[]):
        with open(self.file,"wb") as current: dump(loans,current)
    def introduceScheme(self,loan):
        received = self.loadLoans()
        if any(loan.schemeNo == each.schemeNo for each in received):
            print(self.getMessage("MSG_LOAN_CREATE_DUPLICATE",schemeName=loan.schemeName,schemeNo=loan.schemeNo))
            return
        received.append(loan)
        print(self.getMessage("MSG_LOAN_CREATE_OK",schemeName=loan.schemeName))
        self.alterLoans(received)
    def viewScehemes(self):
        received = self.loadLoans()
        for loan in received:
            print(self.getMessage("MSG_VIEW_LOAN",scheme=loan))
    def modifySchemes(self,loan):
        updates = {}
        if loan.schemeName: updates["schemeName"]=loan.schemeName
        if loan.schemeType: updates["schemeType"]=loan.schemeType
        if loan.schemeEligibility: updates["schemeEligibility"]=loan.schemeEligibility
        if loan.schemeUpdated: updates["schemeUpdated"]=loan.schemeUpdated
        if loan.schemeRoi: updates["schemeRoi"]=loan.schemeRoi
        if loan.schemeMaxAmount: updates["schemeMaxAmount"]=loan.schemeMaxAmount
        received = self.loadLoans()
        for each in received:
            if each.schemeNo == loan.schemeNo:
                if "schemeName" in updates: each.schemeName=loan.schemeName
                if "schemetype" in updates: each.schemeType=loan.schemetype
                if "schemeEligibility" in updates: each.schemeEligibility=loan.schemeEligibility
                if "schemeUpdated" in updates: each.schemeUpdated=loan.schemeUpdated
                if "schemeRoi" in updates: each.schemeRoi=loan.schemeRoi
                if "schemeMaxAmount" in updates: each.schemeMaxAmount=loan.schemeMaxAmount
                self.alterLoans(received)
                print(self.getMessage("MSG_UPDATE_OK",schemeNo=loan.schemeNo))
                return
        print(self.getMessage("MSG_UPDATE_FAIL",schemeNo=loan.schemeNo))
    def discontinue(self,schemeNo):
        received = self.loadLoans()
        updatedLoans=[loan for loan in received if loan.schemeNo!=schemeNo]
        if len(received) == len(updatedLoans):
            print(self.getMessage("MSG_DELETE_NOT_OK",schemeNo=schemeNo))
        else:
            self.alterLoans(updatedLoans)
            print(self.getMessage("MSG_DELETE_OK",schemeNo=schemeNo))
            
    

# service = LoanFileService()
# print(service.loadLoans())
# service.alterLoans()
# service.introduceScheme(Loan(711111,"ICICI Personal Care","Personal","Salaried",'2023-01-20',16.1,200000))
# loan = Loan(7777777)
# loan.schemeMaxAmount=1200000
# loan.schemeType="business"
# loan = Loan(727362)
# loan.schemeMaxAmount=700000
# loan.schemeType="business"
# loan.schemeName="Unicorns"
# service.modifySchemes(loan)
# service.discontinue(827382783)
# service.discontinue(727362)
# service.viewScehemes()