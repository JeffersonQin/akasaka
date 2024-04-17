import argparse
import os
import sys
import multiprocessing

from .loader import load_class
from .task import AkasakaTask
from .torch_task import AkasakaTorchTask


def main():
    parser = argparse.ArgumentParser(description='Dynamically load a Python class from a module.', add_help=False)
    parser.add_argument('module_path', type=str, help='The module path in the format "module.submodule.ClassName"')
    parser.add_argument('--num_process', type=int, default=multiprocessing.cpu_count(), help='Number of processes to use, for normal task (default: number of CPU cores)')
    parser.add_argument('--chunksize', type=int, default=1, help='Number of tasks to be sent to a worker process at a time, for normal task (default: 1)')
    parser.add_argument('--devices', type=int, nargs='+', default=[], help='The devices to run the task on, for torch task (default: [])')
    parser.add_argument('-h', '--help', action='store_true', help='Show help message for task and exit')
    parser.add_argument('-H', '--hel-akasaka', action='help', help='Show Akasaka help message and exit')
    args, remaining_args = parser.parse_known_args()
    
    module_path = args.module_path
    
    if args.help:
        remaining_args += ["-h"]

    # Add the current working directory to the sys.path so that the module can be found
    sys.path.append(os.getcwd())
    # Load the class from the module
    loaded_class = load_class(module_path)
    print(f"Successfully loaded class '{loaded_class.__name__}' from module '{args.module_path}'.")

    # Initialize the task with the remaining command line arguments
    akasaka_task = loaded_class(args=remaining_args)

    if issubclass(loaded_class, AkasakaTask):
        from .executor import akasaka_execute
        num_process = args.num_process
        chunksize = args.chunksize
        akasaka_execute(akasaka_task, num_process, chunksize)
        return

    if issubclass(loaded_class, AkasakaTorchTask):
        devices = args.devices
        if len(devices) == 1:
            from .torch_single_executor import akasaka_torch_single_execute
            akasaka_torch_single_execute(akasaka_task, devices[0])
        else:
            from .torch_executor import akasaka_torch_execute
            akasaka_torch_execute(akasaka_task, module_path, remaining_args, devices)
        return

    raise ValueError("The loaded class should be a subclass of 'AkasakaTask' or 'AkasakaTorchTask'.")
