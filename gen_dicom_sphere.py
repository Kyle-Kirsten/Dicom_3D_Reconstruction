import numpy as np
import pydicom
from pydicom.dataset import FileDataset
from pydicom.uid import UID, generate_uid

def create_dicom_from_voxel_data(voxel_data, output_filename):
    depth, rows, columns = voxel_data.shape

    ds = FileDataset(None, {}, file_meta=None, preamble=b"\0" * 128)

    # Set DICOM file metadata
    ds.PatientName = "Anonymous"
    ds.PatientID = "123456"
    ds.Modality = "CT"
    ds.SeriesInstanceUID = generate_uid()
    ds.SOPInstanceUID = generate_uid()
    ds.ImageType = ["ORIGINAL", "PRIMARY", "AXIAL"]
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0  # unsigned integer

    ds.Rows, ds.Columns = rows, columns
    ds.NumberOfFrames = depth
    ds.PixelSpacing = [1.0, 1.0]
    ds.SliceThickness = 1.0

    # Set BitsAllocated (assuming uint16 for simplicity)
    ds.BitsAllocated = 16
    ds.BitsStored = 16
    ds.HighBit = 15
    # ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

    # Convert voxel data to DICOM pixel data
    pixel_data = (voxel_data * 1000).astype(np.uint16)  # Adjust scale as needed
    ds.PixelData = pixel_data.tobytes()

    # Save DICOM file
    ds.save_as(output_filename)

# Generate voxel data for a sphere
sphere_radius = 1.0
resolution = 10

x = np.linspace(-sphere_radius, sphere_radius, resolution)
y = np.linspace(-sphere_radius, sphere_radius, resolution)
z = np.linspace(-sphere_radius, sphere_radius, resolution)

voxel_data = np.zeros((resolution, resolution, resolution), dtype=np.uint16)

for i in range(resolution):
    for j in range(resolution):
        for k in range(resolution):
            if x[i]**2 + y[j]**2 + z[k]**2 <= sphere_radius**2:
                voxel_data[i, j, k] = 1  # Value for the sphere

# Specify output DICOM filename
output_filename = "sphere_dicom/sphere_dicom.dcm"

# Create and save DICOM file
create_dicom_from_voxel_data(voxel_data, output_filename)
