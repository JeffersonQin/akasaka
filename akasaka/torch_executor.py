import torch
from tqdm import tqdm
import torch.multiprocessing as mp
from .loader import load_class


# these two variables only initialize
# after the `load` function is called
# i.e. in the new process
akasaka_task = None
device = None


def load(module_path, args, cuda_devices):
    # we need to reload the module in the new process
    # because pytorch only supports spawn, which will start with a fresh python interpreter
    loaded_class = load_class(module_path)
    task = loaded_class(args=args)
    # get the process number -> device index
    d_index = mp.current_process()._identity[0] - 1
    # load the model to the device of this process
    task.load_model(cuda_devices[d_index])
    print(f"Process {d_index} finished loading model.")

    # make it global of this process
    global akasaka_task
    akasaka_task = task
    global device
    device = cuda_devices[d_index]
    print(f"Process {d_index} finished globaling.")


def execute(batch):
    # access the global task and device (pre-process)
    global akasaka_task
    global device

    if akasaka_task.is_executed(batch):
        return

    akasaka_task(device=device, batch=batch)


def akasaka_torch_execute(task, module_path, args, devices):
    if not torch.cuda.is_available():
        raise ValueError("CUDA is not available.")

    # create torch devices from the device indices
    cuda_devices = []
    for device in devices:
        cuda_devices.append(torch.device(f"cuda:{device}"))

    # WE ONLY USE TASK TO GET DATALOADER -> distribute the data to each process later
    dataloader = task.get_dataloader()

    # WE WILL RELOAD TASK MODULE IN EACH PROCESS
    mp.set_start_method('spawn')
    pool = mp.get_context('spawn').Pool(processes=len(devices), initializer=load, initargs=(module_path, args, cuda_devices))
    _ = list(tqdm(pool.imap_unordered(execute, dataloader), total=len(dataloader)))

    pool.close()
    pool.join()
