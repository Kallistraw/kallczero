import os
import importlib

def add_handlers(application):
    # Dynamically import all handler modules in the 'modules' directory
    modules_path = "modules"
    for filename in os.listdir(modules_path):
        if filename.endswith("_handler.py"):
            module_name = f"{modules_path}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            # Assume each handler module defines a 'register' function
            if hasattr(module, "register"):
                module.register(application)
