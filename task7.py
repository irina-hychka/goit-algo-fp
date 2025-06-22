import random
import matplotlib.pyplot as plt

"""
Task 6: Using the Monte Carlo Method
"""

def roll_dice_simulation(trials: int):
    """
    Simulate rolling two dice a given number of times using Monte Carlo method.

    Args:
        trials (int): Number of dice rolls.

    Returns:
        dict: Dictionary where keys are sums (2-12) and values are empirical probabilities.
    """
    if trials <= 0:
        print("Number of trials must be positive.")
        return {}

    sum_counts = {total: 0 for total in range(2, 13)}

    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    probabilities = {total: count / trials for total, count in sum_counts.items()}
    return probabilities


def theoretical_dice_probabilities():
    """
    Return exact theoretical probabilities for each possible dice sum (2-12).

    Returns:
        dict: Dictionary of exact probabilities based on 36 combinations.
    """
    return {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }


def display_probability_table(empirical: dict, theoretical: dict):
    """
    Print a formatted table comparing empirical and theoretical probabilities.
    """
    print()
    print("Sum | Empirical Probability (%) | Theoretical Probability (%)")
    print("---------------------------------------------------------------")
    for total in sorted(empirical.keys()):
        empirical_pct = empirical[total] * 100
        theoretical_pct = theoretical[total] * 100
        print(f" {total:2} | {empirical_pct:23.2f} | {theoretical_pct:25.2f}")
    print()


def plot_probability_comparison(empirical: dict, theoretical: dict):
    """
    Plot the comparison of empirical vs theoretical probabilities.
    """
    sums = sorted(empirical.keys())
    empirical_values = [empirical[total] for total in sums]
    theoretical_values = [theoretical[total] for total in sums]

    plt.figure(figsize=(10, 6))
    plt.plot(sums, empirical_values, 'o-', label='Monte Carlo Simulation', color='darkorange')
    plt.plot(sums, theoretical_values, 's--', label='Theoretical Probability', color='teal')
    plt.title("Dice Roll Sum Probabilities: Monte Carlo vs Theoretical")
    plt.xlabel("Dice Sum")
    plt.ylabel("Probability")
    plt.xticks(sums)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Usage
if __name__ == "__main__":
    num_trials = 1_000_000

    empirical_probs = roll_dice_simulation(num_trials)
    exact_probs = theoretical_dice_probabilities()

    display_probability_table(empirical_probs, exact_probs)
    plot_probability_comparison(empirical_probs, exact_probs)
