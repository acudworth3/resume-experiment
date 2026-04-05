#!/usr/bin/env python3
"""
Publish script for CV variants.

Collects generated PDFs from output/generated/ and updates the publish/
directory structure with per-variant folders containing the PDF and an
index.html viewer. Updates the main publish/index.html with links to all variants.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def get_variant_name(pdf_filename: str) -> str:
    """Extract variant name from PDF filename (e.g., 'software-developer.pdf' -> 'software-developer')."""
    return Path(pdf_filename).stem


def title_case_variant(variant: str) -> str:
    """Convert variant name to title case (e.g., 'software-developer' -> 'Software Developer')."""
    return " ".join(word.capitalize() for word in variant.split("-"))


def generate_variant_html(variant: str, pdf_filename: str) -> str:
    """Generate index.html content for a variant folder."""
    return f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <title>View Document</title>
    <style>
        body,
        html {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }}

        iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
</head>

<body>
    <iframe src="./{pdf_filename}"></iframe>
</body>

</html>
"""


def generate_main_html(variants: list) -> str:
    """Generate the main publish/index.html with links to all variants."""
    nav_links = "\n".join(
        f'        <a class="cv-link" href="{variant}/">{title_case_variant(variant)}</a>'
        for variant in sorted(variants)
    )

    return f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Curriculum Vitae | Andrew Thomas Cudworth</title>
    <style>
        body {{
            font-family:
                -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
                Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 80px auto;
            padding: 0 20px;
            text-align: center;
        }}

        h1 {{
            margin-bottom: 10px;
        }}

        p {{
            color: #666;
            margin-bottom: 40px;
        }}

        .nav-container {{
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}

        .cv-link {{
            display: block;
            padding: 15px;
            background-color: #f4f4f9;
            color: #2c3e50;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #ddd;
            transition: all 0.2s ease;
            font-weight: 500;
        }}

        .cv-link:hover {{
            background-color: #e2e2e8;
            border-color: #bbb;
            transform: translateY(-2px);
        }}
    </style>
</head>

<body>
    <h1>Andrew Thomas Cudworth</h1>
    <p>Select a career track to view the associated CV.</p>

    <div class="nav-container">
{nav_links}
    </div>
</body>

</html>
"""


def main():
    """Main entry point."""
    # Determine paths
    repo_root = Path(__file__).parent.parent
    generated_dir = repo_root / "output" / "generated"
    publish_dir = repo_root / "publish"

    # Check if output/generated exists
    if not generated_dir.exists():
        print(f"Error: {generated_dir} does not exist. Generate PDFs first with 'make all'.")
        sys.exit(1)

    # Find all PDFs in output/generated
    pdf_files = list(generated_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {generated_dir}")
        sys.exit(1)

    print(f"Found {len(pdf_files)} PDF(s) in {generated_dir}")

    variants = []

    # Process each PDF
    for pdf_path in sorted(pdf_files):
        variant = get_variant_name(pdf_path.name)
        variants.append(variant)
        pdf_filename = pdf_path.name

        # Create variant folder in publish/
        variant_dir = publish_dir / variant
        variant_dir.mkdir(parents=True, exist_ok=True)

        # Copy PDF to variant folder
        dest_pdf = variant_dir / pdf_filename
        with open(pdf_path, "rb") as src:
            with open(dest_pdf, "wb") as dst:
                dst.write(src.read())
        print(f"✓ Copied {pdf_filename} to {variant_dir}/")

        # Generate and write variant index.html
        variant_html = generate_variant_html(variant, pdf_filename)
        variant_index = variant_dir / "index.html"
        variant_index.write_text(variant_html)
        print(f"✓ Generated {variant_index}")

    # Generate and write main publish/index.html
    main_html = generate_main_html(variants)
    main_index = publish_dir / "index.html"
    main_index.write_text(main_html)
    print(f"✓ Generated {main_index}")

    print(f"\n✓ Publish complete. {len(variants)} variant(s) published.")
    print(f"  Variants: {', '.join(sorted(variants))}")


if __name__ == "__main__":
    main()
