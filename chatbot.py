
from utilities import _predict_class , intents , _get_response 


print ( "------Bot is running------ !")

while True : 

    message=input("You: ")
    if message=="quit":
        break 
    else :
        ints = _predict_class(message)
        res =_get_response(ints , intents )
        print(res)

