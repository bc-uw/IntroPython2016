"""
1. Print the dict by passing it to a string format method, so that you get
something like:

“Chris is from Seattle, and he likes chocolate cake, mango fruit,
greek salad, and lasagna pasta”
"""

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print('{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.'.format(**food_prefs))

"""
2. Using a list comprehension, build a dictionary of numbers from zero to
fifteen and the hexadecimal equivalent (string is fine). (the hex() function
gives you the hexidecimal representation of a number.)
"""
#list comp
s = [(hex(i),i) for i in range(16)]

"""
3. Do the previous entirely with a dict comprehension – should be a one-liner
"""
#dict comp
d = { hex(i): i for i in range(16)}

"""
4. Using the dictionary from item 1: Make a dictionary using the same keys but
with the number of ‘a’s in each value. You can do this either by editing the
dict in place, or making a new one. If you edit in place, make a copy first!
"""

s = {k: v.count("a") for k, v in food_prefs.items()}
"""
5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible 2, 3 and 4.
"""
s2 = {i for i in range(21) if i % 2 != 0}
s3 = {i for i in range(21) if i % 3 != 0}
s4 = {i for i in range(21) if i % 4 != 0}
