import requests
import json
APIKEY='your api key'
class WhetherApp:
    def __init__(self):
        self.location=input('enter the location: ')
    def get_lon_lat(self):
        if self.location:
            try:
                coordinate=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={self.location}&appid={APIKEY}')
                coordinate_data=json.loads(coordinate.content.decode('utf-8'))
                if not coordinate_data:
                    raise ValueError('error in fetch api')
                lat=coordinate_data[0]['lat']
                lon=coordinate_data[0]['lon']
                if not lat:
                    raise ValueError('lat not found')
                if not lon:
                    raise ValueError('lat not found')
                return lat,lon
            except Exception as e:
                print('give a valid location',e)
        else:
            raise ValueError("Location not provided")
        
    def get_whether_response(self):
        lat,lon=self.get_lon_lat()
        if not lat:
            raise ValueError('lat not found')
        if not lon:
            raise ValueError('lat not found')
        try:
            whether_information=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}')
            w_data=json.loads(whether_information.content.decode("utf-8"))
            if w_data:
                print(w_data['weather'][0]['description'])
            else:
                raise ValueError('error to get whether response')
        except Exception as e:
            print('lat lon not valid ',e)

if __name__=='__main__':
    whether_obj=WhetherApp()
    whether_obj.get_whether_response()
