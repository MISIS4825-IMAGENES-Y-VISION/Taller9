import modal

image = (
    modal.Image.from_registry("nvidia/cuda:13.2.1-devel-ubuntu24.04", add_python="3.14")
    .apt_install("libxcb1")
    .uv_pip_install(
        "torch>=2.11",
        "torchvision",
        "ultralytics",
        "pillow",
        "pandas",
        "matplotlib",
        "kaggle",
    )
)

app = modal.App("Taller_9_IV")


@app.function(image=image)
def main():
    pass
