import os
from dotenv import load_dotenv
from mysql.connector import *
from model import Loan

load_dotenv()

class LoanMySQLService:
    def __init__(self):
        self.connection = connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.table = os.getenv("DB_TABLE")
        self.isTableExists()
    def getMessage(self, key,**kwargs):
        return os.getenv(key,"").format(**kwargs)
    def isTableExists(self):
        qry = "create table if not exists loans(schemeNo bigint primary key,schemeName varchar(255),schemeType varchar(255),schemeEligibility varchar(255),schemeUpdated date,schemeRoi float,schemeMaxAmount bigint)"
        self.cursor.execute(qry)
        self.connection.commit()
        print(os.getenv("MSG_TABLE_OK"))
    def introduceScheme(self,loan):
        try:
            qry = f"insert into {self.table} values({loan.schemeNo},'{loan.schemeName}','{loan.schemeType}','{loan.schemeEligibility}','{loan.schemeUpdated}',{loan.schemeRoi},{loan.schemeMaxAmount})"
            self.cursor.execute(qry)
            print(self.getMessage("MSG_LOAN_CREATE_OK",schemeName=loan.schemeName))
            self.connection.commit()
        except Exception as e:
            print(self.getMessage("MSG_LOAN_CREATE_DUPLICATE",schemeName=loan.schemeName,schemeNo=loan.schemeNo))
    def viewScehemes(self):
        qry = f"select * from {self.table}"
        self.cursor.execute(qry)
        loans = self.cursor.fetchall()
        for loan in loans:
            print(self.getMessage("MSG_VIEW_LOAN",scheme=loan))
        
service = LoanMySQLService()
# service.introduceScheme(Loan(727362,"StartUp","Business","Incorporates",'2023-01-20',7.1,500000))
service.viewScehemes()