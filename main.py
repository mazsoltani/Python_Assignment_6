from pyfiglet import Figlet
f= Figlet(font="standard")
print(f.renderText( "Soltani Store."))
my_list=[]
myfile = open("database.txt","r")
data = myfile.read().lower().split("\n")
for i in range(len(data)):
    product_info = data[i].split(',')
    my_dic = {}
    my_dic['id']= product_info[0]
    my_dic['name']= product_info[1]
    my_dic['price']= product_info[2]
    my_dic['count']= product_info[3]
    my_list.append(my_dic)

def show_menu():
    print("Menu Store")
    print("1- Show Commodity.")
    print("2- Add Commodity.")
    print("3- Edit Commodity.")
    print("4- Delete Commodity.")
    print("5- Buy Commodity.")
    print("6- Search Commodity.")
    print("7- Exit")
  
def Add_commodity():
    while True:
        dic_add={}
        add_item = input("Do You Want to Additinon Commodity Please Type y/n= ")
        if add_item == "y":
            dic_add["id"]= input("Please Enter Id = ")
            dic_add["name"]= input("please Enter Name = ")
            dic_add["price"]= input("Please Enter Price =  ")
            dic_add["count"]= input("Please Enter Count of Commodity= ")
            print("ADD Is Successful.")
            my_list.append(dic_add)
        elif add_item == "n":
            break

def Delete_commodity():
    while True:
        delete_item = input("Do You Want to Delete Commodity? Please Type y/n=")
        if delete_item=="y":
            choice_Delete = input("Please Enter Your Commpdity Id For Delete= ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==choice_Delete:
                    my_list.pop(i)
                    print("Delete Items Is Successful.")
                    break 
        elif delete_item=="n":
             break

def Edit_commodity():
    while True:
        edit_item = input("Do You Want to Edit Commodity? Please Type y/n= ")
        if edit_item=="y":
            print("1- Edit id")
            print("2- Edit name ")
            print("3- Edit price ")
            print("4- Edit count ")

            edit_c = input("Please Enter Your Number= ")
            print(my_list)
            choice_Edit = int(input("Please Choose Number For Example 1,2,3 or 4 = "))
            if   edit_c=="1":
                my_list[choice_Edit]["id"]= input("Please Enter Your Id for Edit= ")
            elif   edit_c=="2":
                my_list[choice_Edit]["name"]= input("Please Enter Your Name for Edit= ")
            elif   edit_c=="3":
                my_list[choice_Edit]["price"]= input("Please Enter Your Price for Edit= ")
            elif   edit_c=="4":
                my_list[choice_Edit]["count"]= input("Please Enter Your Count for Edit= ")
            
            print("Edit Is Successful.")

        elif edit_item=="n":
            break
 
def Search_commodity():
    while True:
        search_item = input("Do You Want to Search Commodity? Please Type y/n= ")
        if search_item=="y":
            nameofsearch = input("Please Enter Name of Commodity= ")
            for i in range(len(my_list)):
                if my_list[i]["name"]==nameofsearch:
                    print("Your Search is Ok")
                    print({"id":my_list[i]["id"]
                    ,"name":my_list[i]["name"]
                    ,"price":my_list[i]["price"]
                    ,"count":my_list[i]["count"]})
                    
                    break
            else:
                print("Error ... Your Search is Incorrect.")
        elif search_item=="n":
            break

def buy_commodity():
    Total_price=0
    count=0
    factor=[]
    while True:
        
        buy_item = input("Do You Want to Buy Commodites? Please Type y/n= ")
        if buy_item=="y":
            print(my_list)

            id_of_buy = input("Please Enter Your Id= ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==id_of_buy:
                    print("Your Items is Ok.")
                    count_buy = int(input("Please Enter Count Of Commodites= "))
                    print("Your Factor is=")
                    fact={"price":my_list[i]["price"]
                    ,"sum_price":str(Total_price)
                    ,"sum_count":str(count)}
                    factor.append(fact)
                    print(factor)

                    break
                else: 
                    print("....Error ")
        else:
            break

def exit_commodity():
    while True:
        save_item = input("Do You Want to Save Please Enter s ")
        if save_item=="s":
           
            file = open("database.txt","w")
            for i in range(len(my_list)):
                save_file = my_list[i]["id"]+","+ my_list[i]["name"]+","+ my_list[i]["price"] +","+ my_list[i]["count"]
                file.write(str(save_file))
                if i < len(my_list)-1:
                    file.write("\n")
            file.close()           
            exit()
            break

while True:

    show_menu()

    choice = input("....Please Choose a Number Of Menu= ")

    if choice =="1":
        print(my_list)
        print(len(my_list))

    elif choice =="2":
        Add_commodity()

    elif choice =="3":
        Edit_commodity()

    elif choice =="4":
        Delete_commodity()

    elif choice == "5":
        buy_commodity()

    elif choice =="6":
        Search_commodity()

    elif choice =="7":
        exit_commodity()