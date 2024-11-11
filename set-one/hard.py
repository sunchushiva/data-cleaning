from data import data

# Complex Condition: Retrieve a list of people who are either "Manager" or "Engineer" and have experience of 10 years or more.

def complexFunctionOne(dictionary):
    if(dictionary["occupation"]=="Manager" or dictionary["occupation"]=="Engineer"):
        return dictionary["experience"] >= 10
    

complexFilterOne = filter(complexFunctionOne, data)
complexFilterOne = list(complexFilterOne)


# Advanced Range: Filter out entries where salary is either below 60,000 or above 130,000.
def complexFunctionTwo(dictionary):
    return 60_000 <= dictionary["salary"] <= 130_000

complexFilterTwo = filter(complexFunctionTwo, data)
complexFilterTwo = list(complexFilterTwo)


# Nested Filters: First, filter by city "San Francisco," and then within this result, find people with experience less than 10 years and salary above 80,000.
def complexFunctionThree(dictionary):
    if dictionary["city"] == "San Francisco":
        return dictionary["experience"] < 10 and dictionary["salary"] > 80_000

complexFilterThree = filter(complexFunctionThree, data)
complexFilterThree = list(complexFilterThree)

# Exclusion Criteria: Retrieve all entries except those with occupation as "Intern."
def complexFunctionFour(dictionary):
    return dictionary["occupation"] != "Intern"


complexFilterFour = filter(complexFunctionFour, data)
complexFilterFour = list(complexFilterFour)


# Salary and Age Combination: Find entries where salary is more than 80,000 and age is under 40, but exclude entries with occupation as "Designer."
def complexFunctionFive(dictionary):
    if dictionary["occupation"] != "Designer":
        return dictionary["salary"] > 80_000 and dictionary["age"] < 40


complexFilterFive = filter(complexFunctionFive, data)
complexFilterFive = list(complexFilterFive)
