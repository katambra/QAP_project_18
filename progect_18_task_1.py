# получить данные о питомцах с сайта http://130.193.37.179/app/pets в формате json и отсортировать полные данные питомцев по полу и по имени, вывести на печать отсортированные имя и пол животного

import pandas as pd   # подключаем модуль pandas для парсинга инфо с сайта
data = pd.read_json('http://130.193.37.179/api/pet/') # в панели разработчика находим нужный запрос, используем его с pandas

newdata = data["results"] # изучив ответ на запрос в панели видим, что нам нужен только блок results
newdata = sorted(sorted(newdata, key = lambda s: s['name']), key = lambda s: s['gender']['name']) # сотрируем блок results в соответствии с заданием: сначала пол, потом имя

for i in range(len(newdata)): # выводим на печать искомые данные
    print(newdata[i]['name'], " - ",  newdata[i]['gender']['name'])
    