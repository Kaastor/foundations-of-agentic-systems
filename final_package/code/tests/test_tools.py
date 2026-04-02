from pathlib import Path

import pytest

from m2a.tools import ToolBox


def test_tool_contracts_have_preconditions_and_side_effects(tmp_path) -> None:
    toolbox = ToolBox(tmp_path / "notes")
    assert toolbox.contracts["search_corpus"].preconditions
    assert toolbox.contracts["write_note"].side_effects


def test_search_read_write_note_and_citation_assembly(tmp_path) -> None:
    toolbox = ToolBox(tmp_path / "notes")
    search = toolbox.search_corpus("planning memory", 3, step=1)
    assert search.output["results"]
    citation_id = search.output["results"][0]["citation_id"]
    read = toolbox.read_paper(citation_id, step=2)
    assert read.output["citation_id"] == citation_id
    note = toolbox.write_note("test note", "evidence", [citation_id], step=3)
    assert Path(note.output["note_path"]).exists()
    citations = toolbox.assemble_citations([citation_id], step=4)
    assert citations.output["citations"]


def test_search_requires_non_empty_query(tmp_path) -> None:
    toolbox = ToolBox(tmp_path / "notes")
    with pytest.raises(ValueError):
        toolbox.search_corpus("", 3, step=1)
