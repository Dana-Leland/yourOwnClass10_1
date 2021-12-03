#Dana Leland, Assignment 10.1: Your Own Class
"""
8 functions, one class. __init_ sets our two data variables, self.lactose and self.coffees (boolean and list)
removeCoffee will delete a coffee off the menu
callName will return the name of the order, or, will slightly mess it up (purposefully)
getCoffee returns the order, calories, and amount of milk
addCoffee will add a coffee to the menu
makeCoffee will return the order in full (as if a barista is calling out the order)
and main which demonstrates all these functions and prints the outputs to the user
"""
import random
class coffeeMaker:
    coffeeOptions = {'Black': 5, 'Latte': 103, 'Cappuccino': 130, 'Americano': 15,
        'Espresso':3, 'Macchiato': 13, 'Mocha':197, 'Irish':87}
    milk = [0, 2, 1, 2, 0, 1, 2, 4]
    #two class variables, used throughout the class (showMenu, getCoffee, addCoffee, removeCoffee)

    def __init__(self):
        self.lactose = False
        self.coffees = []
        #two data variables. self.coffees is essentially the same as coffeeOptions, 
        # but is a list instead of a dict, and doesn't contain calorie count
    def showMenu(self):
        #1 "other method"
        self.coffees = list(coffeeMaker.coffeeOptions)
        #extract all the coffees from coffeeOptions, add them to self.coffees
        newMenu = '\t-=+=-\n\nCoffee \t\t Calories\n'
        #format the top of the menu nicely
        calories = []
        #make an empty list to add calories to later
        for x in (coffeeMaker.coffeeOptions):
            calories.append(coffeeMaker.coffeeOptions[x])
            #add all of the calories on the list to the menu
        x=0
        while x<len(self.coffees):
            #add each coffee to the menu, as well as its calorie count
            #add the correct amount of tabs so it lines up
            if len(self.coffees[x])>5:
                newMenu+='{} \t {}\n'.format(self.coffees[x], calories[x])
                #if it's long, add two tabs
            else:
                newMenu+='{} \t\t {}\n'.format(self.coffees[x], calories[x])
                #if it's short, add one tab
            if x==len(self.coffees)-1:
                newMenu+='\n\t-=+=-'
                #if it's the end of the menu, add the bottom border
            x+=1
        return newMenu
    def removeCoffee(self, delCoffee):
        try:
            z=0
            for x in self.coffees:
                #find where the coffee is (its placement in the list)
                if x == delCoffee:
                    break
                z+=1
            del coffeeMaker.coffeeOptions[delCoffee]
            #delete the coffee
            del coffeeMaker.milk[z]
            #delete the parts milk
            return ('{} removed!').format(delCoffee)
        except KeyError:
            #if it's not found, return an error code
            return 'There is no {} on the menu, so it cannot be removed'.format(delCoffee)
    def callName(self, name):
        #2 "other method"
        num = random.randint(0,2)
        #1 in 3 chance callName will mess up the name, replacing vowels
        repA = False
        repE = False
        repI = False
        repO = False
        repU = False
        repY = False
        #booleans just so the letters don't get replaced twice 
        # i.e if we replace the 'a' in 'Danny' don't then replace 
        # the 'y' with 'a' to make it Dynna. That makes it *too* 
        # unrecognizeable
        if num ==1:
            #if, by random chance, you get 1, some vowels in your name will be replaced
            if 'a' in name and repA == False:
                name = name.replace('a', 'y')
                repY = True
            if 'e' in name and repE == False:
                repO=True
                name = name.replace('e', 'o')
            if 'i' in name and repI == False:
                repU=True
                name = name.replace('i', 'u')
            if 'o' in name and repO == False:
                repE=True
                name = name.replace('o', 'e')
            if 'u' in name and repU == False:
                repI=True
                name = name.replace('u', 'i')
            if 'y' in name and repY == False:
                repA = True
                name = name.replace('y', 'a')
        return name
    def getCoffee(self, order, lactose=None):
        #get method
        try:
            cal = coffeeMaker.coffeeOptions[order]
            #calorie count
            partsMilk =coffeeMaker.milk[list(coffeeMaker.coffeeOptions.keys()).index(order)]
            #find where in the list the coffee was found
            partsMilk = coffeeMaker.milk[partsMilk]
            #take where it was found and plug it in to the milk list to find partsmilk
        except KeyError:
            return
            #if the coffee doesn't exist, just skip and the program will catch it in 
            # makeCoffee
        if lactose != None and lactose != False:
            self.lactose = True
            #set self.lactose to True if anything other than none or false is put in
        else:
            self.lactose = False
            #set lactose to False otherwise (i.e just assume they want milk because 
            # they didn't specify or said no)
        if self.lactose:
            #if lactose, there is no milk
            partsMilk =0
        return order, cal, partsMilk
    def addCoffee(self, newCoffee, calCount, partsMilk=None):
        if newCoffee in coffeeMaker.coffeeOptions:
            return 'That coffee is already listed'
            #if the coffee is already in coffeeOptions, skip it
        coffeeMaker.coffeeOptions[newCoffee] = calCount
        if partsMilk != None:
            coffeeMaker.milk.append(partsMilk)
            #if they did specify how many parts milk, add it to the list
        else:
            coffeeMaker.milk.append(0)
            #if they didn't specify how many parts milk, just add 0
        return ('{} added to menu').format(newCoffee)
        #let them know the coffee was succesfully added to the menu 
        # (this permanently adds it to the menu, but the return statement doesn't 
        # affect other functions)
    def makeCoffee(self, order, name, lactose=None):            
        f = coffeeMaker
        #I just got tired of typing out "coffeeMaker", so I changed it to f
        newName = f.callName(self, name)
        #get the messed up name
        newOrder = f.getCoffee(self, order, lactose)
        #get the order, calcount, and amount of milk
        fullOrder = ''
        fullOrder+= 'Ive got an order for {}, '.format(newName)
        #get the string with the order ready
        z=0
        if newOrder!=None:
            #if the order actually came through 
                # i.e. it didn't cause an key error i.e. it's actually on the menu,
                # then actually prepare the order
            for x in newOrder:
                if z == 0:
                    fullOrder+=str(x)+', '
                    #add the coffee order, then a comma after
                elif z == 1:
                    fullOrder+= 'with {} calories'.format(str(x))
                    #add the calcount
                if self.lactose and z==2:                        
                    fullOrder+= ', with no milk'
                    #if lactose, then say "no milk" and the end
                elif z==2:
                    z=0
                    for x in self.coffees:
                        if x == order:
                            #find where the milk is within the list
                            break
                        z+=1
                    if coffeeMaker.milk[z]>1:
                        #if greater than 1 part, make "parts milk" plural
                        fullOrder+= ', {} parts milk'.format(coffeeMaker.milk[z])
                    elif coffeeMaker.milk[z]==1:
                        #if one make it singular
                        fullOrder+= ', {} part milk'.format(coffeeMaker.milk[z])
                    else:
                        #if 0, say no milk
                        fullOrder+= ', no milk'
                z+=1
            fullOrder+='.' 
            #add a period to the end of the sentence 
        else:
            #if the order *did* cause a key error, then getCoffee would return None,
            #and that's how we get here
            return 'Please order something actually on the menu, {}.'.format (newName)
        return fullOrder

def main():
    machine = coffeeMaker()
    print(machine.showMenu())
    machine.addCoffee('Ristretto', 5, 0)
    #adds Ristretto to the menu so customers can order later
    machine.removeCoffee('Black')
    #removes black coffee from the menu (customers can no logner order it)
    print(machine.removeCoffee('Smoothie'))
    #example of what happens when you remove something that isn't on the menu
    
    print(machine.makeCoffee('Cappuccino','Terrance'))
    print(machine.makeCoffee('Cappuccino','Elizabeth', True))
    print(machine.makeCoffee('Slurpee','Karen', True))
    print(machine.makeCoffee('Cappuccino','Augustus', False))
    print(machine.makeCoffee('Ristretto','Annabelle', True))
    #different orders to show flexibility of program
    #specifically the 3 cappuccinos with milk, no milk, then milk again
    #just to prove that once someone orders no milk, that doesn't mean it's always
    #no milk for the following customers
    
    
if __name__ == "__main__":
    main()