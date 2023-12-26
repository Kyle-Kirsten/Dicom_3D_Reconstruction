import pydicom
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def display_3d_dicom(dicom_filename):
    # Read the DICOM file

    import pydicom.uid
    ds = pydicom.read_file(dicom_filename, force=True)
    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian  # or whatever is the correct transfer syntax for the file
    print(ds.pixel_array)

    # Extract voxel data from DICOM pixel array
    voxel_data = ds.pixel_array

    # Display the 3D voxel data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(voxel_data, edgecolor='k')

    plt.title("3D DICOM Voxel Data")
    plt.show()

# Specify the DICOM filename
dicom_filename = "sphere_dicom/sphere_dicom.dcm"

# Display the 3D DICOM voxel data
display_3d_dicom(dicom_filename)
