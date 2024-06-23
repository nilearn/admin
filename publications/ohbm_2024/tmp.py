from nilearn.experimental import surface, plotting
from nilearn.plotting import show

img = surface.fetch_nki(mesh_type="inflated", n_subjects=1)[0]

masker = surface.SurfaceMasker()
masked_data = masker.fit_transform(img)
first_data = masked_data[0]
first_data = masker.inverse_transform(first_data)

bg_data = surface.load_fsaverage_data(data_type="curvature", mesh_type="inflated")

# easy plotting and reporting
report = masker.generate_report()
plotting.plot_surf(first_data, threshold=0.5)
show()



from nilearn.glm.first_level import FirstLevelModel

glm = FirstLevelModel(t_r).fit(surface_time_series, events)
z_scores = glm.compute_contrast("language-string")
plotting.plot_surf_stat_map(stat_map=z_scores, hemi="left", threshold=2.0, ...)