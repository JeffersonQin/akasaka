import torch
from tqdm import tqdm


def akasaka_torch_single_execute(task, device):
    if not torch.cuda.is_available():
        raise ValueError("CUDA is not available.")

    task.load_model(device)
    dataloader = task.get_dataloader()

    for batch in tqdm(dataloader):
        task(device=device, batch=batch)
