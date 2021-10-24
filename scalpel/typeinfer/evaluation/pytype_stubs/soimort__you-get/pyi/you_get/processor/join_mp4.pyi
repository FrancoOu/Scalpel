# (generated with --quick)

import io
from typing import Any, Callable, Dict, List, NoReturn, Tuple, Type

BytesIO: Type[io.BytesIO]
atom_readers: Dict[bytes, Callable[[Any, Any, Any, Any], Any]]
struct: module

class Atom:
    body: Any
    size: Any
    type: Any
    def __init__(self, type, size, body) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def calsize(self) -> Any: ...
    def write(self, stream) -> None: ...
    def write1(self, stream) -> None: ...

class CompositeAtom(Atom):
    body: Any
    size: Any
    type: Any
    def __init__(self, type, size, body) -> None: ...
    def calsize(self) -> Any: ...
    def get(self, *keys) -> Any: ...
    def get1(self, k) -> Any: ...
    def get_all(self, k) -> list: ...
    def write(self, stream) -> None: ...

class VariableAtom(Atom):
    body: Any
    size: Any
    type: Any
    variables: Any
    def __init__(self, type, size, body, variables) -> None: ...
    def get(self, k) -> Any: ...
    def set(self, k, v) -> None: ...
    def write(self, stream) -> None: ...

def concat_mp4(mp4s, output = ...) -> Any: ...
def copy_stream(source, target, n) -> None: ...
def guess_output(inputs) -> Any: ...
def main() -> None: ...
def merge_mdats(mdats) -> Any: ...
def merge_moov(moovs, mdats) -> Any: ...
def merge_mp4s(files, output) -> None: ...
def merge_stco(offsets_list, mdats) -> list: ...
def merge_stsc(chunks_list, total_chunk_number_list) -> List[Tuple[int, Any, Any]]: ...
def merge_stss(samples, sample_number_list) -> list: ...
def merge_stsz(sizes_list) -> Any: ...
def merge_stts(samples_list) -> list: ...
def parse_atoms(stream) -> list: ...
def read_atom(stream) -> Any: ...
def read_avc1(stream, size, left, type) -> Atom: ...
def read_avcC(stream, size, left, type) -> Atom: ...
def read_body_stream(stream, left) -> Tuple[Any, io.BytesIO]: ...
def read_byte(stream) -> int: ...
def read_composite_atom(stream, size, left, type) -> CompositeAtom: ...
def read_ctts(stream, size, left, type) -> Any: ...
def read_descriptor(stream) -> NoReturn: ...
def read_esds(stream, size, left, type) -> Atom: ...
def read_full_atom(stream) -> Any: ...
def read_full_atom2(stream) -> Tuple[Any, Any]: ...
def read_hdlr(stream, size, left, type) -> Atom: ...
def read_int(stream) -> Any: ...
def read_mdat(stream, size, left, type) -> Any: ...
def read_mdhd(stream, size, left, type) -> VariableAtom: ...
def read_mp4(stream) -> Tuple[list, Any, Any]: ...
def read_mp4a(stream, size, left, type) -> Atom: ...
def read_mvhd(stream, size, left, type) -> VariableAtom: ...
def read_raw(stream, size, left, type) -> Atom: ...
def read_smhd(stream, size, left, type) -> Atom: ...
def read_stco(stream, size, left, type) -> Any: ...
def read_stsc(stream, size, left, type) -> Any: ...
def read_stsd(stream, size, left, type) -> Any: ...
def read_stss(stream, size, left, type) -> Any: ...
def read_stsz(stream, size, left, type) -> Any: ...
def read_stts(stream, size, left, type) -> Any: ...
def read_tkhd(stream, size, left, type) -> VariableAtom: ...
def read_udta(stream, size, left, type) -> Any: ...
def read_uint(stream) -> Any: ...
def read_ulong(stream) -> Any: ...
def read_ushort(stream) -> Any: ...
def read_vmhd(stream, size, left, type) -> Atom: ...
def skip(stream, n) -> None: ...
def skip_zeros(stream, n) -> None: ...
def usage() -> None: ...
def write_atom(stream, atom) -> None: ...
def write_uint(stream, n) -> None: ...
def write_ulong(stream, n) -> None: ...