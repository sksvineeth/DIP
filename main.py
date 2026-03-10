"""Entry point for the Diplomatic Intelligence Platform demo."""

from dip.pipeline import Pipeline


def main() -> None:
    pipeline = Pipeline()
    for report in pipeline.run():
        print(report)


if __name__ == "__main__":
    main()
