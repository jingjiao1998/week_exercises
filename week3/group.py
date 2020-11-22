# group exercise
# example data structure solution
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    }
    ,"Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    }
    ,
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

def mean(data):
    """Compute the mean of a non-empty list of numbers."""
    return sum(data) / len(data)

# the maximum age of people in the group
print(max(person["age"] for person in group.values()))  # 34
# the average (mean) number of relations among members of the group
print(mean([len(person["relations"]) for person in group.values()]))  # 1.5
# the maximum age of people in the group that have at least one relation
print(max(person["age"] for person in group.values() if person["relations"]))  # 34
# the maximum age of people in the group that have at least one friend
print(max(person["age"] for person in group.values() if "friend" in person["relations"].values()))  # 28