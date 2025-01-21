# Brain MRI Segmentation and Report Generation

This project involves the visualization of segmented brain MRI images and the generation of a PDF report containing both the visualizations and relevant patient information extracted from a CSV file.

## Features

- **Segmentation Visualization**: Visualizes the segmented brain regions from NIfTI files.
- **PDF Report Generation**: Generates a PDF report with patient details and volume information of various brain regions.
- **Customizable Views**: Provides axial, sagittal, and coronal views with different background options.

## Project Structure

- `load_mri.py`: 
  - Contains functions to visualize NIfTI files and generate a PDF report with colorful segmentation images.
  - Functions include:
    - `visualize_segmented_nifti(nifti_file)`: Visualizes the NIfTI file and saves segmented brain images.
    - `generate_pdf_report(csv_data, output_pdf, image_path)`: Generates a PDF report based on CSV data and segmentation images.
  - Main entry point: `main(nifti_file, csv_file_path, output_pdf)`

- `test.py`: 
  - Similar to `load_mri.py` but includes visualization with a black background for segmented images.
  - Functions include:
    - `visualize_segmented_nifti_black_bg(nifti_file)`: Visualizes segmented brain with a black background.
    - `generate_pdf_report(csv_data, output_pdf, image_path)`: Generates a PDF report with the black background segmented image.
  - Main entry point: `main(nifti_file, csv_file_path, output_pdf)`

## Dependencies

- Python libraries:
  - `nibabel`
  - `matplotlib`
  - `numpy`
  - `pandas`
  - `reportlab`

Install dependencies using:
```bash
pip install nibabel matplotlib numpy pandas reportlab
