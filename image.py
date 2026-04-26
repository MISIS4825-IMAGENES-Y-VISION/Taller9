import modal

image = (
    modal.Image.from_registry("nvidia/cuda:13.2.1-devel-ubuntu24.04", add_python="3.14")
    .apt_install(["libxcb1", "libgl1", "libglib2.0-0"])
    .uv_pip_install(
        "torch>=2.11",
        "torchvision",
        "ultralytics",
        "pillow",
        "pandas",
        "matplotlib",
        "kagglehub",
        "ipykernel",
        "ipywidgets",
    )
)

app = modal.App("Taller_9_IV")


@app.function(image=image)
def main():
    pass
