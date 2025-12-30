with open("transecsionrecord.txt" ,"r") as file:
    total_deposited=0
    total_withdrawl=0
    for line in file:
        parts=line.strip().split(",")
        status=parts[1].lower()
        ammount=int(parts[2])
        if status=="deposite":
            total_deposited += int(parts[2])
        elif status=="withdraw":
            total_withdrawl += int(parts[2])
            if (ammount > 50000):
                print("susspecious account ")
            else:
                print("Not a sespecious transection.. ")
    print(f"Total deposited ammount is : {total_deposited}")
    print(f"Total withdrawn ammount is : {total_withdrawl}")
