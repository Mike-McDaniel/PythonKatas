
stevesAddress = {
	"street": "49 Germantown",
	"city": "Germantown",
	"state": "PA",
	"zip": "138322",
}
samsAddress = {
	"street": "44 Germantown",
	"city": "Jose",
	"state": "CA",
	"zip": "914321"
}
mikesAddress = { }


# print(stevesAddress["street"])
# print(stevesAddress["zip"])
# print(samsAddress["state"])


# print(samsAddress["city"]) # "Jose"
samsAddress["city"] = "San Jose"
# print(samsAddress["city"]) # "San Jose"

mikesAddress["city"] = "XXXXXXXXXX"
mikesAddress["state"] = "YYYYYY"
mikesAddress["zip"] = "111111"

# print(mikesAddress)


numbers = {}
for number in [1,1,2,1,3,4,3,3,3,3]:
    if (number in numbers):
        numbers[number] = numbers[number] + 1
    else:
        numbers[number] = 1
print(numbers)


def getZipCodes(addresses):
    zips = []
    for address in addresses:
        zips.append(address["zip"])
    return zips

def getZipCodes(addresses):
    return list(map(lambda address: address["zip"], addresses))