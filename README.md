# Movie Recommender

A content-based movie recommendation system: pick a movie you like, and it
returns 5 titles with the closest plot/keyword similarity. There are two ways
to run it, included in this repo.

## Files

| File                        | What it is                                                        |
|------------------------------|--------------------------------------------------------------------|
| `app.py`                    | Streamlit app — the interactive Python version                    |
| `movie-recommender.ipynb`   | Notebook where the model was built (vectorizing tags, similarity) |
| `movies.pkl`                | Movie metadata (id, title, tags) used by the model                |
| `similarity.pkl`            | Precomputed cosine-similarity matrix between all movies            |
| `index.html`                | A standalone static version — no Python needed to run it          |

## Option 1: Run the Streamlit app

```bash
pip install streamlit pandas
streamlit run app.py
```

This reads `movies.pkl` and `similarity.pkl` at runtime and serves an
interactive UI in your browser.

## Option 2: Open the static page

`index.html` is completely self-contained — the movie list and every
precomputed recommendation are embedded directly in the file. Open it in
any browser, or host it for free with GitHub Pages:

1. Keep `index.html` anywhere in this repo (root is simplest).
2. Repo Settings → Pages → Source: **Deploy from a branch** → branch `main`,
   folder `/ (root)`.
3. Your live page appears at `https://<username>.github.io/<repo-name>/`.

**Note:** `index.html` does not read `app.py` or the `.pkl` files — its data
is baked in at build time. If `movies.pkl` or `similarity.pkl` are
regenerated later, `index.html` needs to be rebuilt separately to reflect
the new data.

## How it works

Movies are converted to a "tags" string per title (overview + genres +
cast + crew keywords). A bag-of-words vectorizer turns each tag string into
a vector, and cosine similarity between vectors gives a similarity score
between every pair of movies. For a selected movie, the 5 highest-scoring
other movies are returned as recommendations.
