from bareryshop import Bakery
class Admin:
    def addProduct(self):
        no = int(input("Enter Product NO. : "))
        name = input("Enter Product Name : ")
        price = int(input("Enter Product Price : "))
        quantity = int(input("Enter Product Quantity : "))
        b = Bakery(no,name,price,quantity)
        fp = open ("data.txt","a")
        fp.write(str(b))
        fp.close()

    def displayProduct(self):
        with open ("data.txt","r") as fp:
            for i in fp:
                sep_text = i.split(" , ")
                print("----------------------------")
                print("Product No : ",sep_text[0])
                print("Product Name : ",sep_text[1])
                print("Price : ",sep_text[2])
                print("Quantity : ",sep_text[3])
                print("----------------------------")

    def updateProduct(self,no):
        container = []
        found =False
        with open ("data.txt","r") as fp:
             for x in fp:
                sep_list = x.split(" , ")
                if (sep_list[0] == str(no)):
                    found = True
                    ans = input("do you want to change name (y/n) : ")
                    if (ans == "y"):
                        sep_list[1] = input("Enter new name : ")
                             
                        ans = input("do you want to change price : (y/n)")
                        if (ans == "y"):
                             sep_list[2] = input("Enter new price : ")

                        ans = input("do you want to change quantity : (y/n)")
                        if (ans == "y"):
                             sep_list[3] = input("Enter new quantity : ")

                        x = ' , '.join(sep_list)

                container.append(x)
        if(found == True):
            with open("data.txt","w") as fp:
                for y in container:
                    fp.write(y)

        else:
            print("id not present....")
    
    def deleteProduct(self,no):
        container = []
        found = False
        with open ("data.txt","r") as fp:
            for i in fp:
                sep_split = i.split(" , ")
                if (sep_split [0]== str(no)):
                    found = True
                else:
                    container.append(i)                           
         
        if (found == True):
            with open ("data.txt","w") as fp:
                for x in container:
                    fp.write(x)
        
        else:
            print("not found....")
        
            
    def searchProduct(self,name):
          with open("data.txt","r") as fp:
               for i in fp:
                   sep_text = i.split(" , ")

                   if (name) == sep_text[1]:
                    print()
                    print("---------- Details ------------------")
                    print()
                    print("Product No : ",sep_text[0])
                    print("Product Name : ",sep_text[1])
                    print("price : ",sep_text[2])
                    print("Quantity : ",sep_text[3])
                    break

                   else :
                        print("product not found.......") 

    # def updateProduct1(self, no):
    #     container = []
    #     found = False

    #     with open("data.txt", "r") as fp:
    #         for x in fp:
    #             sep_list = x.split(" , ")
    #             if sep_list[0] == str(no):
    #                 found = True
    #                 ans = input("Do you want to change name (y/n): ")
    #                 if ans == "y" or ans == "Y":
    #                     sep_list[1] = input("Enter new name: ")

    #                 ans = input("Do you want to change price (y/n): ")
    #                 if ans == "y" or ans == "Y":
    #                     # update price
    #                     sep_list[2] = input("Enter new price: ")
    #                 ans = input("Do you want to change quantity (y/n): ")
                    
    #                 if ans == "y" or ans == "Y":
    #                     sep_list[3] = input("Enter new quantity: ")
    #                 # join updated data with comma
    #                 x = ' , '.join(sep_list)
    #             container.append(x)
    #     if found == True:
    #         # write updated data to file
    #         with open("data.txt", "w") as fp:
    #             for x in container:
    #                 fp.write(x.strip() + '\n')
    #     else:
    #         print("Product not found")
                        

   