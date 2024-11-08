#!/usr/bin/env python3

from decimal import Decimal
import subprocess
import sys
import os

VARIANCE_ACCEPTED = 5
NUMBER_OF_RUNS = 5


def compute_mean_exec_time(file, outfile):
    with open(file, 'r') as f:
        times = [Decimal(line.strip()) for line in f if line.strip()]

    # Sort and get all but the first and last values
    times.sort()
    avg_times = times[1:NUMBER_OF_RUNS-1]

    # Calculate the mean of the values
    time = sum(avg_times) / Decimal(NUMBER_OF_RUNS-2)

    # Compute absolute deviations from the mean
    val1, val2, val3 = avg_times
    val11 = abs(val1 - time)
    val12 = abs(val2 - time)
    val13 = abs(val3 - time)

    max_deviation = max(val11, val12, val13)

    variance = (max_deviation / time) * 100 if time != 0 else 0
    variance = round(variance, 5)

    # Compare variance with the accepted threshold
    if variance > VARIANCE_ACCEPTED:
        print(
            f"[WARNING] Variance is above threshold, unsafe performance measurement",
            file=outfile)
        print(f"        => max deviation={variance}%, tolerance={
              VARIANCE_ACCEPTED}%", file=outfile)
        print(f"[INFO] Maximal deviation from arithmetic mean of 3 average runs: {
              variance}%", file=outfile)
    else:
        print(f"[INFO] Maximal deviation from arithmetic mean of 3 average runs: {
              variance}%", file=outfile)

    return time


def run_benchmark(command, outfile=sys.stdout):
    print(f"[INFO] Running {NUMBER_OF_RUNS} times {command}...", file=outfile)
    print(f"[INFO] Maximal variance authorized on 3 average runs: {
          VARIANCE_ACCEPTED}%...", file=outfile)

    # Run the command NUMBER_OF_RUNS times and capture output
    with open("____tempfile.data.polybench", "w") as f:
        for _ in range(NUMBER_OF_RUNS):
            result = subprocess.run(
                command, shell=True, stdout=f, stderr=f)

    # Compute the mean execution time
    processed_time = compute_mean_exec_time(
        "____tempfile.data.polybench", outfile)
    print(f"[INFO] Normalized time: {processed_time}", file=outfile)

    # Clean up the temporary file
    os.remove("____tempfile.data.polybench")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 time_benchmark.py <binary_name>")
        print("Example: python3 time_benchmark.py './a.out'")
        print("Note: the file must be a Polybench program compiled with -DPOLYBENCH_TIME")
        sys.exit(1)

    binary_name = sys.argv[1]
    run_benchmark(binary_name)
