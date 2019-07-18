favFruits= ["mango", "avcado","pineapple","grapes","pomogranate"]
print(favFruits)
favFruits.append("orange")
print(favFruits) 
eniesFav = favFruits[2]
print(eniesFav)
# favFruits.pop(2)
# print (favFruits)
# favFruits.remove("pineapple")
# print (favFruits)
favFruits[2]= "apple"
print(favFruits)


for fruit in range(0,len(favFruits)):
    print("I like " + favFruits[fruit]) 
    
# fruitCriteria=[True, 0.20, True, True, 100, "Banana", True]
fruitCriteria = {"isFresh": True,
    "costPerPound": 0.20,
    "isRipe": True,
    "inSeason": True,
    "howMuchLike": 100,
    "whatIsIt": "banana",
    "isAllergic": True

fruitCriteria["specialFeature"] = "GMO"

print(fruitCriteria)

for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + ".")
    
print(fruitCriteria["specialFeature"])
Collapse



