def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            # wrap risky operation in try-except
            try:
                ratio = values[i] / (values[j] - values[i])
            except ZeroDivisionError as e:
                print(f"ZeroDivisionError for indices ({i},{j}): {e}")
            except Exception as e:
                print(f"Error for indices ({i},{j}): {e}")
            else:
                results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))