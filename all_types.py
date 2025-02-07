from functogui import App, intUi, strUi, floatUi, listUi, fileUi, imageFileReturn, folderUi, passwordUi
from typing import Annotated
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

EFFECTS = ["None", "Blur", "Contour", "Edge Enhance", "Sharpen"]

# This is a simple example of a function that uses all the types of inputs and outputs.
# The function itself doesn't make much sense, it's just to show you all the different types there are.

def all_types_test(image_path: Annotated[str, fileUi] = "",
                   folder_path: Annotated[str, folderUi] = "",
                   brightness: Annotated[float, floatUi(min_value=0.0, max_value=2.0)] = 1.0,
                   rotation: Annotated[int, intUi(min_value=0, max_value=360)] = 0,
                   watermark: Annotated[str, strUi(min_length=0, max_length=20)] = "",
                   password: Annotated[str, passwordUi(min_length=3, max_length=10)] ="test",
                   effect: Annotated[str, listUi(values=EFFECTS)] = "None",
                   color: tuple[int, int, int, int] = (255, 0, 0, 125),
                   grayscale: bool = False
                   ) -> Annotated[str, imageFileReturn]:

    print(f"folder_path: {folder_path}")
    print(f"password: {password}")

    if not image_path:
        return ""

    try:
        img = Image.open(image_path)
        img = ImageEnhance.Brightness(img).enhance(brightness)

        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        if rotation:
            img = img.rotate(rotation, expand=True)

        if grayscale:
            img = img.convert('L')
        
        if color:
            print(color)
            overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            
            width, height = img.size
            square_size = min(width, height) // 3
            x1 = (width - square_size) // 2
            y1 = (height - square_size) // 2
            x2 = x1 + square_size
            y2 = y1 + square_size
            
            draw.rectangle([x1, y1, x2, y2], fill=color)
            
            if img.mode == 'RGBA':
                img = Image.alpha_composite(img, overlay)
            else:
                img = Image.alpha_composite(img.convert('RGBA'), overlay)

        if effect != "None":
            if effect == "Blur":
                img = img.filter(ImageFilter.BLUR)
            elif effect == "Contour":
                img = img.filter(ImageFilter.CONTOUR)
            elif effect == "Edge Enhance":
                img = img.filter(ImageFilter.EDGE_ENHANCE)
            elif effect == "Sharpen":
                img = img.filter(ImageFilter.SHARPEN)
        
        if watermark:
            draw = ImageDraw.Draw(img)
            text_pos = (10, 10)
            draw.text(text_pos, watermark, fill="white")
        
        ext = image_path.split(".")[-1].lower()
        output_path = image_path.replace(f".{ext}", f"_processed.{ext}")
        
        if ext in ['jpg', 'jpeg']:
            img = img.convert('RGB')
        
        img.save(output_path)
        return output_path
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

App(all_types_test, width=500)