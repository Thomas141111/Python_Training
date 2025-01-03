inventory = {"electronic": {}, "furniture": {}}
while True:
    choice = int(input(
        "Enter your choice:\n1.Add Product\n2.Display Products\n3.Show Inventory Category wise\n4.Remove product\n"))
    if choice == 1:
        category=input("Enter Category Name(Electronic/Furniture): ").lower()
        if category in inventory:
            item_name=input("Enter Item Name: ").lower()
            item_count=input("Enter count: ").lower()
            inventory[category][item_name]=item_count
            print("Item Added")
        else:
            print("Category Not Found: ")
        continue

    elif choice == 2:
        for key, products in inventory.items():
            print(key,":",products)

    elif choice == 3:
        category = input("Enter Category Name: ").lower()
        if category in inventory:
            print(inventory[category])
        else:
            print("Category Not Found: ")
        continue

    elif choice == 4:
        category = input("Enter Category Name: ").lower()
        purchase_item = input("Enter Purchase item: ").lower()
        if category in inventory:
            if purchase_item in inventory[category]:
                inventory[category][purchase_item] = int(inventory[category][purchase_item]) - 1
                print("Purchase Completed")
        else:
            print("Category not found")
        continue

    else:
        print("Exited")
        break