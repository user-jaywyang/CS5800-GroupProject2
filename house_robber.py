# Abhilash Singh,  Alex Williams,  Jay Yang
# CS5800 - Summer 2025 - Group Project
# Dynamic Programming Problem 1: House Robber (Leetcode 198)
# This script reads JSON input for the 'House Robber' problem, runs the algorithm, and creates a timing graph.

# RUN BY ENTERING "python house_robber.py house_robber_input.json" IN COMMAND LINE

import json
import time
import sys
import matplotlib.pyplot as plt
from typing import List

def rob(nums: List[int]) -> int:
    """
    Returns the maximum amount of money that can be robbed without robbing two adjacent houses.
    Uses a bottom-up iterative dynamic programming approach with a full DP array.
    """
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

def main(input_file: str):
    """
    Reads test cases from a JSON file and runs the House Robber algorithm on each.
    Prints output and timing results for each test case.
    Also generates a timing graph based on input sizes.
    """
    with open(input_file, 'r') as f:
        test_cases = json.load(f)

    results = []
    timing_data = []

    for case in test_cases:
        nums = case["input"]
        expected = case.get("expected", None)

        start = time.perf_counter()
        result = rob(nums)
        end = time.perf_counter()

        elapsed_time = end - start
        results.append({
            "input": nums,
            "output": result,
            "expected": expected,
            "time_seconds": elapsed_time
        })

        timing_data.append((len(nums), elapsed_time))

    # Print results
    for res in results:
        print(f"Input size: {len(res['input'])}")
        print(f"Output: {res['output']}")
        if res["expected"] is not None:
            print(f"Expected: {res['expected']}")
            print(f"Pass: {res['output'] == res['expected']}")
        print(f"Time: {res['time_seconds']:.8f} seconds\n")

    # Plot timing graph
    sizes, times = zip(*timing_data)
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o')
    plt.title("House Robber Timing Analysis (Iterative DP)")
    plt.xlabel("Input Size (Number of Houses)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    graph_filename = "house_robber_timing_graph.png"
    plt.savefig(graph_filename)
    print(f"Timing graph saved to: {graph_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python house_robber.py <input_file.json>")
    else:
        main(sys.argv[1])


