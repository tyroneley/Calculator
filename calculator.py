import tkinter as tk

equationToCalculate = ""

def input(symbol, textResult):
    global equationToCalculate
    equationToCalculate += str(symbol)
    textResult.delete(1.0, "end") 
    textResult.insert(1.0, equationToCalculate)
def calculate(textResult):
    global equationToCalculate
    result = str(eval(equationToCalculate))
    equationToCalculate = ""
    textResult.delete(1.0, "end")
    textResult.insert(1.0, result)  

def clearField(textResult):
    global equationToCalculate
    equationToCalculate = ""
    textResult.delete(1.0, "end")

def calculateBMI(heightInput, weightInput, BMIDisplay):
    height = float(heightInput.get("1.0", "end-1c")) / 100
    weight = float(weightInput.get("1.0", "end-1c"))
    result = str(round(weight / (height**2), 1)) + "kg/m²"
    BMIDisplay.delete(1.0, "end")
    BMIDisplay.insert(1.0, result)

def openCalculatorWindow():
    calculatorWindow = tk.Tk()
    calculatorWindow.geometry("300x275")
    calculatorWindow.title("Simple Calculator")

    textResult = tk.Text(calculatorWindow, height=2, width=16, font=("Arial", 24), background="light gray")
    textResult.grid(columnspan=5)

    buttonOne = tk.Button(calculatorWindow, text="1", command=lambda: input(1, textResult), width=5, font=("Arial", 14))
    buttonOne.grid(row=2, column=1)
    buttonTwo = tk.Button(calculatorWindow, text="2", command=lambda: input(2, textResult), width=5, font=("Arial", 14))
    buttonTwo.grid(row=2, column=2)
    buttonThree = tk.Button(calculatorWindow, text="3", command=lambda: input(3, textResult), width=5, font=("Arial", 14))
    buttonThree.grid(row=2, column=3)
    buttonOne = tk.Button(calculatorWindow, text="4", command=lambda: input(4, textResult), width=5, font=("Arial", 14))
    buttonOne.grid(row=3, column=1)
    buttonTwo = tk.Button(calculatorWindow, text="5", command=lambda: input(5, textResult), width=5, font=("Arial", 14))
    buttonTwo.grid(row=3, column=2)
    buttonThree = tk.Button(calculatorWindow, text="6", command=lambda: input(6, textResult), width=5, font=("Arial", 14))
    buttonThree.grid(row=3, column=3)
    buttonOne = tk.Button(calculatorWindow, text="7", command=lambda: input(7, textResult), width=5, font=("Arial", 14))
    buttonOne.grid(row=4, column=1)
    buttonTwo = tk.Button(calculatorWindow, text="8", command=lambda: input(8, textResult), width=5, font=("Arial", 14))
    buttonTwo.grid(row=4, column=2)
    buttonThree = tk.Button(calculatorWindow, text="9", command=lambda: input(9, textResult), width=5, font=("Arial", 14))
    buttonThree.grid(row=4, column=3)
    buttonThree = tk.Button(calculatorWindow, text="0", command=lambda: input(0, textResult), width=5, font=("Arial", 14))
    buttonThree.grid(row=5, column=2)

    buttonPlus = tk.Button(calculatorWindow, text="+", command=lambda: input("+", textResult), width=5, font=("Arial", 14))
    buttonPlus.grid(row=5, column=4)
    buttonMinus = tk.Button(calculatorWindow, text="-", command=lambda: input("-", textResult), width=5, font=("Arial", 14))
    buttonMinus.grid(row=4, column=4)
    buttonMultiply = tk.Button(calculatorWindow, text="x", command=lambda: input("*", textResult), width=5, font=("Arial", 14))
    buttonMultiply.grid(row=3, column=4)
    buttonDivide = tk.Button(calculatorWindow, text="÷", command=lambda: input("/", textResult), width=5, font=("Arial", 14))
    buttonDivide.grid(row=2, column=4)
    buttonOpenBracket = tk.Button(calculatorWindow, text="(", command=lambda: input("(", textResult), width=5, font=("Arial", 14))
    buttonOpenBracket.grid(row=5, column=1)
    buttonClosedBracket = tk.Button(calculatorWindow, text=")", command=lambda: input(")", textResult), width=5, font=("Arial", 14))
    buttonClosedBracket.grid(row=5, column=3)
    buttonEquals = tk.Button(calculatorWindow, text="=", command=lambda: calculate(textResult), width=5, font=("Arial", 14))
    buttonEquals.grid(row=6, column=4)
    buttonClear = tk.Button(calculatorWindow, text="C", command=lambda: clearField(textResult), width=5, font=("Arial", 14))
    buttonClear.grid(row=6, column=1)
    buttonDecimal = tk.Button(calculatorWindow, text=".", command=lambda: input(".", textResult), width=5, font=("Arial", 14))
    buttonDecimal.grid(row=6, column=3)
    buttonPower = tk.Button(calculatorWindow, text="ⁿ", command=lambda: input("**", textResult), width=5, font=("Arial", 14))
    buttonPower.grid(row=6, column=2)

def openBMICalculatorWindow():
    BMICalculatorWindow = tk.Tk()
    BMICalculatorWindow.geometry("275x200")
    BMICalculatorWindow.title("BMI Calculator")

    BMIDisplay = tk.Text(BMICalculatorWindow, height=2, width=16, font=("Arial", 24), background="light gray")
    BMIDisplay.grid(columnspan=5)
    weightLabel = tk.Label(BMICalculatorWindow, text="Weight (kg):", width=10, font=("Arial", 14), background="light gray")
    weightLabel.grid(row=3, column=1)
    heightLabel = tk.Label(BMICalculatorWindow, text="Height (cm):", width=10, font=("Arial", 14), background="light gray")
    heightLabel.grid(row=4, column=1)

    weightInput = tk.Text(BMICalculatorWindow, height=1, width=6, font=("Arial", 14), background="light gray")
    weightInput.grid(row=3, column=2)
    heightInput = tk.Text(BMICalculatorWindow, height=1, width=6, font=("Arial", 14), background="light gray")
    heightInput.grid(row=4, column=2)
    buttonCalculate = tk.Button(BMICalculatorWindow, text="Calculate BMI", command=lambda: calculateBMI(heightInput, weightInput, BMIDisplay), width=11, font=("Arial", 14), background="light gray")
    buttonCalculate.grid(row=5, column=1, columnspan=2)

menu = tk.Tk()
menu.geometry("300x200")
menu.title("Calculator Menu")
openCalculatorButton = tk.Button(menu, text="Open Number Calculator", command=openCalculatorWindow, width=26, font=("Arial", 14))  
openCalculatorButton.grid(row=2, column=3)
OpenBMIWindow = tk.Button(menu, text="Open BMI Calculator", command=openBMICalculatorWindow, width=26, font=("Arial", 14))  
OpenBMIWindow.grid(row=3, column=3)

menu.mainloop()