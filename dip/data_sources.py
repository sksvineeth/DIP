"""Data source definitions for the Diplomatic Intelligence Platform."""

from dataclasses import dataclass
from typing import Iterable, Any


@dataclass
class SatelliteImagery:
    """Placeholder for satellite imagery data."""
    image_path: str


@dataclass
class MediaArticle:
    """Represents a piece of media content."""
    language: str
    text: str


@dataclass
class VoiceCommunication:
    """Represents captured voice communication metadata."""
    transcript: str
    speaker: str


@dataclass
class EconomicIndicator:
    """Represents economic data points."""
    name: str
    value: float


class DataSource:
    """Abstract interface for data sources."""

    def fetch(self) -> Iterable[Any]:
        """Fetch new data items from the source."""
        raise NotImplementedError


class DummyDataSource(DataSource):
    """Example implementation that yields placeholder data."""

    def fetch(self) -> Iterable[Any]:
        # In a real system this would connect to external APIs or data feeds
        yield SatelliteImagery(image_path="/path/to/image.png")
        yield MediaArticle(language="en", text="Example news article")
        yield VoiceCommunication(transcript="Hello world", speaker="Analyst")
        yield EconomicIndicator(name="GDP", value=1.0)
