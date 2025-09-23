from array import array
order= [10,50,80,40,1,5,30]
t = sum(order)
print("total:",t)
maxx = max(order)
print("max:", maxx)

mixx = min(order)
print("min:", mixx)

avg= t / len(order)
print("average:", avg)
print(f" task 2 \n restuarant table orders")
print(f"restuarant table orders totals is {t} and averages is {avg}")

print(f" task 3 \n Booleans")
threshold = 50
print(f"Threshold = {threshold}")
print(f"Average = {avg}")
print(f"Maximum = {maxx}")

if threshold > avg and maxx > 700:
    print("Condition met: Threshold > avg and max > 700. Output: TRUE")
else:
    print("Condition not met. No output.")

print(f" task 4: Lists")
prices = [3000, 1500,50000,20000, 5000, 800, 4000]
print(prices)
prices.append(17500)
prices = [ price for price in prices if price < 20000]

print(f" task 5: Lists after condition ")
print(prices)

print(f"Lists after Sort ")
prices.sort()
print(prices)

print(f" task 6: Array from prices")
prices_in_array = array('i', prices)
print("Array of prices:", prices_in_array)
array_sum = sum(prices_in_array)
print("Sum of array:", array_sum)
print("Sum of original list:", sum(prices))


print(f" task 7: Dictionaries ")
client_orders = [
    {'id':1, "name": 'kamana', "value": 7000},
    {'id':2, "name": 'kamari', "value": 1000},
    {'id':3, "name": 'kamara', "value": 3000},
    {'id':4, "name": 'kamata', "value": 9000},
    {'id':5, "name": 'kamasa', "value": 10000},
]

print(f" Dictionaries ")
print(client_orders)

client_orders[0]['name'] = 'karisa'

print(f"after update client on index 0 ")

print(client_orders)

del client_orders[4]
 
print(f"after delete  client on index 4 ")

print(client_orders)

client_orders_sum = [sum(c['value'] for c in client_orders)]

print(f"Total of client order:", client_orders_sum)


