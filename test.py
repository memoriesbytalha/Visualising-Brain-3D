from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
import pandas as pd

# Function to visualize segmented brain with black background
def visualize_segmented_nifti_black_bg(nifti_file):
    img = nib.load(nifti_file)
    data = img.get_fdata()
    data = np.squeeze(data)

    # Create black background figure
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), facecolor='black')
    slices = [data[:, :, data.shape[2] // 2], data[data.shape[0] // 2, :, :], data[:, data.shape[1] // 2]]
    titles = ["Axial", "Sagittal", "Coronal"]

    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="Spectral", origin="lower")
        axes[i].set_title(titles[i], color='white')
        axes[i].axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    image_path = 'segmented_brain_black_bg.png'
    plt.savefig(image_path, facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()
    return image_path

# Function to generate PDF report
def generate_pdf_report(csv_data, output_pdf, image_path):
    # Create document
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Set up styles
    styles = getSampleStyleSheet()
    content = []

    # Patient info
    patient_info = [
        Paragraph(f"<b>Patient Name:</b> {csv_data['Patient Name'][0]}", styles['Normal']),
        Paragraph(f"<b>Sex:</b> {csv_data['Sex'][0]}", styles['Normal']),
        Paragraph(f"<b>Date of Birth:</b> {csv_data['Date of Birth'][0]}", styles['Normal']),
        Paragraph(f"<b>Age at Scan:</b> {csv_data['Age in month (Scanned)'][0]} months", styles['Normal']),
        Spacer(1, 12)
    ]
    content.extend(patient_info)

    # Segmented brain image
    content.append(Image(image_path, width=400, height=300))
    content.append(Spacer(1, 12))

    # Table data
    table_data = [
        ["Region", "Total Volume (mL)", "Right Volume (mL)", "Left Volume (mL)"],
        ["Frontal Lobe", 193.6, 97, 96.5],
        ["Parietal Lobe", 143.3, 72.5, 70.7],
        ["Temporal Lobe", 123, 60.6, 62.4],
        ["Occipital Lobe", 61.4, 30.1, 31.2],
        ["Cingulate Cortex", 15.4, 6.7, 8.7],
        ["Insula", 12, 6.3, 5.7],
        ["Cerebral White Matter", 268.8, 130.7, 132.2],
        ["Cerebellum", 102.7, 50.2, 52.5],
        ["Lateral Ventricle", 8.6, 4.1, 4.4],
        ["Corpus Callosum", 5.9, "N/A", "N/A"],
        ["Lentiform Nucleus", 11.9, 5.7, 6.1],
        ["Caudate", 6.4, 3.2, 3.2],
        ["Thalamus", 15.3, 7.6, 7.7],
        ["Hippocampus", 5.2, 2.6, 2.6],
        ["Amygdala", 2.5, 1.3, 1.2]
    ]

    # Create table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(table)

    # Build the PDF
    doc.build(content)
    print(f"PDF report saved successfully as: {output_pdf}")

# Main function
def main(nifti_file, csv_file_path, output_pdf):
    csv_data = pd.read_csv(csv_file_path)
    image_path = visualize_segmented_nifti_black_bg(nifti_file)
    generate_pdf_report(csv_data, output_pdf, image_path)

# File paths
nifti_file = '20190221-ST001-MNBCP000178-v01-2-15mo_MR-SE002-T1w.nii.gz'
csv_file_path = 'MNBCP000178_v01-2-15mo-20190221/pediatrics_results_p2.csv'
output_pdf = 'output_report.pdf'

main(nifti_file, csv_file_path, output_pdf)
