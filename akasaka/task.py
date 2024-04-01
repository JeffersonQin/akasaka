class AkasakaTask():
    def __init__(self, args) -> None:
        """
        Initialize the task with command line arguments
        args can be passed to ArgumentParser.parse_args() to parse remaining command line arguments.
        """
        pass

    def generate_tasks(self, **kwargs) -> list:
        """Generate a list of tasks to be executed."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def is_executed(self, **kwargs) -> bool:
        """Check if the task has already been executed."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def __call__(self, **kwargs) -> None:
        """Run the task."""
        raise NotImplementedError("This method should be implemented in a subclass.")
