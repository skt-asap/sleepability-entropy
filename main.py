from sorting import sorting_process
from probability import probability_process
from probability2 import probability2_process
from entropy_zero import entropy_zero_process

def run_all_processes():
    print("Starting all processes...")
    sorting_process()
    probability_process()
    probability2_process()
    entropy_zero_process()
    print("All processes completed successfully.")

if __name__ == "__main__":
    run_all_processes()