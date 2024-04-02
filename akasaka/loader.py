import importlib.util


def load_class(module_path):
    try:
        module_name, class_name = module_path.rsplit('.', 1)
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ImportError(f"Module '{module_name}' not found.")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not hasattr(module, class_name):
            raise AttributeError(f"Class '{class_name}' not found in module '{module_name}'.")
        return getattr(module, class_name)
    except ValueError:
        raise ValueError("Invalid module path. It should be in the format 'module.submodule.ClassName'.")
