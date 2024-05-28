from model import DB_API


class PredictPlaceLogic():
    def __init__(self):
        self.__dbAPI = DB_API()
        return
    
    def predict(self, id_patient):
        # gps_data = ['imdang', 'sampung', 'zoyoung']
        
        gps_data:list = self.__dbAPI.get_gps_data(id_patient)
        print("gps",gps_data)
        logic_data = {"method" : "predict",
                      "place1" : gps_data[0] + ',',
                      "place2" : gps_data[1] + ',',
                      "place3" : gps_data[2] + ',',
                      }
        return logic_data
    