# Jupyter to PDF (WebPDF)

Convert Jupyter Notebooks (`.ipynb`) to PDF **without LaTeX or Pandoc** using the WebPDF exporter from `nbconvert`.

---

## Quick Start

### 1. Install Python and dependencies
Make sure Python **3.10+** is installed, then run:

```bash
pip install jupyter nbconvert[webpdf] nbformat traitlets
```

---

### 2. (First time only) Download Chromium
The WebPDF exporter uses a headless browser.  
Run this once to allow nbconvert to download Chromium automatically:

```bash
python -m jupyter nbconvert --to webpdf your_notebook.ipynb --allow-chromium-download
```

---

### 3. Convert your notebook
After that, use the script in this repository:

```bash
python convert_notebook.py notebook.ipynb
```

Or, if you want to execute the notebook before exporting:

```bash
python convert_notebook.py notebook.ipynb --execute
```

A PDF file will be created in the same folder, for example:

```
notebook.pdf
```

---

## Features

- No LaTeX or Pandoc required  
- Cross-platform (Windows, macOS, Linux)  
- Fast, clean, and reliable conversion
- Works fully offline after first Chromium download

---

## Requirements

- Python ≥ 3.10  
- `jupyter`, `nbconvert[webpdf]`, `nbformat`, `traitlets`
