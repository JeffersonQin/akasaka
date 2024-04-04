class AkasakaTorchTask():
    def __init__(self, args) -> None:
        """
        Initialize the task with command line arguments
        args can be passed to ArgumentParser.parse_args() to parse remaining command line arguments.
        """
        pass

    def load_model(self, device) -> None:
        """Load the model on a device."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def get_dataloader(self):
        """Return a DataLoader object."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def is_executed(self, batch) -> bool:
        """Check if the task has already been executed."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def __call__(self, device, batch) -> None:
        """Run the task. Also provide the device to run the task on."""
        raise NotImplementedError("This method should be implemented in a subclass.")
