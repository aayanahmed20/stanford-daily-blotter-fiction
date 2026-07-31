# Stanford Daily Blotter Fiction

A short story of crime at Stanford, written from the police blotter dataset curated by The Stanford Daily.

## Overview

[The Stanford Daily](https://stanforddaily.com) publishes a weekly police blotter summarizing incidents reported to the Stanford University Department of Public Safety (SUDPS). `stanforddams/daily` on Hugging Face collects 139 of these blotter articles, published between September 2021 and June 2026, along with structured metadata and a taxonomy of the crime categories and tags used across the collection.

This repository contains an original short story, "Lot 95," inspired by that dataset. The story uses real Stanford campus geography and the format of the blotter itself as texture, but the characters, dialogue, and central case are invented. It is fiction, not reporting.

## Data Source

- Dataset: [stanforddams/daily](https://huggingface.co/datasets/stanforddams/daily)
- Source publication: [The Stanford Daily](https://stanforddaily.com)
- License: content is copyright The Stanford Daily; dataset metadata is released under MIT

## Repository Contents

| File | Description |
|---|---|
| `STORY.md` | The short story, "Lot 95" |
| `notes/dataset-notes.md` | Notes on the dataset structure and the details drawn from it while writing |
| `scripts/load_dataset.py` | Reference script for loading and exploring the dataset |
| `LICENSE` | License for the original written content in this repository |

## Method

The story does not summarize or quote any individual blotter article. It draws on:

- The dataset's five-year time span and weekly cadence
- The `categories` and `tags` taxonomy structure described in `taxonomy.json`, which resolves numeric codes to labels like "bike theft" and "vehicle burglary"
- Real, publicly known Stanford locations that recur across the blotter (residential lots, athletic facilities, academic buildings) used only as setting

Further detail is in `notes/dataset-notes.md`.

## Reproducing the Dataset Exploration

```python
from datasets import load_dataset
from bs4 import BeautifulSoup

ds = load_dataset("stanforddams/daily", "html")

def collect(example):
    soup = BeautifulSoup(example["html"], "html.parser")
    example["text"] = soup.get_text(" ", strip=True)
    example["title"] = soup.title.string if soup.title else None
    return example

ds = ds.map(collect)
ds["train"][0]["text"]
```

## Disclaimer

"Lot 95" is a work of fiction. No character, event, arrest, or investigation in the story corresponds to an actual incident, person, or case. Any resemblance to real individuals is coincidental.

## License

The written content in this repository (`STORY.md`, notes) is original work released under the license in `LICENSE`. It is independent of the source dataset's own license and does not reproduce any of the dataset's underlying article text.

## Contributors

- [aayanahmed20](https://github.com/aayanahmed20)
- Timothy Pshenicnhy
