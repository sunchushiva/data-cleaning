from data import data


# Filter by City: Find all entries where the city is "New York."
def cityFunction(dictionary):
    return dictionary["city"] == "New York"


cityFilter = filter(cityFunction, data)
cityFilter = list(cityFilter)


# Filter by Age: Get all people under the age of 30.
def ageFunction(dictionary):
    return dictionary["age"]<30


ageFilter = filter(ageFunction, data)
ageFilter = list(ageFilter)


# Filter by Occupation: Retrieve a list of all "Engineer" occupations.
def occupationFunction(dictionary):
    return dictionary["occupation"] == "Engineer"


occupationFilter = filter(occupationFunction, data)
occupationFilter = list(occupationFilter)


#Chat-gpt review

### Overall Suggestions for Time and Space Complexity

# 1. **For large datasets**:
#  - If your data grows large, consider switching to list comprehensions instead of `filter`, as list comprehensions tend to have slightly better performance.
#  - Example for City Filter:
#    ```python
# cityFilter = [item for item in data if item["city"] == "New York"]
#    ```
#  - This is a minor optimization but can make a difference with big datasets.

# 2. **Improving Space Complexity**:
#  - Since `filter` only creates an iterator and doesn’t store a list in memory until `list()` is called, it's quite memory-efficient.
#  - If your filters are being used separately, this approach is already efficient. For chained filters, using generators can help in memory efficiency.

