import pandas
##### INTIALIZATION #####
#STRING SERIES
fruits = pandas.Series(["apples", "oranges", "bananas"])
print("Fruit series:")
print(fruits)
#FLOAT SERIES
temperature = pandas.Series([32.6, 34.1, 28.0, 35.9])
print("\nTemperature series:")
print(temperature)
#INTEGER SERIES
factors_of_12 = pandas.Series([1,2,4,6,12])
print("\nFactors of 12 series:")
print(factors_of_12)
print("Type of this data structure is:", type(factors_of_12))

#FLOAT & INTEGER FRAME
temp_fact = {'col1':factors_of_12, 'col2':temperature} 
result = pandas.DataFrame(data = temp_fact)
print("\nTemperature & Factors of 12 series combined in a frame: ")
print(result)
print("Type of this data structure is:", type(result))