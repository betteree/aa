from model.database import DB_API
import requests

class GPSSaveLogic():
    def __init__(self):
        self.__count = 0
        self.__db = DB_API()
        return
    
    def is_save_GPS(self, gps_data:dict):
        if self.__count < 5:
            self.__count += 1
            return
        
        #api_data = self.__tmap_api(gps_data)
        #load_name = api_data["addressInfo"]['roadName']
        load_name = "imdang"
        #self.__db.save_gps_data(gps_data)
        print("gps 저장합니다요 : ", load_name)
        self.__count = 0
        
        return
    
    def __tmap_api(self, gps_data):
        lon = gps_data['x']
        lat = gps_data['y']
        
        api_url = "https://apis.openapi.sk.com/tmap/geo/reversegeocoding?version=1&format=json&callback=result",
        
        # 전송할 데이터 (헤더)
        headers = {
            "accept": "application/json",  # JSON 형식으로 데이터
            "appKey": TMAP_APPKEY,  # 인증 토큰
            "content-type":"application/json"
        }
    
        """ headers
        - accept : application/json
        - appKey : 발급 Appkey
        - content-type : application/json
        """

        body : {
            "coordType" : "WGS84GEO",
            "addressType" : "A10",
            "lon" : lon,
            "lat" : lat
        }
        
        response = requests.post(api_url, headers=headers, json=body)
        response = response.json()
        
        return response
        
        
        
        
        
        
        
        