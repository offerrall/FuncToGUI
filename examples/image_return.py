from functogui import App, intUi, boolUi, fileUi, imageFileReturn
from PIL import Image, ImageEnhance

def process_image(image_path: str = fileUi(),
                  brightness: int = intUi(100, max_value=200),
                  rotate: int = intUi(max_value=360),
                  flip: bool = boolUi(False)
                  ) -> imageFileReturn:

    if not image_path:
        return ""

    img = Image.open(image_path)
    img = ImageEnhance.Brightness(img).enhance(brightness/100)
    img = img if not rotate else img.rotate(rotate)
    img = img if not flip else img.transpose(Image.FLIP_LEFT_RIGHT)
    ext = image_path.split(".")[-1]
    new_path = image_path.replace(f".{ext}", f"_processed.{ext}")
    img.save(new_path)

    return new_path

App(process_image, width=500)