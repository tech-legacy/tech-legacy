import os

from PIL import Image, ImageDraw, ImageFilter


def create_high_quality_rounded_icons(input_path, output_folder, corner_radius=200, sizes=(128, 64, 32, 16)):
    # 打开原始图片
    image = Image.open(input_path).convert("RGBA")

    # 确保图片为正方形
    min_side = min(image.size)
    image = image.crop((0, 0, min_side, min_side))

    for size in sizes:
        # 调整图片尺寸
        resized_image = image.resize((size, size), Image.Resampling.LANCZOS)

        # 创建高质量的圆角蒙版
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(
            [(1, 1), (size - 1, size - 1)],  # 边缘留1像素，避免溢出
            radius=corner_radius * size // min_side,  # 圆角半径按比例缩放
            fill=255
        )
        mask = mask.filter(ImageFilter.SMOOTH)

        # 应用圆角蒙版
        rounded_image = Image.new("RGBA", (size, size), (255, 255, 255, 0))  # 创建透明背景
        rounded_image.paste(resized_image, (0, 0), mask=mask)

        # 添加更强的锐化滤镜
        if size / min_side < 0.1:
            rounded_image = rounded_image.filter(ImageFilter.UnsharpMask(radius=1.0, percent=150, threshold=3))

        # 保存为 PNG 格式
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = f"{output_folder}/icon_{size}x{size}.png"
        rounded_image.save(output_path, format="PNG")
        print(f"高质量圆角图标已保存到 {output_path}")


if __name__ == '__main__':
    input_path = "../assets/chatgpt-古老的-蒸汽朋克机器人-保险箱3.webp"
    output_folder = "../assets"

    create_high_quality_rounded_icons(
        input_path=input_path,
        output_folder=output_folder,
        corner_radius=100,
        sizes=(512, 256, 128, 96, 64, 48, 32, 24, 16)
    )
