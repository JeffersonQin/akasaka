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

Write a task class of the subclass of `AsakasaTask` and implement needed methods. Take a look at the examples in the [`examples` directory](./examples).

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
