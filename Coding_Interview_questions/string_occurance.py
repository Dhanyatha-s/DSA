"""
Docstring for Coding_Interview_questions.string_occurance
Find the occurrence of particular String  of length N
"""

def count(input1,input2,input3):
    return  input1.count(input3)
    # print(f"The Number of times the String {input3} occurred are: {occurrence}  ")


input1 = "Helloworld"
input2 = 10
input3 = "H"

occurrence = count(input1, input2, input3) 
print(f"The Number of times the String {input3} occurred are: {occurrence}  ")
