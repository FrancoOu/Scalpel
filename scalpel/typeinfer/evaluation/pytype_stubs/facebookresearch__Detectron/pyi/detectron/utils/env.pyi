# (generated with --quick)

import __future__
from typing import Any, IO, NoReturn, Optional, Union, overload

_CMAKE_INSTALL_PREFIX: str
_DETECTRON_OPS_LIB: str
absolute_import: __future__._Feature
division: __future__._Feature
os: module
print_function: __future__._Feature
sys: module
unicode_literals: __future__._Feature
yaml: module

def exit_on_error() -> NoReturn: ...
def get_custom_ops_lib() -> str: ...
def get_detectron_ops_lib() -> str: ...
def get_py_bin_ext() -> str: ...
def get_runtime_dir() -> str: ...
def import_nccl_ops() -> None: ...
def set_up_matplotlib() -> None: ...
@overload
def yaml_dump(data, stream: None = ..., Dumper = ..., *, default_style = ..., default_flow_style = ..., canonical = ..., indent = ..., width = ..., allow_unicode = ..., line_break = ..., encoding: Optional[str] = ..., explicit_start = ..., explicit_end = ..., version = ..., tags = ..., sort_keys: bool = ...) -> Any: ...
@overload
def yaml_dump(data, stream: IO[str], Dumper = ..., *, default_style = ..., default_flow_style = ..., canonical = ..., indent = ..., width = ..., allow_unicode = ..., line_break = ..., encoding = ..., explicit_start = ..., explicit_end = ..., version = ..., tags = ..., sort_keys: bool = ...) -> None: ...
def yaml_load(stream: Union[bytes, str, IO[Union[bytes, str]]], Loader = ...) -> Any: ...