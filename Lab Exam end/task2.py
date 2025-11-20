"""
Module overview
---------------
Provides a simple Quick Sort implementation specialized for sorting a gaming
leaderboard: a list of (player_name, score) tuples. The sort orders players
by score in descending order (highest score first). The algorithm selects the
middle element's score as the pivot and partitions the input into three
groups (greater than, equal to, and less than the pivot), recursively
sorting the non-equal partitions.
Function: quick_sort(players)
-----------------------------
Parameters:
    players (list[tuple[str, int]]):
        A list of tuples where each tuple is (player_name, score). The
        function expects comparable score values (typically integers).
Returns:
    list[tuple[str, int]]:
        A new list of the same (player_name, score) tuples sorted in
        descending order by score.
Behavior and guarantees:
    - Descending order: players with higher scores appear before those with
      lower scores.
    - Stability: ordering among players with equal scores is preserved (stable),
      because equal-score elements are collected into a 'middle' list that
      preserves their original relative order.
    - Non-mutating: the function returns a new sorted list and does not rely
      on in-place mutations of the input list.
Algorithmic complexity:
    - Average time complexity: O(n log n)
    - Worst-case time complexity: O(n^2) (e.g., adversarial inputs against the
      chosen pivot strategy)
    - Additional space: O(n) auxiliary space for partition lists; recursion
      depth O(log n) on average (O(n) worst case).
Notes and usage example:
    - Suitable for small-to-medium leaderboards where readability and stability
      are desirable.
    - Example:
        sorted_players = quick_sort(players)
        # sorted_players -> [("Zara", 100), ("Alice", 95), ("Bob", 70)]
Testing:
    The module includes a simple test function that asserts correct ordering
    for a representative sample of players and duplicate scores.
Limitations and extensions:
    - If scores can be non-numeric or require custom comparison, adapt the
      pivot selection and comparison logic accordingly.
    - For very large lists or performance-critical contexts, consider an
      in-place quicksort or Timsort (Python's built-in sorted()) for better
      worst-case guarantees and lower memory overhead.
Quick Sort for Gaming Leaderboard
----------------------------------

Purpose:
    Sort a list of players based on their scores in *descending* order
    using the Quick Sort algorithm.

Input Format:
    A list of tuples: (player_name, score)

Example:
    players = [("Alice", 95), ("Bob", 70), ("Zara", 100)]

Output:
    [("Zara", 100), ("Alice", 95), ("Bob", 70)]

Algorithm Notes:
    - Uses a pivot (middle element)
    - Recursively sorts elements greater than, equal to, and less than the pivot
    - Stable ordering for equal scores
"""


def quick_sort(players):
    """Sorts players by score in descending order using Quick Sort."""
    
    if len(players) <= 1:
        return players

    # Choose pivot = score of middle player
    pivot = players[len(players) // 2][1]

    # Partition the list
    left = [p for p in players if p[1] > pivot]     # higher scores first
    middle = [p for p in players if p[1] == pivot]  # equal scores
    right = [p for p in players if p[1] < pivot]    # lower scores

    # Recursively sort
    return quick_sort(left) + middle + quick_sort(right)


# ------------------------------------------------
# TEST CASES
# ------------------------------------------------

def test_quick_sort():
    print("\nRunning Quick Sort tests...")

    players = [
        ("A", 50),
        ("B", 80),
        ("C", 30),
        ("D", 80),
        ("E", 99),
        ("F", 10)
    ]

    sorted_output = quick_sort(players)

    expected_output = [
        ("E", 99),
        ("B", 80),
        ("D", 80),
        ("A", 50),
        ("C", 30),
        ("F", 10)
    ]

    assert sorted_output == expected_output, "Quick Sort failed!"

    print("Test passed successfully! Leaderboard sorted correctly.\n")


if __name__ == "__main__":
    test_quick_sort()
