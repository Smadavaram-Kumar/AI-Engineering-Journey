import csv


file = open("notes.txt", "r")     # open for reading
content = file.read()              # read everything
print(content)                    # print the content
file.close()                       # close the file to free up resources and it doesn't automatically close when done, so we have to do it manually


# Rule: From this day forward, every time you open a file, use with. No exceptions.
with open("notes.txt", "r") as file: # with will automatically close the file when done
    content = file.read()
    print(content)



# Method 2: readline() — ONE line at a time
with open("notes.txt", "r") as f:
    first_line = f.readline()    # gets line 1
    second_line = f.readline()   # gets line 2
    print(first_line)
    print(second_line)

with open("notes.txt", "r") as f:
    lines = f.readlines()    
    print(lines)   # prints a list of lines, each line is an element in the list



with open("notes.txt", "r") as f:
    for line in f:
        print(line)    # prints each line one at a time, this is memory efficient because it doesn't read the whole file into memory at once, it reads one line at a time


with open("../day3/notes2.txt", "w") as f:
    f.write("This is a new file.\n")   # write to the file, if the file doesn't exist, it will be created, if it does exist, it will be overwritten
    f.write("This is the second line.\n")  # write another line to the file 

with open("../day3/notes2.txt", "r") as f: 
    print(f.read())  # append to the file, if the file doesn't exist, it will be created, if it does exist, it will be appended to


# Reading
with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Each row is a LIST of strings: ['Smadavaram', 'Hello, world!', '25']

# Writing
rows = [
    ["name", "quote", "age"],
    ["Smadavaram", "Hello, world!", 25],
    ["Anita", "Data is the new oil.", 30],
]



with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    #writer.writerow(["sumanth", "Hello, world!", 2333])  # write a single row
    writer.writerows(rows)  # write multiple rows at once, it will overwrite the previous content of the file, so be careful when using "w" mode, if you want to append to the file, use "a" mode instead



import json

data = {
    "name": "Smadavaram",
    "skills": ["Python", "Power Platform"],
    "experience_years": 3,
    "is_learning_ai": True
}

# Writing to a file
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


text = json.dumps(data, indent=2, ensure_ascii=False)
print(type(text))