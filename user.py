from bareryshop import Bakery
import datetime
class User:

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
                   

    def displayProduct(self):
        with open ("data.txt","r") as fp:
            for i in fp:
                sep_text = i.split(" , ")
                print("----------------------------")
                print("no : ",sep_text[0])
                print("name : ",sep_text[1])
                print("price : ",sep_text[2])
                print("quantity : ",sep_text[3])

    
    def place_order(self, name , quantity):
          with open("data.txt","r") as fp:
               for i in fp:
                   sep_text = i.split(" , ")
                   order_str = f"{name} , {quantity}\n"
                   if (name) == sep_text[1]:
                       
                       with open ("ord.txt","w") as o:
                           o.write(order_str)
                           print("order place suceesufully")
                           break
                     
               else:
                print("Product not found")
                
    def pay_bill(self,name):
          with open ("data.txt","r") as data:
              with open("ord.txt","r") as order:
                  with open("paybill.txt","w") as bill:
                      for d in data:
                          sep_data = d.split(" , ")

                          if sep_data[1]==name:
                              bill.write("Product Name : "+ sep_data[1] +"\n")
                              bill.write("price : "+ sep_data[2]+ "\n") 
                              x = float(sep_data[2])

                      for o in order:
                          sep_ord = o.split(" , ")

                          if sep_ord[0] == name:
                              bill.write("Quantity : "+sep_ord[1]+"\n")
                              y = float(sep_ord[1])

                              total = x * y 
                              bill.write("Total Price : "+ str(total))
                              today = datetime.datetime.now()
                              print()
                              print("bill to : ","                ","Order Date : ")
                              print("          Customer ","                    ", today)
                              print()
                              print("\t\tsub total : ",total)
                              tax = total * 10/100
                              print("\t\ttax (10%) : ",tax)
                              sum= total + tax
                              dis = sum*20/100
                              print("\t\tDis (20%) : ",dis)

                              print("\t\tYOU SAVED : ",dis)
                              print()
                              total_bill = (total  + tax) - dis
                              print("\t\tTotal bill : ",total_bill)
    

    def feedBack(self):
         with open ("Feedform.txt","w") as fp:
              print("-------------------------------")
              fp.write(input("Enter your name:  "))
              fp.write(" : \n  -- ")
              fp.write(input("Enter your feedback:  "))
              print("-------------------------------")
