# Akasaka

Dynamic mutiprocess preprocessing task loader and dispatcher.

To be brief, akasaka enables you to write a task class and run it in parallel with a simple command. It features

* Argument parsing through `argparse`
* Cache management, i.e. you can override `is_executed` to check if the task is already executed
* Automatic parallelization
* Some helper functions to make your life easier (to be added later)

## Install

```bash
pip install akasaka
```

## Usage

```bash
$ akasaka -H
usage: akasaka [--num_process NUM_PROCESS] [--chunksize CHUNKSIZE] [--devices DEVICES [DEVICES ...]] [-h] [-H] module_path

Dynamically load a Python class from a module.

positional arguments:
  module_path           The module path in the format "module.submodule.ClassName"

optional arguments:
  --num_process NUM_PROCESS
                        Number of processes to use, for normal task (default: number of CPU cores)
  --chunksize CHUNKSIZE
                        Number of tasks to be sent to a worker process at a time, for normal task (default: 1)
  --devices DEVICES [DEVICES ...]
                        The devices to run the task on, for torch task (default: [])
  -h, --help            Show help message for task and exit
  -H, --hel-akasaka     Show Akasaka help message and exit
```

Write a task class of the subclass of `AsakasaTask` and implement needed methods. Take a look at the examples in the [`examples` directory](./examples).

For PyTorch CUDA tasks, you would need to use `AsakasaTorchTask` as the base class. The number of processes is determined by the number of CUDA devices provided.

With akasaka installed, to run the examples, try following commands:

```bash
cd examples
# print.py
akasaka print.PrintTaskTest --test test_string
# directory_example/print.py
akasaka directory_example.print.PrintTaskTest --test test_string
```

## Development

To install from source, clone the repository and run

```bash
pip install -e .
```

## Known Issues

For torch (CUDA) task, you might need to wait for unexpected long time after model loaded before the task can start. Reason to be figured out.
