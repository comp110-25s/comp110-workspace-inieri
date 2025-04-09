"""A Program to Plan a Tea Party"""

__author__: str = "730543747"


def main_planner(guests: int) -> None:
    """Combine functions and print outputs"""
    print("A Cozy Tea Party For " + str(guests) + " people!"),
    print("Tea Bags: " + str(tea_bags(people=guests))),
    print("Treats: " + str(treats(people=guests))),
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Calculate number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate combined cost of tea and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
