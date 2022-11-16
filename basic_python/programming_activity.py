first = input ("first name? ")
last = input ("last name? ")
email = input ("email address? ")
phone = input ("phone number? ")
job = input ("job title? ")
ID = input ("ID number? ")

#extension questions
hair = input ("hair color? ")
eye = input ("eye color? ")
month = input ("starting month? ")
training = input ("completed additional training? ")


#printed results
print("ID card is:")
print ("-------------------------------------------")
print(last.upper() + ", " + first)
print (job.capitalize())
print("ID: " + ID)
print()
print(email.lower())
print(phone)
print()

#extension results
print (f"hair: {hair:15} eyes: {eye}")
print (f"month: {month:15} trianing: {training}")
print ("-------------------------------------------")