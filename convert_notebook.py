import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import logging
from pathlib import Path
from nbconvert import WebPDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
from traitlets.config import Config
from nbformat import read, NO_CONVERT

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class NotebookToPdfConverter:
    def __init__(self, timeout=600, kernel_name="python3"):
        self.timeout = timeout
        self.kernel_name = kernel_name

    def convert(self, input_path, output_path=None, execute=False):
        input_path = Path(input_path)
        output_path = Path(output_path) if output_path else input_path.with_suffix(".pdf")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with input_path.open("r", encoding="utf-8") as f:
            nb_node = read(f, as_version=NO_CONVERT)
        resources = {"metadata": {"path": str(input_path.parent)}}
        if execute:
            ExecutePreprocessor(timeout=self.timeout, kernel_name=self.kernel_name).preprocess(nb_node, resources)
        exporter = WebPDFExporter(config=Config())
        body, _ = exporter.from_notebook_node(nb_node, resources)
        with open(output_path, "wb") as f:
            f.write(body)
        logging.info("✅ PDF created: %s", output_path)
        return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Jupyter notebook to PDF via WebPDFExporter (no Pandoc or LaTeX).")
    parser.add_argument("src", help="Path to notebook (.ipynb)")
    parser.add_argument("-o", "--out", help="Output PDF path")
    parser.add_argument("--execute", action="store_true", help="Execute notebook before conversion")
    args = parser.parse_args()
    NotebookToPdfConverter().convert(args.src, output_path=args.out, execute=args.execute)
