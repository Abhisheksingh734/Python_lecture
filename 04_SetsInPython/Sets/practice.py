mydict={
    "fast": "Tezz",
    "up": "upar",
    "down": "neeche",
    "look": "dekhna"
}
print("Options are: ",list(mydict))
user=input("Enter the english word\n")
print("The hindi meaning of your word is: ",mydict.get(user)) #.get will not throw error if key is not present in dict


