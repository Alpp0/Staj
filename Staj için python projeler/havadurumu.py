import requests
import datetime
import json
apiKey = '10d816fd2ad802ecc70b04f152c75208'
sehirİsmi=input("Şehir İsmi Giriniz")
orgin_url=(f'http://api.openweathermap.org/data/2.5/weather?q={sehirİsmi}&appid={apiKey}')
response = requests.get(orgin_url)
jsonResponse=json.loads(response.text)
skyDescription = jsonResponse['weather'][0]['description']
skyTypes = ['clear sky', 'few clouds', 'overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain',
            'thunderstorm', 'snow', 'mist','light rain']
skyTypesTR = ['Güneşli', 'Az Bulutlu', 'Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu',
              'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Sisli','Hafif Yağmurlu']
for i in range(len(skyTypes)):
    if skyDescription == skyTypes[i]:
        skyDescription = skyTypesTR[i]
        
temp = round((jsonResponse['main']['temp'] - 273.15), 2) 
feels_temp = round((jsonResponse['main']['feels_like'] - 273.15), 2)  
temp_min = round((jsonResponse['main']['temp_min'] - 273.15), 2)  
temp_max = round((jsonResponse['main']['temp_max'] - 273.15), 2)  
cloud_rate=jsonResponse['clouds']['all'] 
humidity=jsonResponse['main']['humidity'] 
sunset_unix=jsonResponse["sys"]["sunset"] 
sunrise_unix=jsonResponse["sys"]["sunrise"] 
datatime = jsonResponse["dt"]

sunset=datetime.datetime.fromtimestamp(sunset_unix).strftime(' %H:%M:%S')
sunrise=datetime.datetime.fromtimestamp(sunrise_unix).strftime(' %H:%M:%S')
datatime_real=datetime.datetime.fromtimestamp(datatime).strftime('%d-%m-%y %H:%M:%S')


print("Sehir: "+ jsonResponse["name"])
print("Verinin Alındığı Tarih-Saat:"+datatime_real)
print("Gökyüzü:"+skyDescription)
print("Hava Sıcaklığı: "+str(temp)+" C")
print("Hissedilen Hava Sıcaklığı: "+str(feels_temp)+" C")
print("Minumum Sıcaklık: "+str(temp_min)+" C")
print("Maksimum Sıcaklık "+str(temp_max)+" C")
print("Nem Oranı : %"+str(humidity))
print("Bulutluluk Oranı:%"+str(cloud_rate))
print("Gün Batımı: "+sunset)
print("Gün Doğumu:"+sunrise)