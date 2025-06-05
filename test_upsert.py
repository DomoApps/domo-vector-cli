import pytest
from upsert import (
    chunk_text_with_overlap,
    read_file_contents,
    iterate_documents_breadth_first,
)
import os
import tempfile


def test_chunk_text_with_overlap_basic():
    text = "A B C D E F G H I J"
    chunks = chunk_text_with_overlap(text, max_length=5, overlap=2)
    assert isinstance(chunks, list)
    assert all(isinstance(c, str) for c in chunks)
    assert len(chunks) > 0


def test_read_file_contents(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello world")
    content = read_file_contents(str(file_path))
    assert content == "hello world"


def test_iterate_documents_breadth_first(tmp_path):
    d1 = tmp_path / "dir1"
    d1.mkdir()
    f1 = d1 / "a.md"
    f1.write_text("foo")
    f2 = tmp_path / "b.md"
    f2.write_text("bar")
    files = list(iterate_documents_breadth_first(str(tmp_path)))
    assert str(f1) in files
    assert str(f2) in files
