mesVehicules = {
    50021:["Toyota", "Corolla", 2015, [12, "Sheppard ave", "Toronto"]],
    50022:["Mazda", "CX-9", 2019, [1, "Yong Street", "Toronto"]],
    50023:["Nissan", "Pathfinder", 2020, [98, "Laird ave", "Toronto"]],
    50024:["Mercedes-Benz", "C class", 2018, [75, "Frontenac Drive", "Markham"]],
    50025:["Hyundai", "Tucson", 2017, [12, "Rue Berry", "Montreal"]],
    50026:["Kia", "Sportage", 2020, [150, "Sheppard Ave", "Toronto"]],
    50027:["Tesla", "Model X", 2019, [1, "Yonge", "Toronto"]],
    50028:["Toyota", "Tacoma", 2018, [82, "Taunton Ave", "Oshawa"]],
    50029:["Mercedes-Benz", "A class", 2020, [87, "Marine Drive", "Vancouver"]],
    50030:["Tesla", "Model S", 2020, [75, "Frontenac Drive", "Markham"]],
    50031:["Ford", "F150", 2017, [25, "Salem Road", "Ajax"]],
    50032:["Toyota", "Highlander", 2018, [5, "Kingston Road", "Scarborough"]],
    50033:["Lexus", "RX", 2021, [250, "Boul. Bourassa", "Montreal"]],
    50034:["BMW", "X6", 2019, [87, "King Street", "Toronto"]]
}
v= int(input("Veuillez entrez un identifiant de voitures: "))
try:
    print(f"La voiture que vous recherchez est: {mesVehicules[v]}")
except Exception:
    print("Ce vehicule n'est pas dans la liste")
