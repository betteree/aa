import json
import requests

def kakao_api(gps_data):
    lon = gps_data['X']
    lat = gps_data['Y'] 
    
    url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={longitude}&y={latitude}'.format(longitude=lon,latitude=lat)
    headers = {"Authorization": "KakaoAK "+"0e1719d848aa5c31d88702b6f9fca1ff" }
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address_name']
    return str(match_first)


gps_data = {"method":"GPS",
            "X" :"128.80000111622303",
            "Y" :"36.4552517554429",
            }


print(kakao_api(gps_data))