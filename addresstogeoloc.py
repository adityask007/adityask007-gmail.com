import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="tql")

z=""
x=""
cord=""
cord1=""
tc=""
data=pd.read_csv("address.csv",encoding='latin1')
l=[]
total=len(data)
for i in range(12936,total):
        z=str(data.iloc[i,5])
        x=x+z
        location = geolocator.geocode(z)
        if(location is not None):
                cord=str(location.latitude)
                cord1=str(location.longitude)
                print(cord+','+cord1)
                
   

        

