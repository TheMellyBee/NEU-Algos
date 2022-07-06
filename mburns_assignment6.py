# author: Melanie Burns
# Due: July 5, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 6, but everything else is my own
import pytest


def minimal_removal(activities: list[tuple[int, int]]) -> int:
    # which takes a list of activities, and returns the
    # minimum number of activities that should be removed
    # in order to schedule the remaining activities.
    # this should be a greedy algo

    # This is mainly from code given in class as it was a very similar problem
    activities.sort(key=lambda x: x[1])     # sort by finish
    result = [activities[0]]                 # this gets the start of the first
    for activity in activities[1:]:
        if activity[0] >= result[-1][1]:    # Gets the end time of the last result and compares to start
            result.append(activity)
    return len(activities) - len(result)


def minAvgCompletion1(tasks: list[int]) -> float:
    # which returns the minimum average comple-
    # tion time for tasks with processing time.
    tasks.sort()
    result = tasks[0]
    # following the formula after greedy sorting for min
    for task in tasks[1:]:
        new_time = result + task
        result += new_time
    return result/len(tasks)



def minAvgCompletion2(tasks: list[list[int]]) -> float:
    # returns the minimum average completion time
    # for tasks with processing time and release time.
    task_time = [(task[1]+task[0], i) for i, task in enumerate(tasks)]
    task_time.sort(key=lambda x: x[0])
    result = task_time[0][0]
    # following the formula after greedy sorting for min
    for task, position in task_time[1:]:
        new_time = result + task
        result += new_time
    final_task_position =  task_time[-1][1]
    result -= tasks[final_task_position][1]
    return result/len(task_time)


@pytest.mark.parametrize("activities,expected", [
    ([(0, 1), (0, 1), (0, 1)], 2),
    ([(0, 1), (1, 2)], 0),
    ([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)], 7)
])
def test_minimal_removal(activities: list[tuple[int, int]], expected: int):
    assert minimal_removal(activities) == expected


@pytest.mark.parametrize("tasks,expected", [
    ([3, 5], 5.5),

])
def test_minAvgCompletion1(tasks: list[int], expected: float):
    assert minAvgCompletion1(tasks) == expected


@pytest.mark.parametrize("tasks,expected", [
    ([[3, 5], [5, 2]], 8.5),
    ([[3, 5], [5, 4]], 10.0)
])
def test_minAvgCompletion2(tasks: list[list[int]], expected: float):
    assert minAvgCompletion2(tasks) == expected


if __name__ == '__main__':
    pytest.main()
