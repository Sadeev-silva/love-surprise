# 💌 Love Surprise — QR Love Meter Experience

An interactive "open when alone" surprise you send as a QR code. Scanning it opens a five-screen experience:

1. **Love meter** — a slider asks "How much do you love me?". A cute cat reacts as the value changes (crying → unimpressed → delighted). Only sliding to the very end unlocks **1000% — Correct answer!** and the Next button.
2. **You passed the love test** — two gift boxes; tapping one opens it.
3. **Your Bouquet** — a rose bouquet surrounded by six love notes that fade in.
4. **Music** — a scrapbook collage (tickets, blossoms, butterfly, polaroid) with a music-player card. Add your own `music.mp3` to make the play button produce sound.
5. **A Letter From My Heart** — a typewriter-animated letter ending "Always, forever. ❤" with a replay option.

Everything is one self-contained `index.html` (no build step, no dependencies). All artwork is original inline SVG, so it stays crisp at any size.

---

## Customise it (2 minutes)

Open `index.html` and edit the `CONFIG` object near the bottom:

- `question`, `reactions` — the meter texts
- `bouquetNotes` — the six speech-bubble messages
- `song.title` / `song.artist` — the label shown on the player
- `letterParagraphs`, `signOff` — the letter itself

**Music:** drop a file named `music.mp3` into the project folder (use audio you own or are licensed to use — none is included). On GitHub Pages it plays directly; on Streamlit it is embedded automatically by `streamlit_app.py`.

---

## Option A — Deploy on Streamlit Community Cloud (free)

Step 1 — create a new GitHub repository and push this folder:

```
git init
```

```
git add .
```

```
git commit -m "Love surprise app"
```

```
git branch -M main
```

```
git remote add origin https://github.com/YOUR-USERNAME/love-surprise.git
```

```
git push -u origin main
```

Step 2 — go to https://share.streamlit.io, sign in with GitHub, click **Create app**, pick the repository, and set **Main file path** to `streamlit_app.py`.

Step 3 — copy the URL Streamlit gives you (e.g. `https://your-app.streamlit.app`).

Note: free Streamlit apps sleep after inactivity; the first scan may take ~30 seconds to wake the app.

## Option B — Deploy on GitHub Pages (free, no sleeping, recommended)

Because the whole experience is a single `index.html`, GitHub Pages hosts it perfectly with no wake-up delay:

Step 1 — push the folder to GitHub (same commands as above).

Step 2 — in the repository, open **Settings → Pages**, set **Source** to `Deploy from a branch`, choose `main` and `/ (root)`, then save.

Step 3 — after ~1 minute your app is live at `https://YOUR-USERNAME.github.io/love-surprise/`.

---

## Generate the heart QR code

Step 1 — install the dependency:

```
pip install "qrcode[pil]"
```

Step 2 — generate the code with your live URL:

```
python make_qr.py https://YOUR-USERNAME.github.io/love-surprise/
```

This saves `love_qr.png` — a pink-to-crimson QR with a heart in the centre (high error correction keeps it scannable). Send it on WhatsApp with a caption like **"Open when alone 💌"**.

---

## Project structure

```
love-surprise/
├── index.html        # the entire experience (edit CONFIG here)
├── streamlit_app.py  # Streamlit wrapper for Option A
├── make_qr.py        # heart QR generator
├── requirements.txt  # streamlit + qrcode
└── music.mp3         # (optional) add your own audio — not included
```
