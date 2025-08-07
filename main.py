from simulation.runner import run_simulation
import time

def main():
    T = 1 * 365.25 * 24 * 3600  # 1 year

    start_time = time.perf_counter()  # Record start time

    bodies, solution = run_simulation(T, steps=100, file='py')

    # Execution process time
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("Integration complete!")
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
