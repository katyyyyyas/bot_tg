def transcriptor (name:str)->str:
    name = name.upper()
    alphabet={'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G',
     'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 
     'З': 'Z','И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 
     'М':'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 
     'С':'S', 'Т': 'T', 'У':'U', 'Ф': 'F', 'Х': 'KH', 
     'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 
     'Ы': 'Y','Ъ': 'IE','Ь':'', 'Э': 'E', 'Ю': 'IU', 
     'Я': 'IA'}
    res = ''
    for i in name:
        res = res + alphabet.get(i,i)
    return res
