
# Fractional Knapsack and Job Scheduling

def fractional_knapsack(weights, values, capacity):
    # Create a list to store value-to-weight ratio and item details
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort items in decreasing order of value-to-weight ratio
    items.sort(reverse=True)
    total_profit = 0

    # Select items with the highest ratio first
    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Take the complete item
            total_profit += value
            capacity -= weight
        else:
            # Take only the fraction that fits
            total_profit += ratio * capacity
            capacity = 0

    return total_profit


def job_scheduling(jobs):
    # Sort jobs by decreasing profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create empty time slots
    slots = [None] * max_deadline
    total_profit = 0

    # Schedule each job in the latest available slot
    for job_id, deadline, profit in jobs:
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Remove empty slots from the job sequence
    sequence = [job for job in slots if job is not None]

    return sequence, total_profit


def main():
    # Input for Fractional Knapsack
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    # Calculate maximum knapsack profit
    profit = fractional_knapsack(weights, values, capacity)
    print("Maximum Fractional Knapsack Profit:", profit)

    # Jobs are represented as (job ID, deadline, profit)
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15)
    ]

    # Calculate the optimal job sequence
    sequence, profit = job_scheduling(jobs)
    print("Optimal Job Sequence:", sequence)
    print("Maximum Job Profit:", profit)


if __name__ == "__main__":
    main()
