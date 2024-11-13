def inverte_string_recursiva(s):
   
    if len(s) <= 1:
        return s
   
    else:
        return s[-1] + inverte_string_recursiva(s[:-1])

print(inverte_string_recursiva("olá")) 

