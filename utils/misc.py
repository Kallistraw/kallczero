import os
import importlib

def add_handlers(application):
    modules_path = "modules"
    for filename in os.listdir(modules_path):
        if filename.endswith(".py"):
            module_name = f"{modules_path}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            if hasattr(module, "register"):
                module.register(application)
