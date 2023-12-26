import pydicom
from pydicom.dataset import FileDataset
from pydicom.uid import UID, generate_uid
import numpy as np

def create_dicom_from_voxel_grid(voxel_grid, output_folder):
    depth, rows, columns = voxel_grid.shape

    ds = FileDataset(None, {}, file_meta=None, preamble=b"\0" * 128)
    # Set necessary metadata
    ds.PatientName = "Anonymous"
    ds.PatientID = "123456"
    ds.Modality = "CT"
    ds.ImageType = ["ORIGINAL", "PRIMARY", "AXIAL"]
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0  # unsigned integer

    # Set UID for the series
    ds.SeriesInstanceUID = generate_uid()

    for i in range(depth):
        # Set UID for each SOP Instance
        ds.SOPInstanceUID = generate_uid()

        # Set pixel data for each slice
        ds.PixelData = voxel_grid[i].tobytes()

        # Set PixelSpacing
        ds.PixelSpacing = [1.0, 1.0]

        # Set position
        ds.Rows, ds.Columns = rows, columns
        ds.SliceThickness = 1.0
        # ds.SliceLocation = i
        ds.ImagePositionPatient = [0.0, 0.0, i] # Adjust for slice position
        ds.ImageOrientationPatient = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0]  # Adjust for orientation

        # Set BitsAllocated (assuming uint16 for simplicity)
        ds.BitsAllocated = 16
        ds.BitsStored = 16
        ds.HighBit = 15

        # Specify transfer syntax explicitly
        # ds.file_meta = pydicom.Dataset()
        ds.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'  # Explicit VR Little Endian

        dicom_filename = f"{output_folder}/slice_{i+1}.dcm"
        ds.save_as(dicom_filename)

# Generate voxel grid for a sphere
radius = 1.0
resolution = 256

x = np.linspace(-radius, radius, resolution)
y = np.linspace(-radius, radius, resolution)
z = np.linspace(-radius, radius, resolution)

voxel_grid = np.zeros((resolution, resolution, resolution), dtype=np.uint16)

for i in range(resolution):
    for j in range(resolution):
        for k in range(resolution):
            if x[i]**2 + y[j]**2 + z[k]**2 <= (radius/2)**2:
                voxel_grid[i, j, k] = 1000  # Value for the sphere

output_folder = "dicom_slices"
create_dicom_from_voxel_grid(voxel_grid, output_folder)
