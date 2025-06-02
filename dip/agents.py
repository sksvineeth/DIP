"""Agentic workflow components for the Diplomatic Intelligence Platform."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Any, List

from .data_sources import DataSource
from .processing import Analyzer, aggregate


@dataclass
class Agent:
    """Base class for an agent in the workflow."""

    def run(self) -> Iterable[Any]:
        raise NotImplementedError


@dataclass
class CollectionAgent(Agent):
    """Agent responsible for gathering data."""

    sources: List[DataSource]

    def run(self) -> Iterable[Any]:
        for source in self.sources:
            yield from source.fetch()


@dataclass
class AnalysisAgent(Agent):
    """Agent responsible for analyzing collected data."""

    analyzer: Analyzer
    inbox: Iterable[Any]

    def run(self) -> Iterable[Any]:
        for item in self.inbox:
            yield self.analyzer.process(item)


@dataclass
class SynthesisAgent(Agent):
    """Agent responsible for synthesizing analysis results."""

    inbox: Iterable[Any]

    def run(self) -> Any:
        return aggregate(self.inbox)
