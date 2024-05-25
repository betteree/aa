from model import DB_API


class ImformationPatient():
    def __init__(self):
        self.__dbAPI = DB_API()
        return
    
    def patient_imformation(self,id_patient):
        imformation_patient:list = self.__dbAPI.imfomation_data()

        logic_data = {"method" : "predict",
                      "name" : imformation_patient[0],
                      "address" : imformation_patient[1],
                      "guardianNumber" : imformation_patient[2],
                      }
        return logic_data
    