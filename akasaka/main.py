import argparse
import os
import sys
import multiprocessing

from .loader import load_class
from .task import AkasakaTask

from tqdm import tqdm


akasaka_task = None


def execute(args):
    global akasaka_task

    if akasaka_task.is_executed(**args):
        return
    akasaka_task(**args)


def main():
    global akasaka_task

    parser = argparse.ArgumentParser(description='Dynamically load a Python class from a module.', add_help=False)
    parser.add_argument('module_path', type=str, help='The module path in the format "module.submodule.ClassName"')
    parser.add_argument('--num_process', type=int, default=multiprocessing.cpu_count(), help='Number of processes to use (default: number of CPU cores)')
    parser.add_argument('--chunksize', type=int, default=1, help='Number of tasks to be sent to a worker process at a time (default: 1)')
    parser.add_argument('-h', '--help', action='store_true', help='Show help message for task and exit')
    parser.add_argument('-H', '--hel-akasaka', action='help', help='Show Akasaka help message and exit')
    args, remaining_args = parser.parse_known_args()
    
    module_path = args.module_path
    num_process = args.num_process
    chunksize = args.chunksize
    
    if args.help:
        remaining_args += ["-h"]

    # Add the current working directory to the sys.path so that the module can be found
    sys.path.append(os.getcwd())
    # Load the class from the module
    loaded_class = load_class(module_path)
    print(f"Successfully loaded class '{loaded_class.__name__}' from module '{args.module_path}'.")
    # Check if the loaded class is a subclass of 'AkasakaTask'
    if not issubclass(loaded_class, AkasakaTask):
        raise ValueError("The loaded class should be a subclass of 'AkasakaTask'.")

    # Initialize the task with the remaining command line arguments
    akasaka_task = loaded_class(args=remaining_args)

    # Generate a list of tasks to be executed
    tasks = akasaka_task.generate_tasks()
    tasks = list(tasks)
    print(f"Generated {len(tasks)} tasks to be executed.")

    pool = multiprocessing.Pool(processes=num_process)
    _ = list(tqdm(pool.imap_unordered(execute, tasks, chunksize=chunksize), total=len(tasks)))

    pool.close()
    pool.join()
