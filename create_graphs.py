import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

results = Path("results")
graphs = Path("graphs")
graphs.mkdir(exist_ok=True)

# Read CSV files
df = pd.read_csv(results / "sorting_results.csv")
fib = pd.read_csv(results / "fibonacci_results.csv")

# 1. Sorting - Execution Time
plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    data = df[df["Algorithm"] == algorithm]
    avg = data.groupby("Input_Size")["Execution_Time_ms"].mean()
    plt.plot(avg.index, avg.values, marker="o", label=algorithm)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")
plt.title("Sorting Algorithms - Execution Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs / "sorting_execution_time.png", dpi=300)
plt.close()

# 2. Sorting - Memory Usage
plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    data = df[df["Algorithm"] == algorithm]
    avg = data.groupby("Input_Size")["Memory_Usage_KB"].mean()
    plt.plot(avg.index, avg.values, marker="o", label=algorithm)

plt.xlabel("Input Size")
plt.ylabel("Memory Usage (KB)")
plt.title("Sorting Algorithms - Memory Consumption")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs / "sorting_memory_usage.png", dpi=300)
plt.close()

# 3. Fibonacci - Execution Time
plt.figure(figsize=(10, 6))

for algorithm in fib["Algorithm"].unique():
    data = fib[fib["Algorithm"] == algorithm]
    plt.plot(
        data["Input_n"],
        data["Execution_Time_ms"],
        marker="o",
        label=algorithm
    )

plt.xlabel("Input n")
plt.ylabel("Execution Time (ms)")
plt.title("Fibonacci Algorithms - Execution Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs / "fibonacci_execution_time.png", dpi=300)
plt.close()

# 4. Fibonacci - Memory Usage
plt.figure(figsize=(10, 6))

for algorithm in fib["Algorithm"].unique():
    data = fib[fib["Algorithm"] == algorithm]
    plt.plot(
        data["Input_n"],
        data["Memory_Usage_KB"],
        marker="o",
        label=algorithm
    )

plt.xlabel("Input n")
plt.ylabel("Memory Usage (KB)")
plt.title("Fibonacci Algorithms - Memory Consumption")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs / "fibonacci_memory_usage.png", dpi=300)
plt.close()

print("4 graphs created successfully in the graphs/ folder.")