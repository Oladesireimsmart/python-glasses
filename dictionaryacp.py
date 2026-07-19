students={
    "issy": "math",
    "John,b": "science",
    "Alice": "english"
}

print(students.get("issy"))

students["John,g"] = "history"

students["Jhon,b"] = "biology"

students.pop("Alice")

print("Total students:", len(students))

print("The students are:", students)