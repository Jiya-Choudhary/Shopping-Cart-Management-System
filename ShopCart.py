print("Your Shopping Cart")
dict ={"Trouser": 2222, "SoftToy": 3456 , "Bracelet":1286}
print("You Added :" , dict)
List = ["Trouser","SoftToy","Bracelet" ]
Options = ["Add","Remove","Total Bill","Exit"]
print(Options)
Select = input("Enter option:")
for option in Options:
 if Select == "Add":
   Items = input("Enter items:")
   if Items in dict:
      dict[Items] = dict[Items] * 2
      print("Item already exists! , Doubled the price.")
      print(dict)
      print(List)
      print(Options)
      Select = input("Enter option:")
   else:
        price = int(input("Enter price:"))
        dict[Items] = price
        print(dict)
        List.append(Items)
        print("Added new Item")
        print(List)
   print(Options)
   Select = input("Enter option:")
 elif Select == "Remove":
    Items = input("Enter items:")
    if Items in List:
        List.remove(Items)
        del dict[Items]
        print(List)
        print(dict)
    print(Options)
    Select = input("Enter option:")
 elif Select == "Total Bill":
    total = sum(dict.values())
    print("Total Bill is:",total)
    print(Options)
    Select = input("Enter option:")
 elif Select == "Exit":
    print("Closed")
    break
 else:
    print("Select Again")
    Select = input("Enter option:")
