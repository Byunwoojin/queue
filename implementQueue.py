
queue=[]

while True:
    print("********Queue Program*********")
    print("1.Insert item to Queue")
    print("2.Delete item from Queue")
    print("3.Print Queue")
    print("4.Exit")
    menu=int(input("\nEnter menu : "))
    if menu==1:
        item=input("#Enter item to insert :")
        queue.append(item)
        print("# '",item,"' is inserted.")
        print("# State of Queue: ",queue)
        print()
    elif menu==2:
        if len(queue)==0:
            print("# Nothing to delete in queue.")
            print()
        else:
            print("# First item '",queue[0],"' was removed.")
            del queue[0]
            print("# State of Queue : ", queue)
            print()
    elif menu==3:
        if len(queue)==0:
            print("# Nothing in queue.")
            print()
        else:
            print("# State of Queue : ",queue)
            print()
    elif menu==4:
        break
    
        
    
