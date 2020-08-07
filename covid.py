import COVID19Py as cp 
covid = cp.COVID19(data_source="jhu")
location = covid.getLocationByCountryCode("IN")
mylist = location
print(mylist)
