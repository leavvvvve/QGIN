"""Load only pinned, locally supplied official source trees."""
import importlib.util
import os
from pathlib import Path
SOURCE=Path(os.environ.get('QGIN_OFFICIAL_ROOT','external'))
def official(method,file):
    path=SOURCE/method/file
    spec=importlib.util.spec_from_file_location('qgin_official_'+method+'_'+file.replace('/','_').replace('.','_'),path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
