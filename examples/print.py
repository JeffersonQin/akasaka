import akasaka
import argparse


class PrintTaskTest(akasaka.AkasakaTask):
    def __init__(self, args):
        parser = argparse.ArgumentParser(description='Print task test')
        parser.add_argument('--test', type=str, help='Test argument, to be printed')
        args = parser.parse_args(args)
        self.test = args.test

    def generate_tasks(self):
        for i in range(10000):
            yield {"i": i}

    def is_executed(self, i):
        return False

    def __call__(self, i):
        print(f"{self.test}: Task {i} is executed.")
