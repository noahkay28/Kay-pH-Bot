import guizero

app = guizero.App(title = 'noahSquaredIceCream')

textboxTitle = guizero.Text(app, text = 'Your Name')
textbox = guizero.TextBox(app)
flavorChoice = guizero.ButtonGroup(app, options=['chocolate', 'vanilla', 'strawberry'])
sliderTitle = guizero.Text(app, text = 'Number of Scoops')
slider = guizero.Slider(app)
dairyFree = guizero.CheckBox(app, text = 'Dairy Free')
toppingsTitle = guizero.Text(app, text = 'Extra Toppings')
toppingsList = guizero.ListBox(app, items=['nuts', 'chocolate sauce', 'wafer'])
costDetails = guizero.Text(app, text = 'Cost is $2 plus $.50 per topping') 
finalCost = guizero.TextBox(app)
def buttonClicked():
    info('Your Order Has Been Placed - Thank You')
finishedButton = guizero.PushButton(app, command = buttonClicked, text = 'Place Order')

app.display()
