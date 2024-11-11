from data import data

# Filter by Experience: Find all entries with experience of 5 years or more.
def experienceFunction(dictionary):
    return dictionary["experience"]>=5

experienceFilter = filter(experienceFunction, data)
experienceFilter = list(experienceFilter)


# Filter by Salary Range: Retrieve all entries where salary is between 70,000 and 100,000.
def salaryFunction(dictionary):
    return 70_000 < dictionary["salary"] < 100_000

salaryFilter = filter(salaryFunction, data)
salaryFilter = list(salaryFilter)


# Multiple Conditions: Get a list of entries where occupation is "Analyst" and city is "Boston."
def multipleConditions(dictionary):
    return dictionary["occupation"] == "Analyst" and dictionary["city"] == "Boston"

multipleFilter = filter(multipleConditions, data)
multipleFilter = list(multipleFilter)


# Combined Filter: Find entries where age is above 30 and salary is over 100,000.
def combinedFilterFunction(dictionary):
    return dictionary["age"] > 30 and dictionary["salary"] > 100_000

combinedFilter = filter(combinedFilterFunction, data)
combinedFilter = list(combinedFilter)
