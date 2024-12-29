class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())  # Frequency of the most common task

        # Calculate the number of idle slots
        max_count_tasks = sum(1 for task in task_counts if task_counts[task] == max_count)
        intervals = (max_count - 1) * (n + 1) + max_count_tasks

        # The result is the maximum of the intervals calculated or the total number of tasks
        return max(intervals, len(tasks))
