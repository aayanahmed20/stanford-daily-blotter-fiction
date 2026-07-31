# Dataset Notes

Notes on `stanforddams/daily`, taken while preparing "Lot 95."

## Structure

The dataset ships three files:

- `index.json` — one record per article, with `id`, `title`, `author`, `url`, `date`, `categories`, and `tags`
- `train.jsonl` — the raw HTML body for each article, keyed by `id`
- `taxonomy.json` — a lookup table resolving the numeric `categories` and `tags` IDs into readable labels (for example, category 4409 is "Crime & Safety," and tags include labels like "bike theft" and "hate violence")

Each article is a weekly SUDPS bulletin summary, organized by day, listing incident type, a time window, and a campus location. Articles span September 2021 through June 2026, roughly one per week during the academic year.

## What informed the story

- **Cadence and format.** The blotter's weekly, day-by-day structure — a fixed vocabulary of incident types (petty theft, burglary from a motor vehicle, vandalism, grand theft) paired with a building or lot name — shaped both the setting and the narrator's job in the story.
- **Recurring locations.** Certain locations recur across multiple articles in the dataset: residential lots, Escondido Village, Wilbur Hall, athletic facilities near Cobb Track and Angell Field, and parking areas tied to specific dorms or departments. These are real, publicly known Stanford locations used only as backdrop.
- **The taxonomy layer.** The separation between the human-readable blotter text and the underlying `categories`/`tags` codes suggested the story's central device: a narrator who notices a pattern in the metadata that the prose itself doesn't surface.
- **No article content was reproduced.** No incident, date, or location from a specific real article was copied into the story. "Lot 95," the case, the coaches, and the investigation are invented.

## Reproducing the exploration

See `scripts/load_dataset.py` for a runnable version of the loading snippet from the dataset card.
