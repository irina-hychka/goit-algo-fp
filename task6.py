"""
Task 6: Greedy Algorithms and Dynamic Programming
"""

from typing import Dict, List, Tuple


def solve_with_greedy_strategy(menu: Dict[str, Dict[str, int]], max_budget: int) -> Tuple[List[str], int, int]:
    """
    Selects dishes using a greedy strategy based on the highest
    calorie-per-cost ratio. This approach does not guarantee the optimal solution.

    Args:
        menu: Dictionary where each key is a dish name and value is a dictionary with 'cost' and 'calories'.
        max_budget: Maximum budget allowed for selecting dishes.

    Returns:
        A tuple with:
        - List of selected dish names
        - Total calories of selected dishes
        - Total cost spent
    """
    # Sort dishes by calories per unit cost (descending)
    sorted_menu = sorted(menu.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)

    selected_dishes = []
    total_calories = 0
    budget_left = max_budget

    for dish_name, properties in sorted_menu:
        if properties['cost'] <= budget_left:
            selected_dishes.append(dish_name)
            total_calories += properties['calories']
            budget_left -= properties['cost']

    return selected_dishes, total_calories, max_budget - budget_left


def solve_with_dynamic_programming(menu: Dict[str, Dict[str, int]], max_budget: int) -> Tuple[List[str], int, int]:
    """
    Selects dishes using dynamic programming to maximize total calories
    within a fixed budget. Guarantees an optimal solution.

    Args:
        menu: Dictionary where each key is a dish name and value is a dictionary with 'cost' and 'calories'.
        max_budget: Maximum budget allowed for selecting dishes.

    Returns:
        A tuple with:
        - List of selected dish names
        - Maximum total calories achievable
        - Total cost spent
    """
    dishes = list(menu.items())
    num_dishes = len(dishes)

    # Initialize DP table: rows = items, columns = budgets
    dp = [[0 for _ in range(max_budget + 1)] for _ in range(num_dishes + 1)]

    # Fill DP table
    for i in range(1, num_dishes + 1):
        dish_name, values = dishes[i - 1]
        cost, calories = values['cost'], values['calories']
        for budget in range(max_budget + 1):
            if cost <= budget:
                dp[i][budget] = max(dp[i - 1][budget], calories + dp[i - 1][budget - cost])
            else:
                dp[i][budget] = dp[i - 1][budget]

    # Backtrack to find selected dishes
    selected_dishes = []
    remaining_budget = max_budget
    for i in range(num_dishes, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            dish_name, values = dishes[i - 1]
            selected_dishes.append(dish_name)
            remaining_budget -= values['cost']

    selected_dishes.reverse()
    total_calories = dp[num_dishes][max_budget]
    total_spent = max_budget - remaining_budget

    return selected_dishes, total_calories, total_spent


# Usage
if __name__ == "__main__":
    menu_items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    # Greedy approach
    greedy_selection, greedy_total_calories, greedy_spent = solve_with_greedy_strategy(menu_items, budget)
    print("--- Greedy Algorithm ---")
    print(f"Selected dishes: {greedy_selection}")
    print(f"Total calories: {greedy_total_calories}")
    print(f"Total cost: {greedy_spent}\n")

    # Dynamic programming approach
    dp_selection, dp_total_calories, dp_spent = solve_with_dynamic_programming(menu_items, budget)
    print("--- Dynamic Programming ---")
    print(f"Selected dishes: {dp_selection}")
    print(f"Total calories: {dp_total_calories}")
    print(f"Total cost: {dp_spent}")
