import multiprocessing
from tqdm import tqdm


akasaka_task = None


def execute(args):
    global akasaka_task

    if akasaka_task.is_executed(**args):
        return
    akasaka_task(**args)


def akasaka_execute(task, num_process, chunksize):
    global akasaka_task
    akasaka_task = task
    # Generate a list of tasks to be executed
    tasks = akasaka_task.generate_tasks()
    tasks = list(tasks)
    print(f"Generated {len(tasks)} tasks to be executed.")

    pool = multiprocessing.Pool(processes=num_process)
    _ = list(tqdm(pool.imap_unordered(execute, tasks, chunksize=chunksize), total=len(tasks)))

    pool.close()
    pool.join()
