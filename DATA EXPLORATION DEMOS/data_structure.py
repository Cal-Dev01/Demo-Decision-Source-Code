# Array

single_dimensional_array1 = [2, 4, 6, 8, 10]
single_dimensional_array2 = [3.6, 4.8, 16.3, 12.7, 10.34]
single_dimensional_array3 = ["Manchester", "Birmingham", "London", "Leeds", "Milton Keynes"]

print(single_dimensional_array1[0])
print(single_dimensional_array2[2])
print(single_dimensional_array3[1])

multi_dimensional_array1 = [
    [2, 4, 6, 8, 10], [5, 12.9, 14, 8, 21], [1, 2, 3], [7.3, 3.1, 17.4]
]
print(multi_dimensional_array1[1][3])

# Dictionary

string_data = {"John", "Mathew", "Ben", "Lucy"}
string_data_2 = {3, 4, 6, 8, 10}

customer_data = {
    "first_name": "John",
    "last_name": "Doe",
    "address": "12 Melbourn Road , 1B5 4RA",
    "dob": "20-May-2006"
}

customer_data_multi_dimensional = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "address": {"home1": "12 Melbourn Road , 1B5 4RA", "home2": "14 Melbourn Road , 1B5 4RA"},
        "dob": "20-May-2006",
        "phone_number": {"number1": "02288888", "number2": "0255549"},
        "color": {"colour": "blue", "colour2": "green"}
    },
    {
        "first_name": "Jane",
        "last_name": "Mason",
        "address": "20 Filing Avenue RA3 YBZ",
        "dob": "6- June-2008"
    }
]

multi_dimensional_dictionary = [
    {1, 5, 89}, {12, 6, 9}, {20, 45.8}, {23, 50, 3.6}
]

multi_dimensional_dictionary2 = [
    {"Lion", "Tiger", "Cat"}, {"Dove", "Hen", "Turkey"}
]

print(string_data)

# Tuple

single_dimensional_tuple1 = (2, 4, 6, 8, 10)
single_dimensional_tuple2 = (3.6, 4.8, 16.3, 12.7, 10.34)
single_dimensional_tuple3 = ("Manchester", "Birmingham", "London", "Leeds", "Milton Keynes")

print(single_dimensional_tuple1[0])
print(single_dimensional_tuple2[2])
print(single_dimensional_tuple3[1])

multi_dimensional_tuple1 = (
    (2, 4, 6, 8, 10), (5, 12.9, 14, 8, 21), (1, 2, 3), (7.3, 3.1, 17.4)
)
print(multi_dimensional_tuple1[1][3])

# Adding a tuple example for dictionary

tuple_data = ("John", "Mathew", "Ben", "Lucy")
tuple_data_2 = (3, 4, 6, 8, 10)

print(tuple_data)
print(tuple_data_2)
