values = [1,2,3,4]

new_value = []

for value in values:
    if value % 2 == 0:
        new_value.append(value**2)
    else:
        new_value.append(value)

print(new_value)

new_value = [value ** 2 if value % 2 == 0 else value for value in values]
print(new_value)

# List Comprehension

new_values = [value ** 2 for value in values]
print(type(new_values))

#Set comprehension

new_values = {value ** 2 for value in values}
print(type(new_values))

# Dict comprehension

new_values = {value : value **2 for value in values}
print(type(new_values))

#Tupple Comprehension

new_values = (value ** 2 for value in values)
print(type(new_values))


def first_n_lowercase_letters(n):
    alphabet_fiesta = {
        'a': "apple",
        'b': "banana",
        'c': "cherry",
        'd': "donut",
        'e': "elephant",
        'f': "flamingo",
        'g': "grape",
        'h': "hedgehog",
        'i': "ice cream",
        'j': "jellyfish"
    }

    return [alphabet_fiesta[word] for word in sorted(alphabet_fiesta.keys())[:n]]

n = int(input('Type a number: '))
result = first_n_lowercase_letters(n)
print(result)