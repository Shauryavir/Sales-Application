from tkinter import *
import random

root=Tk()

root.title("Sales Apllication Tupples")
root.geometry("400x400")



month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "November", "December")

label_month = Label(root)
label_month["text"] = "Months : " + str(month)

label_profit = Label(root)
label_profits["text"] = "Profits : " + str(profits)



profits = (28000, 45000, 98000, 73000, 65500, 16000, 80000, 76000, 35000, 50000, 78000, 89055)


max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)


max_profit_month = month[max_profit_index]  
print("The Maximum Profit Of " + str(max_profit)+ " Was Recorded In The Month of " + str(max_profit_month))
     
      
min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]  
print("The Minimum Profit Of " + str(min_profit)+ " Was Recorded In The Month of " + str(min_profit_month))