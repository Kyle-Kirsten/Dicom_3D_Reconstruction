import vtk
import numpy as np

def create_sphere_voxel_data(radius, resolution):
    x = np.linspace(-radius, radius, resolution)
    y = np.linspace(-radius, radius, resolution)
    z = np.linspace(-radius, radius, resolution)

    voxel_data = np.zeros((resolution, resolution, resolution), dtype=np.uint8)

    for i in range(resolution):
        for j in range(resolution):
            for k in range(resolution):
                if x[i]**2 + y[j]**2 + z[k]**2 <= radius**2:
                    voxel_data[i, j, k] = 1  # Set to 1 to represent the presence of the sphere

    return voxel_data

# Parameters for the sphere
sphere_radius = 1.0
resolution = 32

# Create sphere voxel data
voxel_data = create_sphere_voxel_data(sphere_radius, resolution)

# Convert NumPy array to VTK image data
vtk_image = vtk.vtkImageData()
vtk_image.SetDimensions(resolution, resolution, resolution)
vtk_image.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)

for i in range(resolution):
    for j in range(resolution):
        for k in range(resolution):
            vtk_image.SetScalarComponentFromFloat(i, j, k, 0, voxel_data[i, j, k])

# Create a VTK renderer
renderer = vtk.vtkRenderer()

# Create a VTK render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a VTK render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Create a VTK image actor
image_actor = vtk.vtkImageActor()
image_actor.SetInputData(vtk_image)

# Add the image actor to the renderer
renderer.AddActor(image_actor)

# Set up camera and render window
renderer.ResetCamera()
render_window.SetWindowName("VTK Viewer")
render_window.Render()

# Start the VTK event loop
render_window_interactor.Initialize()
render_window_interactor.Start()
