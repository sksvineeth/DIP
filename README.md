# DIP

Diplomatic Intelligence Platform (DIP) is a demonstration of an agentic
architecture that brings together multiple data modalities in order to aid
strategic decision making. The project shows how satellite imagery, media
monitoring, voice communication transcripts and economic indicators could be
processed in a unified workflow.

## Structure

The core logic lives in the `dip` package:

- `data_sources.py` – placeholder classes for different data streams.
- `processing.py` – simple analyzers that mimic AI model processing.
- `agents.py` – agent classes that perform collection, analysis and synthesis.
- `pipeline.py` – wires the agents together into an end‑to‑end pipeline.

`main.py` provides a small runnable example using dummy components.

## Running

The example requires Python 3.12+. With a local Python environment
active, run:

```bash
python main.py
```

This will execute the demo pipeline and print a synthesized report from
the placeholder data sources.
