stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def printInventory(inventory):
    print("Inventory:")
    itemTotal=0
    for k, v in inventory.items():
        itemTotal=itemTotal+v
        print(str(v)+' '+str(k))
    print("Total number of items: "+str(itemTotal))
printInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0) #this adds a defaulted to zero item in the inv if the key isn't already there
        inventory[item]+=1
    return inventory
newInv={'gold coin':42, 'rope':1}
printInventory(newInv)
bossLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
newInv=addToInventory(newInv, bossLoot)
printInventory(newInv)
