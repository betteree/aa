from model.database import DB_API
import requests
import json

class GPSSaveLogic():
    def __init__(self):
        self.__count = 0
        self.__db = DB_API()
        return
    
    def is_save_GPS(self, gps_data:dict):
        
        if self.__count < 5:
            self.__count += 1
            return
        #id_patient = gps_data['ID']  
        load_name = self.__kakao_api(gps_data)
        self.__db.save_gps_data(load_name)
        print("gps 저장합니다요 : ", load_name)
        self.__count = 0
        return
    

    def __kakao_api(self,gps_data:dict):
        lon = gps_data['X']
        lat = gps_data['Y'] 
        
        url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={longitude}&y={latitude}'.format(longitude=lon,latitude=lat)
        headers = {"Authorization": "KakaoAK "+"0e1719d848aa5c31d88702b6f9fca1ff" }
        result = json.loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address_name']
        return str(match_first)
    
    
    # def __tmap_api(self, gps_data):
    #     lon = gps_data['x']
    #     lat = gps_data['y']
        
    #     api_url = "https://apis.openapi.sk.com/tmap/geo/reversegeocoding?version=1&format=json&callback=result",
        
    #     # 전송할 데이터 (헤더)
    #     headers = {
    #         "accept": "application/json",  # JSON 형식으로 데이터
    #         "appKey": TMAP_APPKEY,  # 인증 토큰
    #         "content-type":"application/json"
    #     }
    
    #     """ headers
    #     - accept : application/json
    #     - appKey : 발급 Appkey
    #     - content-type : application/json
    #     """

    #     body : {
    #         "coordType" : "WGS84GEO",
    #         "addressType" : "A10",
    #         "lon" : lon,
    #         "lat" : lat
    #     }
        
    #     response = requests.post(api_url, headers=headers, json=body)
    #     response = response.json()
        
    #     return response
        
        
        
        
        
        
        
        