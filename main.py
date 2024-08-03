from admin import Admin
from user import User

admin =Admin()
user = User()
choice =0

ch=0

while (choice != 3):
    print()
    print("------------------------------------  Welcome to Moon pie bakery  --------------------------------------------------------")
    print()

    print("\t\t 1 . Admin section")
    print("\t\t 2 . User Section ")
    print("\t\t 3 . Exit")

    choice = int(input("\nEnter your choice : "))
    
    if (choice == 1):
        while ch!=6:
            print()
            print("---------------------------  Welcome ! you are logged in Admin ! -----------------------------------------------------")
            print()
            print("\t\t 1 . Add products ")
            print("\t\t 2 . Display products ")
            print("\t\t 3 . Update products ")
            print("\t\t 4 . Delete products ")
            print("\t\t 5 . Search products ")
            print("\t\t 6 . Exit.. ")           
            ch = int(input("\nEnter your choice : "))

            if ch == 1:
                admin.addProduct()

            elif ch == 2:
                admin.displayProduct()

            elif ch==3:
                 no = int(input("Enter no which you want to update : "))
                 admin.updateProduct(no)

            elif ch==4:
                no = int(input("Enter no which you want to delete :  "))
                admin.deleteProduct(no)

            elif ch==5:
                name = input("Enter Product Name which you want to search : ")
                admin.searchProduct(name)


                           

    if (choice == 2):
        while ch!=5 :
            print()
            print("---------------------------  Welcome ! you are logged in User ! -----------------------------------------------------")
            print()
            print("\t\t 1 . Search products ")
            print("\t\t 2 . Display  products ")
            print("\t\t 3 . Place Order of products ")
            print("\t\t 4 . Enter your Feedback ")
            print("\t\t 5 . Exit.. ")
            ch = int(input("\nEnter your choice : "))

            
            if ch == 1:
                name = input("enter name of product : ")
                user.searchProduct(name)

            elif ch == 2:
                user.displayProduct()

            elif ch==3:
                name = input("Enter the product name : ")
                quantity = int(input("Enter the quantity : "))
                user.place_order(name,quantity)
    
            elif ch==4:
                user.feedBack()








