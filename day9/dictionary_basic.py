person = {"firstName": "Rizki",
          "middleName": "Abdillah",
          "lastName": "Azmi"}

person["fullName"] = "Rizki Abdillah Azmi"
print(person["firstName"])

for dict in person:
    print(dict)
    print(person[dict])
