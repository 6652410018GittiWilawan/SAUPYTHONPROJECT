def calculate_package_cost(num_people):
    if num_people >= 1 and num_people <= 2:
        return num_people * 300
    elif num_people >= 3 and num_people <= 5:
        return num_people * 250
    elif num_people >= 6 and num_people <= 10:
        return num_people * 210
    elif num_people >= 11:
        return num_people * 150

def calculate_summary_costs(num_people_list):
    total_cost = 0
    min_cost = float('inf')
    max_cost = float('-inf')

    for num_people in num_people_list:
        cost = calculate_package_cost(num_people)
        total_cost += cost

        if cost < min_cost:
            min_cost = cost

        if cost > max_cost:
            max_cost = cost

    average_cost = total_cost / len(num_people_list)
    return total_cost, min_cost, max_cost, average_cost

def gg():
    num_people_list = []
    group_leader_name = input("Enter Group Leader Name: ")
    contact_number = input("Enter Contact Number: ")

    while True:
        num_people = int(input("Enter Number of People (or -1 to finish): "))

        if num_people == -1:
            break

        num_people_list.append(num_people)

    total_cost, min_cost, max_cost, average_cost = calculate_summary_costs(num_people_list)

    print(f"Group Leader: {group_leader_name}")
    print(f"Contact Number: {contact_number}")
    print(f"Total Cost for All Packages: {total_cost} Baht")
    print(f"Minimum Cost for a Package: {min_cost} Baht")
    print(f"Maximum Cost for a Package: {max_cost} Baht")
    print(f"Average Cost per Package: {average_cost} Baht")


gg()