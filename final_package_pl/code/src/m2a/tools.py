from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .schemas import ToolObservation

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS_PATH = REPO_ROOT / "data" / "corpus" / "papers.jsonl"


@dataclass(frozen=True, slots=True)
class ToolContract:
    name: str
    preconditions: list[str]
    outputs: list[str]
    side_effects: list[str]


@dataclass(frozen=True, slots=True)
class PaperCard:
    citation_id: str
    title: str
    year: int
    abstract: str
    keywords: list[str]
    topic_tags: list[str]
    findings: list[str]
    limitations: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PaperCard":
        return cls(**data)

    def summary(self) -> dict[str, Any]:
        return {
            "citation_id": self.citation_id,
            "title": self.title,
            "year": self.year,
            "topic_tags": list(self.topic_tags),
        }


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


class ToolBox:
    def __init__(self, note_dir: str | Path, corpus_path: str | Path = DEFAULT_CORPUS_PATH) -> None:
        self.note_dir = Path(note_dir)
        self.note_dir.mkdir(parents=True, exist_ok=True)
        self.papers = self._load_corpus(corpus_path)
        self.contracts = {
            "search_corpus": ToolContract(
                name="search_corpus",
                preconditions=["query must be non-empty", "search is lexical over title, abstract, and keywords"],
                outputs=["ranked result summaries", "matched terms", "scores"],
                side_effects=["none"],
            ),
            "read_paper": ToolContract(
                name="read_paper",
                preconditions=["citation_id must exist in the local corpus"],
                outputs=["full local paper card"],
                side_effects=["none"],
            ),
            "write_note": ToolContract(
                name="write_note",
                preconditions=["title and body must be non-empty", "source_refs must be local citation IDs"],
                outputs=["path to markdown note"],
                side_effects=["creates a markdown note under the run's notes directory"],
            ),
            "assemble_citations": ToolContract(
                name="assemble_citations",
                preconditions=["citation_ids must exist in the local corpus"],
                outputs=["formatted local citations"],
                side_effects=["none"],
            ),
        }

    def _load_corpus(self, path: str | Path) -> dict[str, PaperCard]:
        papers: dict[str, PaperCard] = {}
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                paper = PaperCard.from_dict(json.loads(line))
                papers[paper.citation_id] = paper
        return papers

    def search_corpus(self, query: str, limit: int, step: int) -> ToolObservation:
        if not query.strip():
            raise ValueError("search_corpus requires a non-empty query")
        query_tokens = _tokenize(query)
        ranked: list[dict[str, Any]] = []
        for paper in self.papers.values():
            title_text = " ".join(_tokenize(paper.title))
            abstract_text = " ".join(_tokenize(paper.abstract))
            keyword_text = " ".join(_tokenize(" ".join(paper.keywords)))
            score = 0
            matched_terms: list[str] = []
            for token in query_tokens:
                if token in title_text:
                    score += 4
                    matched_terms.append(token)
                elif token in keyword_text:
                    score += 3
                    matched_terms.append(token)
                elif token in abstract_text:
                    score += 1
                    matched_terms.append(token)
            if score == 0:
                continue
            ranked.append(
                {
                    "citation_id": paper.citation_id,
                    "title": paper.title,
                    "year": paper.year,
                    "score": score,
                    "matched_terms": sorted(set(matched_terms)),
                    "topic_tags": list(paper.topic_tags),
                }
            )
        ranked.sort(key=lambda item: (-item["score"], item["citation_id"]))
        results = ranked[:limit]
        return ToolObservation(
            step=step,
            tool_name="search_corpus",
            success=True,
            input={"query": query, "limit": limit},
            output={"results": results},
            summary=f"Search returned {len(results)} result(s).",
            source_refs=[item["citation_id"] for item in results],
            side_effects=[],
        )

    def read_paper(self, citation_id: str, step: int) -> ToolObservation:
        if citation_id not in self.papers:
            raise ValueError(f"Unknown citation_id: {citation_id}")
        paper = self.papers[citation_id]
        return ToolObservation(
            step=step,
            tool_name="read_paper",
            success=True,
            input={"citation_id": citation_id},
            output=asdict(paper),
            summary=f"Read {citation_id}.",
            source_refs=[citation_id],
            side_effects=[],
        )

    def write_note(self, title: str, body: str, source_refs: list[str], step: int) -> ToolObservation:
        if not title.strip() or not body.strip():
            raise ValueError("write_note requires a non-empty title and body")
        if not source_refs:
            raise ValueError("write_note requires at least one source_ref")
        unknown = [ref for ref in source_refs if ref not in self.papers]
        if unknown:
            raise ValueError(f"write_note received unknown citation IDs: {unknown}")
        filename = f"{step:02d}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:50]}.md"
        note_path = self.note_dir / filename
        note_path.write_text(
            f"# {title}\n\n{body}\n\n## Sources\n" + "\n".join(f"- {ref}" for ref in source_refs) + "\n",
            encoding="utf-8",
        )
        return ToolObservation(
            step=step,
            tool_name="write_note",
            success=True,
            input={"title": title, "source_refs": source_refs},
            output={"note_path": str(note_path)},
            summary=f"Wrote note {note_path.name}.",
            source_refs=list(source_refs),
            side_effects=[f"created:{note_path.name}"],
        )

    def assemble_citations(self, citation_ids: list[str], step: int) -> ToolObservation:
        missing = [citation_id for citation_id in citation_ids if citation_id not in self.papers]
        if missing:
            raise ValueError(f"assemble_citations received unknown citation IDs: {missing}")
        citations = [f"[{paper.citation_id}] {paper.title} ({paper.year})" for paper in (self.papers[cid] for cid in citation_ids)]
        return ToolObservation(
            step=step,
            tool_name="assemble_citations",
            success=True,
            input={"citation_ids": citation_ids},
            output={"citations": citations},
            summary=f"Assembled {len(citations)} citation(s).",
            source_refs=list(citation_ids),
            side_effects=[],
        )
