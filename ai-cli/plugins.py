import importlib
import pkg_resources
from .models import register_models

def load_plugins():
    for entry_point in pkg_resources.iter_entry_points(group='ai-cli.models'):
        try:
            mod = importlib.import_module(entry_point.module_name)
            register_func = getattr(mod, entry_point.attrs[0], None)
            if register_func:
                register_models(register_func)
        except Exception as e:
            click.echo(f"Plugin load error {entry_point}: {e}", err=True)