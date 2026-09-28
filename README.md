# Image to PDF Converter

A simple Python script that converts one or more images into a multi-page PDF file using the Pillow (PIL) library.

## Features

- Convert multiple images into a single PDF
- Supports common image formats (PNG, JPEG, etc.)
- Automatically converts images to RGB mode for PDF compatibility
- Skips missing or invalid images with warnings
- Easy to use function-based API

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) (`pip install Pillow`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ankushminhas80366-tech/Image_to_PDF_Converter.git
   cd Image_to_PDF_Converter
   ```

2. Install the required dependency:
   ```bash
   pip install Pillow
   ```

## Usage

### Basic Example

```python
from Main import image_to_pdf

# List of image paths
my_images = [
    'image1.png',
    'image2.jpg',
    'image3.png'
]

# Output PDF name
pdf_name = "output.pdf"

# Convert images to PDF
image_to_pdf(my_images, pdf_name)
```

### Running the Script Directly

Edit the `__main__` section in `Main.py` to specify your image paths and desired PDF name, then run:

```bash
python Main.py
```

## Function Reference

### `image_to_pdf(image_list, output_pdf_name)`

Converts a list of images into a PDF file.

**Parameters:**
- `image_list` (list of str): Paths to the image files to include in the PDF.
- `output_pdf_name` (str): Name/path of the output PDF file.

**Behavior:**
- Skips any images that cannot be opened or do not exist.
- Prints progress messages and a success message when done.
- Does nothing if no valid images are found.

## Notes

- Images are converted to RGB mode before saving to ensure PDF compatibility.
- The first valid image becomes the base page; subsequent images are appended as additional pages.
- Make sure the image files exist in the working directory (or provide full paths).

## License

This project is open source and available for personal and educational use.
