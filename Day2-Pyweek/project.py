#contact manger 
#Lets Build!!
contact=[]

def Home():
    name=input("Enter Name:")
    number=input("Enter Number:")
    contact.append(name)
    contact.append(number)
    def save_contact():
        with open("contacts.txt","a")as file:
            name,number=contact
            file.write("| ")
            file.write(name+" ")
            file.write(number)
            file.write("\n")
    save_contact()
 
def read_contacts():
     with open("contacts.txt","r")as file:
         contacts=file.read()
         print(contacts)
            
print("Contact System")
print("\n 01.Add \n 02.Read \n 03.Del \n 04.Exit")
opt=input("Select the options : ")

if opt == '1':
    Home()
elif opt == '2':
    read_contacts()
else:
    print("Select the right option Bro!!")
