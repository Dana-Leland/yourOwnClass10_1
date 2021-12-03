Dana Leland, 10.1 Your Own Class, README.txt
A description of the class. (This only needs to be a short paragraph.)


The class will let the user edit an already existing menu, by adding or removing from it, let the user make an order entering their name and milk preference, then will call out the order with their “name” and any drink specifications. The part of this project which suggested I be creative inspired the “naming” function. In it, there’s a ⅓ chance that your name will get messed up by the program. It will exchange some random vowels so the name which comes out is recognizable, but far from accurate. The program is modeling a coffee shop -- specifically its menu and ordering process


A description of each of the class and data variables. (Each variable description only needs to be a sentence of two.)


        There are two class variables: coffeeOptions and milk. coffeeOptions is a dictionary which stores each type of coffee and its calorific intake, milk is a list which has how many parts milk each drink has (i.e how many parts coffee to how many parts milk). 
I have three data variables, two of which are booleans (self.lactose and self.invalid) and the third a list (self.coffees). Function getCoffee turns self.lactose to true if the user requests no coffee, which changes the print statement in makeCoffee to contain “no milk” rather than how many parts milk. self.coffees is a list created by showMenu and later referenced by makeCoffee. Its use in showMenu is to create a column consisting of only the coffee, while the other is calories, and in makeCoffee it’s simply used to find the list index of whatever coffee the customer ordered. 


A description of each of the methods. These descriptions should include what arguments or inputs are necessary and what the method returns if anything. (Each method description only needs to be 2-3 sentences, including describing arguments and returns.)


* __init__ just defines self.lactose and self.coffees for the following methods. The usage of these variables is described in the previous section.
* addCoffee will add a new coffee item (if given the name of the coffee and the calorie count). It will also take how many parts milk and add it to the milk list, but if the parts milk isn’t specified, addCoffee will assume 0. Further, it checks to see if the coffee already exists on the menu, and if it does, will return 'That coffee is already listed' (the only time this method returns something). 
* removeCoffee only takes the name of the coffee, then removes that coffee from the menu, and any order after its removal won’t be valid (it will print “order something actually on the menu”). If given an item that isn’t already on the menu, it will return “[item] not found” and skip the command.
* showMenu prints the menu nice and pretty, with one column holding types of coffee and the other with calories per coffee. It will line up nicely and includes a top and bottom border
* callName is my favorite function of the bunch; it has a ⅓ chance of messing up the name of the customer. For example, in my main function, ‘Annabelle’ can become ‘Annybollo.’ Literally the entire purpose of this function is to (maybe) mess up the names, and I love it.
* getCoffee finds the name of the coffee, calories of the coffee, and how much milk is in the coffee. It essentially makes the order nice and readable for makeCoffee.
* makeCoffee is the final print statement, and will print out “I’ve got an order for [name], [order], with [x] calories and” either “[x] parts milk” or “no milk.” It’s meant to mimic a barista calling out an order. 


What the Demo Program does
        The demo program uses all of the functions within the program. It will first show the original menu, then add a new coffee (‘Ristretto’), remove a coffee (‘Black’), and then show an example of what happens when asked to remove a non-existent coffee (‘Smoothie’). It will then print out the orders of 5 customers. Each of these can be altered as you will, and I highly suggest trying out different names and orders. I had a lot of fun seeing how the names got messed up, and hopefully you’ll have the same enjoyment.


How to run the Demo Program
        Just run the program as is and it’ll work just fine. If you want to test it out more, go into the main function and input different orders, names, and milk preferences. You can also add/remove anything to the menu as you will.