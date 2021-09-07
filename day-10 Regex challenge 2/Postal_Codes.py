import re

#find the city names from given text file
largest_cities_file = open('largest_cities_germany.txt',encoding=('UTF-8'))

largest_cities_data = largest_cities_file.readlines()

# extract all the 19 largest cities

regex_19_cities = re.compile('\s[\w\s]+\s+')


city_names_list = []

for city_data in largest_cities_data:
    city_name = regex_19_cities.findall(city_data)[0]
    city_names_list.append(city_name.strip())






cities_postal_data_file=open('postal_codes_germany.txt','r')
cities_postal_data=cities_postal_data_file.read()





city_postal_codes_dict = {}





for city in city_names_list:

    regex_exp = '\s'+city+'\s[\d]+\s'
    city_matches =  (re.findall(regex_exp,cities_postal_data)[0:3])
    #covert the city matches list to str
    city_matches_str = "".join(city_matches)
    
    
    city_postal_codes_dict[city] = re.findall(r'[0-9]+', city_matches_str)
    
    
print (city_postal_codes_dict)












