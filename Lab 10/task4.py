def calculate_average(scores):
    """Returns the average of the scores."""
    return sum(scores) / len(scores) if scores else 0
def find_highest(scores):
    """Returns the highest score."""
    return max(scores) if scores else None
def find_lowest(scores):
    """Returns the lowest score."""
    return min(scores) if scores else None
def process_scores(scores):
    """Processes the scores and prints average, highest, and lowest values."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
scores = [10,20,30,40,50]
process_scores(scores)