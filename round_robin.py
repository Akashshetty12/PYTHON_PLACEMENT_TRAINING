from collections import deque

def find(task, time):
    queue = deque(task)              # Task durations
    ids = deque(i + 1 for i in range(len(task)))  # Task IDs (1-based)
    tot = 0                          # Total time
    completed_order = []            # To store the order of completion

    while queue:
        for i in range(min(3, len(queue))):  # Process up to 3 tasks per round
            current_task = queue.popleft()
            current_id = ids.popleft()

            if current_task <= time:
                tot += current_task
                completed_order.append((current_id, tot))  # Record completion time
            else:
                tot += time
                queue.append(current_task - time)  # Re-add remaining work
                ids.append(current_id)

    print("Total time:", tot)
    print("Completion order (ID, completion time):", completed_order)

# Example
task = [10, 5, 8]
time = 4
find(task, time)
