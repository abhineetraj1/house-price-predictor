import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the house price data
data = pd.read_csv("house_price.csv")

# Train a machine learning model on the data
X = data[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors']]
y = data['price']
model = LinearRegression()
model.fit(X, y)

# Define the prediction function
def predict_price(bedrooms, bathrooms, sqft_living, sqft_lot, floors):
    inputs = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors]])
    price = model.predict(inputs)[0]
    return round(price, 2)

# Create the GUI
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("500x350+10+10")

tk.Label(background="green", height="200", width="200").place(x=0,y=0)

# Create input fields for the features
bedrooms_label = tk.Label(root, text="Bedrooms",font=("Bahnschrift","20"), background="green")
bedrooms_label.grid(row=0, column=0)
bedrooms_entry = tk.Entry(root, font=("Bahnschrift","20"))
bedrooms_entry.grid(row=0, column=1)

bathrooms_label = tk.Label(root, text="Bathrooms",font=("Bahnschrift","20"), background="green")
bathrooms_label.grid(row=1, column=0)
bathrooms_entry = tk.Entry(root, font=("Bahnschrift","20"))
bathrooms_entry.grid(row=1, column=1)

sqft_living_label = tk.Label(root, text="Sqft Living",font=("Bahnschrift","20"), background="green")
sqft_living_label.grid(row=2, column=0)
sqft_living_entry = tk.Entry(root, font=("Bahnschrift","20"))
sqft_living_entry.grid(row=2, column=1)

sqft_lot_label = tk.Label(root, text="Sqft Lot",font=("Bahnschrift","20"), background="green")
sqft_lot_label.grid(row=3, column=0)
sqft_lot_entry = tk.Entry(root, font=("Bahnschrift","20"))
sqft_lot_entry.grid(row=3, column=1)

floors_label = tk.Label(root, text="Floors",font=("Bahnschrift","20"), background="green")
floors_label.grid(row=4, column=0)
floors_entry = tk.Entry(root, font=("Bahnschrift","20"))
floors_entry.grid(row=4, column=1)

# Define the button's callback function
def predict_price_callback():
    # Get the user's input values
    bedrooms = float(bedrooms_entry.get())
    bathrooms = float(bathrooms_entry.get())
    sqft_living = float(sqft_living_entry.get())
    sqft_lot = float(sqft_lot_entry.get())
    floors = float(floors_entry.get())
    # Call the prediction function with the input values
    predicted_price = predict_price(bedrooms, bathrooms, sqft_living, sqft_lot, floors)
    # Update the output label
    output_label.config(text=f"Predicted Price: ${predicted_price}")

# Create a button to predict the house price
predict_button = tk.Button(root, text="Predict Price",font=("Bahnschrift","18") ,command=predict_price_callback)
predict_button.grid(row=5, column=0, columnspan=2)

# Create an output label to display the predicted house price
output_label = tk.Label(root, text="")
output_label.grid(row=6, column=0, columnspan=2)

# Run the GUI
root.mainloop()
