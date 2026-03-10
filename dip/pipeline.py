"""Orchestration pipeline for the Diplomatic Intelligence Platform."""

from typing import Any, Iterable

from .agents import CollectionAgent, AnalysisAgent, SynthesisAgent
from .data_sources import DummyDataSource
from .processing import DummyAnalyzer


class Pipeline:
    """High-level pipeline that wires agents together."""

    def __init__(self) -> None:
        self.collection_agent = CollectionAgent(sources=[DummyDataSource()])
        self.analysis_agent: AnalysisAgent | None = None
        self.synthesis_agent: SynthesisAgent | None = None

    def build(self) -> None:
        collected = list(self.collection_agent.run())
        self.analysis_agent = AnalysisAgent(analyzer=DummyAnalyzer(), inbox=collected)
        analysis_results = list(self.analysis_agent.run())
        self.synthesis_agent = SynthesisAgent(inbox=analysis_results)

    def run(self) -> Iterable[Any]:
        if self.synthesis_agent is None:
            self.build()
        yield self.synthesis_agent.run()
