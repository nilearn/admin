# get a mesh and contrast maps in Nifti format
from nilearn.datasets import fetch_surf_fsaverage, fetch_localizer_contrasts

fsaverage = fetch_surf_fsaverage()
cmaps = fetch_localizer_contrasts(
    n_subjects=10, contrasts=["left button press", "right button press"]
)

# project volume onto a mesh via SurfaceImage object
from nilearn.surface import SurfaceImage

mesh = {"left": fsaverage["pial_left"], "right": fsaverage["pial_right"]}

surf_img = SurfaceImage.from_volume(mesh=mesh, volume_img=cmaps["cmaps"][0])

print(surf_img)

# do it for each contrast map
surf_imgs = []
labels = []

for cmap in cmaps["cmaps"]:
    surf_img = SurfaceImage.from_volume(mesh=mesh, volume_img=cmap)
    surf_imgs.append(surf_img)
    if "Left" in cmap:
        labels.append("left")
    else:
        labels.append("right")

# quickly Decode from surface data
from nilearn.decoding import Decoder

decoder = Decoder(n_jobs=5)
decoder.fit(surf_imgs, y=labels)


# easily plot classifier's coefficients
from nilearn.plotting import view_surf

plotting.view_surf(decoder.coef_img_["left"])
plotting.view_surf(decoder.coef_img_["right"])
