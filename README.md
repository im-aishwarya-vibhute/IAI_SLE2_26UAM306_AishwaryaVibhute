# IAI_SLE2_26UAM306_AishwaryaVibhute

# SLE-2: Empirical Performance Analysis of BFS and DFS

## Course

02AML204 – Introduction to Artificial Intelligence

## Objective

The objective of this experiment is to compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) using actual experimental measurements.

## Problem Used

A small graph is used as the search problem.

Both BFS and DFS search for the same goal node from the same starting node.

## Algorithms

### BFS

Breadth First Search explores nodes level by level and uses a queue.

### DFS

Depth First Search explores a path deeply before backtracking and uses a stack.

## Profiling Method

The Python `timeit` module is used to measure execution time.

A manual node counter is used to count the number of nodes expanded.

## Metrics

The experiment measures:

- Execution time
- Nodes expanded
- Search path

## Number of Runs

The experiment is repeated three times.

## Files

- `bfs_vs_dfs.py` – Python implementation
- `profiling_results.txt` – Experimental results
- `AI_Contribution_Log.md` – AI usage information
- `screenshots/` – Output screenshots

## How to Run

1. Install Python.
2. Open Command Prompt.
3. Go to the project folder.
4. Run:

```text
python bfs_vs_dfs.py
