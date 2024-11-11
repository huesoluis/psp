import os

def print_recursive_parents():
    current_pid = os.getpid()
    parent_pid = os.getppid()
    
    # List to store all the PIDs in the chain
    parent_chain = [(current_pid, parent_pid)]
    
    while parent_pid != 1:  # PID 1 is usually the init/systemd process
        try:
            current_pid = parent_pid
            parent_pid = os.getppid()
            parent_chain.append((current_pid, parent_pid))
        except Exception as e:
            break
    
    # Print the full chain of parent processes
    for pid, ppid in parent_chain:
        print(f"PID: {pid}, Parent PID: {ppid}")

# Run the recursive parent function
print_recursive_parents()

