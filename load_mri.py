# import nibabel as nib
# import matplotlib.pyplot as plt
# import pandas as pd
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.units import inch

# # Function to generate PDF report based on CSV data
# def generate_pdf_report(csv_data, output_pdf, image_path):
#     c = canvas.Canvas(output_pdf, pagesize=letter)
#     c.setFont("Helvetica", 12)

#     # Title
#     c.drawString(100, 750, "Brain MRI Segmentation Volume Report")

#     # Insert the colorful image
#     c.drawImage(image_path, 100, 450, width=400, height=300)

#     # Extract general patient data
#     patient_name = csv_data['Patient Name'][0]
#     patient_sex = csv_data['Sex'][0]
#     dob = csv_data['Date of Birth'][0]
#     age_at_scan = csv_data['Age in month (Scanned)'][0]

#     # Write basic patient info
#     c.drawString(100, 430, f"Patient Name: {patient_name}")
#     c.drawString(100, 410, f"Sex: {patient_sex}")
#     c.drawString(100, 390, f"Date of Birth: {dob}")
#     c.drawString(100, 370, f"Age at Scan: {age_at_scan} months")

#     # Region volume data headers
#     y_pos = 340
#     region_headers = ["Region", "Total Volume (mL)", "Right Volume (mL)", "Left Volume (mL)"]
#     c.drawString(100, y_pos, f"{region_headers[0]:<30} {region_headers[1]:<20} {region_headers[2]:<20} {region_headers[3]}")
#     y_pos -= 20

#     # Extract relevant columns for regions and volumes
#     regions = [
#         ('Frontal Lobe', 193.6, 97, 96.5),
#         ('Parietal Lobe', 143.3, 72.5, 70.7),
#         ('Temporal Lobe', 123, 60.6, 62.4),
#         ('Occipital Lobe', 61.4, 30.1, 31.2),
#         ('Cingulate Cortex', 15.4, 6.7, 8.7),
#         ('Insula', 12, 6.3, 5.7),
#         ('Cerebral White Matter', 268.8, 130.7, 132.2),
#         ('Cerebellum', 102.7, 50.2, 52.5),
#         ('Lateral Ventricle', 8.6, 4.1, 4.4),
#         ('Corpus Callosum', 5.9, 'N/A', 'N/A'),
#         ('Lentiform Nucleus', 11.9, 5.7, 6.1),
#         ('Caudate', 6.4, 3.2, 3.2),
#         ('Thalamus', 15.3, 7.6, 7.7),
#         ('Hippocampus', 5.2, 2.6, 2.6),
#         ('Amygdala', 2.5, 1.3, 1.2)
#     ]

#     for region, total_vol, right_vol, left_vol in regions:
#         c.drawString(100, y_pos, f"{region:<30} {total_vol:<20} {right_vol:<20} {left_vol}")
#         y_pos -= 20
        
#         if y_pos < 100:  # Create new page if not enough space
#             c.showPage()
#             c.setFont("Helvetica", 12)
#             y_pos = 750

#     # Save the PDF
#     c.save()
#     print(f"PDF report saved successfully as: {output_pdf}")

# # Function to load and visualize NIfTI data
# def visualize_nifti(nifti_file, slice_index=50):
#     # Load the NIfTI file
#     img = nib.load(nifti_file)
#     data = img.get_fdata()

#     # Visualize a specific slice (e.g., slice 50) with a color map
#     plt.imshow(data[:, :, slice_index], cmap="jet")  # Use a colorful colormap
#     plt.title(f"NIfTI File - Slice {slice_index}")
#     plt.axis("off")
    
#     # Save the image instead of showing it
#     image_path = 'nifti_slice.png'
#     plt.savefig(image_path, bbox_inches='tight', pad_inches=0.1)
#     plt.close()
    
#     return image_path

# # Main processing function
# def main(nifti_file, csv_file_path, output_pdf):
#     # Load and visualize NIfTI data
#     image_path = visualize_nifti(nifti_file)

#     # Load the CSV data
#     csv_data = pd.read_csv(csv_file_path)

#     # Generate PDF report
#     generate_pdf_report(csv_data, output_pdf, image_path)

# if __name__ == "__main__":
#     # File paths
#     nifti_file = '20190221-ST001-MNBCP000178-v01-2-15mo_MR-SE002-T1w.nii.gz'  # Path to your NIfTI file
#     csv_file_path = 'MNBCP000178_v01-2-15mo-20190221/pediatrics_results_p2.csv'  # Path to your CSV file
#     output_pdf = 'brain_volumes_report.pdf'
    
#     # Run the main function
#     main(nifti_file, csv_file_path, output_pdf)


import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle  # <-- Add this import
from reportlab.lib import colors




# def generate_pdf_report(csv_data, output_pdf, image_path):
#     c = canvas.Canvas(output_pdf, pagesize=letter)
#     c.setFont("Helvetica", 12)

#     # Title
#     c.drawString(100, 750, "Brain MRI Segmentation Volume Report")

#     # Insert the colorful image
#     c.drawImage(image_path, 100, 450, width=400, height=300)

#     # Extract general patient data
#     patient_name = csv_data['Patient Name'][0]
#     patient_sex = csv_data['Sex'][0]
#     dob = csv_data['Date of Birth'][0]
#     age_at_scan = csv_data['Age in month (Scanned)'][0]

#     # Write basic patient info
#     c.drawString(100, 430, f"Patient Name: {patient_name}")
#     c.drawString(100, 410, f"Sex: {patient_sex}")
#     c.drawString(100, 390, f"Date of Birth: {dob}")
#     c.drawString(100, 370, f"Age at Scan: {age_at_scan} months")

#     # Region volume data headers
#     data = [
#         ["Region", "Total Volume (mL)", "Right Volume (mL)", "Left Volume (mL)"],
#         ["Frontal Lobe", 193.6, 97, 96.5],
#         ["Parietal Lobe", 143.3, 72.5, 70.7],
#         ["Temporal Lobe", 123, 60.6, 62.4],
#         ["Occipital Lobe", 61.4, 30.1, 31.2],
#         ["Cingulate Cortex", 15.4, 6.7, 8.7],
#         ["Insula", 12, 6.3, 5.7],
#         ["Cerebral White Matter", 268.8, 130.7, 132.2],
#         ["Cerebellum", 102.7, 50.2, 52.5],
#         ["Lateral Ventricle", 8.6, 4.1, 4.4],
#         ["Corpus Callosum", 5.9, 'N/A', 'N/A'],
#         ["Lentiform Nucleus", 11.9, 5.7, 6.1],
#         ["Caudate", 6.4, 3.2, 3.2],
#         ["Thalamus", 15.3, 7.6, 7.7],
#         ["Hippocampus", 5.2, 2.6, 2.6],
#         ["Amygdala", 2.5, 1.3, 1.2]
#     ]

#     # Create table with data
#     table = Table(data)

#     # Add style to the table
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Header background color
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Cell background color
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Cell borders
#     ])

#     table.setStyle(style)

#     # Set position and size of table
#     table.wrapOn(c, 400, 600)
#     table.drawOn(c, 100, 100)

#     # Save the PDF
#     c.save()
#     print(f"PDF report saved successfully as: {output_pdf}")
# # Function to visualize and save segmented brain images
def visualize_segmented_nifti(nifti_file):
    # Load the NIfTI file
    img = nib.load(nifti_file)
    data = img.get_fdata()

    # Squeeze the data to remove any singleton dimensions
    data = np.squeeze(data)

    # Define three views: axial, sagittal, and coronal
    axial_slice = data[:, :, data.shape[2] // 2]
    sagittal_slice = data[data.shape[0] // 2, :, :]
    coronal_slice = data[:, data.shape[1] // 2, :]

    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    views = [axial_slice, sagittal_slice, coronal_slice]
    titles = ["Axial", "Sagittal", "Coronal"]

    for i, view in enumerate(views):
        axes[0, i].imshow(view.T, cmap="gray", origin="lower")
        axes[0, i].set_title(f"{titles[i]} - T1w")
        axes[0, i].axis("off")

    # Now create segmented (colorful) versions of these slices
    cmap = plt.get_cmap("Spectral")
    for i, view in enumerate(views):
        segmented_view = np.ma.masked_where(view <= 0, view)  # Mask non-brain parts
        axes[1, i].imshow(segmented_view.T, cmap=cmap, origin="lower")
        axes[1, i].set_title(f"{titles[i]} - Segmentation")
        axes[1, i].axis("off")

    # Save the resulting figure with the 3 views and segmentation
    image_path = 'segmented_brain_views.png'
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    return image_path

# Function to generate PDF report based on CSV data
def generate_pdf_report(csv_data, output_pdf, image_path):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Title
    c.drawString(100, 750, "Brain MRI Segmentation Volume Report")

    # Insert the colorful image
    c.drawImage(image_path, 100, 450, width=400, height=300)

    # Extract general patient data
    patient_name = csv_data['Patient Name'][0]
    patient_sex = csv_data['Sex'][0]
    dob = csv_data['Date of Birth'][0]
    age_at_scan = csv_data['Age in month (Scanned)'][0]

    # Write basic patient info
    c.drawString(100, 430, f"Patient Name: {patient_name}")
    c.drawString(100, 410, f"Sex: {patient_sex}")
    c.drawString(100, 390, f"Date of Birth: {dob}")
    c.drawString(100, 370, f"Age at Scan: {age_at_scan} months")

    # Region volume data headers
    y_pos = 340
    region_headers = ["Region", "Total Volume (mL)", "Right Volume (mL)", "Left Volume (mL)"]
    c.drawString(100, y_pos, f"{region_headers[0]:<30} {region_headers[1]:<20} {region_headers[2]:<20} {region_headers[3]}")
    y_pos -= 20

    # Extract relevant columns for regions and volumes
    regions = [
        ('Frontal Lobe', 193.6, 97, 96.5),
        ('Parietal Lobe', 143.3, 72.5, 70.7),
        ('Temporal Lobe', 123, 60.6, 62.4),
        ('Occipital Lobe', 61.4, 30.1, 31.2),
        ('Cingulate Cortex', 15.4, 6.7, 8.7),
        ('Insula', 12, 6.3, 5.7),
        ('Cerebral White Matter', 268.8, 130.7, 132.2),
        ('Cerebellum', 102.7, 50.2, 52.5),
        ('Lateral Ventricle', 8.6, 4.1, 4.4),
        ('Corpus Callosum', 5.9, 'N/A', 'N/A'),
        ('Lentiform Nucleus', 11.9, 5.7, 6.1),
        ('Caudate', 6.4, 3.2, 3.2),
        ('Thalamus', 15.3, 7.6, 7.7),
        ('Hippocampus', 5.2, 2.6, 2.6),
        ('Amygdala', 2.5, 1.3, 1.2)
    ]

    for region, total_vol, right_vol, left_vol in regions:
        c.drawString(100, y_pos, f"{region:<30} {total_vol:<20} {right_vol:<20} {left_vol}")
        y_pos -= 20
        
        if y_pos < 100:  # Create new page if not enough space
            c.showPage()
            c.setFont("Helvetica", 12)
            y_pos = 750

    # Save the PDF
    c.save()
    print(f"PDF report saved successfully as: {output_pdf}")

# Main processing function
def main(nifti_file, csv_file_path, output_pdf):
    # Load and visualize NIfTI data
    image_path = visualize_segmented_nifti(nifti_file)

    # Load the CSV data
    csv_data = pd.read_csv(csv_file_path)

    # Generate PDF report
    generate_pdf_report(csv_data, output_pdf, image_path)

if __name__ == "__main__":
    # File paths
    nifti_file = '20190221-ST001-MNBCP000178-v01-2-15mo_MR-SE002-T1w.nii'  # Path to your NIfTI file
    csv_file_path = 'MNBCP000178_v01-2-15mo-20190221/pediatrics_results_p2.csv'  # Path to your CSV file
    output_pdf = 'brain_volumes_report.pdf'
    
    # Run the main function
    main(nifti_file, csv_file_path, output_pdf)
