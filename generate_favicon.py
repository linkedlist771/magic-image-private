#!/usr/bin/env python3
"""
Magic Image AI项目的favicon生成器
生成一个现代化的AI魔法主题图标
"""

import os
from PIL import Image, ImageDraw, ImageFilter
import math

def create_magic_ai_icon(size=64):
    """创建Magic Image AI主题的图标"""
    # 创建透明背景的图像
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 计算中心点
    center = size // 2
    
    # 1. 绘制渐变背景圆形
    for r in range(center - 2, 0, -1):
        # 从外到内的渐变：紫色 -> 粉色 -> 蓝色
        progress = (center - 2 - r) / (center - 2)
        
        if progress < 0.5:
            # 外层：紫色到粉色
            t = progress * 2
            red = int(99 + t * 137)    # 99 -> 236
            green = int(102 + t * 54)  # 102 -> 156  
            blue = int(241 + t * 14)   # 241 -> 255
        else:
            # 内层：粉色到亮蓝
            t = (progress - 0.5) * 2
            red = int(236 - t * 137)   # 236 -> 99
            green = int(156 + t * 100) # 156 -> 256
            blue = int(255)            # 保持255
        
        alpha = int(240 * (1 - progress * 0.1))  # 轻微透明度变化
        color = (red, green, blue, alpha)
        
        # 绘制圆形
        draw.ellipse([center - r, center - r, center + r, center + r], 
                    fill=color, outline=None)
    
    # 2. 绘制AI神经网络连接点
    node_positions = [
        (center * 0.5, center * 0.6),      # 左上
        (center, center * 0.4),            # 上中
        (center * 1.5, center * 0.6),      # 右上
        (center * 0.6, center),            # 左中
        (center * 1.4, center),            # 右中
        (center * 0.5, center * 1.4),      # 左下
        (center, center * 1.6),            # 下中
        (center * 1.5, center * 1.4),      # 右下
    ]
    
    # 绘制连接线
    connections = [
        (0, 1), (1, 2), (0, 3), (2, 4), 
        (3, 5), (4, 7), (5, 6), (7, 6),
        (1, 3), (1, 4), (3, 6), (4, 6)
    ]
    
    for start_idx, end_idx in connections:
        start_pos = node_positions[start_idx]
        end_pos = node_positions[end_idx]
        draw.line([start_pos, end_pos], fill=(255, 255, 255, 120), width=2)
    
    # 绘制节点
    for pos in node_positions:
        node_size = size // 16
        draw.ellipse([pos[0] - node_size, pos[1] - node_size, 
                     pos[0] + node_size, pos[1] + node_size], 
                    fill=(255, 255, 255, 200))
    
    # 3. 添加魔法星星效果
    star_positions = [
        (center * 0.3, center * 0.3),
        (center * 1.7, center * 0.2), 
        (center * 1.8, center * 1.7),
        (center * 0.2, center * 1.6),
    ]
    
    for i, pos in enumerate(star_positions):
        # 不同大小的星星
        star_size = (size // 20) + (i % 2)
        # 金色星星
        draw.text(pos, "✦", fill=(255, 215, 0, 220), anchor="mm")
    
    # 4. 中心添加画笔/魔法棒图标
    brush_size = size // 6
    brush_x, brush_y = center, center
    
    # 画笔柄
    draw.line([brush_x - brush_size//2, brush_y + brush_size//2,
              brush_x + brush_size//2, brush_y - brush_size//2], 
             fill=(255, 255, 255, 255), width=3)
    
    # 画笔头
    draw.ellipse([brush_x + brush_size//3, brush_y - brush_size//2 - 2,
                 brush_x + brush_size//2 + 2, brush_y - brush_size//3 + 2], 
                fill=(255, 215, 0, 255))
    
    return img

def main():
    """主函数：生成多种尺寸的favicon"""
    print("🎨 开始生成Magic Image AI主题favicon...")
    
    # 生成高清版本
    hd_icon = create_magic_ai_icon(256)
    
    # 创建不同尺寸
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        if size == 256:
            resized = hd_icon
        else:
            resized = hd_icon.resize((size, size), Image.Resampling.LANCZOS)
        images.append(resized)
        print(f"✅ 生成 {size}x{size} 图标")
    
    # 保存为ICO文件（包含多种尺寸）
    ico_path = "./favicon.ico"
    images[0].save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images])
    
    # 也保存PNG版本用于预览
    hd_icon.save("./magic-icon-preview.png", format='PNG')
    
    print(f"🎉 成功生成favicon.ico!")
    print(f"📁 文件位置: {ico_path}")
    print("🌟 特色: AI神经网络 + 魔法元素 + 现代渐变")
    
    return ico_path

if __name__ == "__main__":
    main()
