def Cesar(input_string,key):
    new_string=""
    for i in range(len(input_string)):
       if input_string[i].isalpha():
           curr_char=input_string[i].lower()
           #do your shifting to curr_char with key and append to a new string.
       elif input_string[i]==' ':
           new_string+=' '
    return new_string
