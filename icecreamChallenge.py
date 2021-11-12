import guizero

app = guizero.App(title = 'noahSquaredIceCream')

textboxTitle = guizero.Text(app, text = 'Your Name')
textbox = guizero.TextBox(app)
flavorChoice = guizero.ButtonGroup(app, options=['chocolate', 'vanilla', 'strawberry'])
sliderTitle = guizero.Text(app, text = 'Number of Scoops')
slider = guizero.Slider(app)
dairyFree = guizero.CheckBox(app, text = 'Dairy Free')
if dairyFree == true:
    text = guizero.Text(app, text = 'YOUR WEIRD')
toppingsTitle = guizero.Text(app, text = 'Extra Toppings?')
textbox = guizero.TextBox(app)


app.display()