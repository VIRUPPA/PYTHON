def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x:x[0])

    
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged

intervals = [[1, 3], [10, 11], [8, 10], [9, 12]]
print("Merged Intervals:", merge_intervals(intervals))


