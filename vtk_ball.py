import vtkmodules.all as vtk
import numpy as np

# 创建球体源
sphere_source = vtk.vtkSphereSource()
sphere_source.SetRadius(1.0)
sphere_source.SetThetaResolution(32)
sphere_source.SetPhiResolution(16)

# 创建球体的映射器
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere_source.GetOutputPort())

# 创建球体的演员
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# 创建渲染器和渲染窗口
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# 创建交互器和渲染窗口交互器
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# 将演员添加到渲染器中
renderer.AddActor(actor)

# 设置渲染器的背景颜色
renderer.SetBackground(1.0, 1.0, 1.0)

# 设置相机位置和方向
renderer.GetActiveCamera().Azimuth(30)
renderer.GetActiveCamera().Elevation(30)

# 设置交互器样式
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

# 打开渲染窗口
render_window.Render()
interactor.Start()
