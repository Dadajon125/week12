data = """Apples,50,100
Bananas,120,100
Cherries,5,20
Dates,50,50
Eggs,10,24"""

with open("inventory.csv", "w") as f:
    f.write(data)

def check_inventory(csv_file):
    with open(csv_file , "r") as f, open("reorder_list.txt" , "w") as w:
        for item in f:
            item = item.strip()
            name , stock , min_required = item.split(",")
            stock = int(stock)
            min_required = int(min_required)
            if stock < min_required:
                needed = min_required - stock
                w.write(f"Item: {name} | Order Amount: {needed} \n")

check_inventory("inventory.csv")



    

