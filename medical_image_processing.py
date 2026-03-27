"""
医学图像处理 Demo
展示：图像读取、滤波、边缘检测、可视化
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_synthetic_ct(size=256):
    """
    生成模拟 CT 图像（包含圆形结构模拟器官）
    """
    image = np.zeros((size, size))
    
    # 创建背景噪声
    image += 0.1 * np.random.randn(size, size)
    
    # 添加圆形结构（模拟不同组织）
    y, x = np.ogrid[:size, :size]
    center = size // 2
    
    # 大圆（模拟主要器官）
    mask1 = (x - center)**2 + (y - center)**2 <= (size//3)**2
    image[mask1] = 0.6 + 0.1 * np.random.randn(np.sum(mask1))
    
    # 小圆（模拟病变/结节）
    mask2 = (x - center - 30)**2 + (y - center - 20)**2 <= 20**2
    image[mask2] = 0.9 + 0.05 * np.random.randn(np.sum(mask2))
    
    # 另一个小圆
    mask3 = (x - center + 40)**2 + (y - center + 30)**2 <= 15**2
    image[mask3] = 0.3 + 0.05 * np.random.randn(np.sum(mask3))
    
    return image

def apply_gaussian_filter(image, sigma=2):
    """
    高斯滤波（平滑/去噪）
    """
    return ndimage.gaussian_filter(image, sigma=sigma)

def apply_edge_detection(image):
    """
    边缘检测（Sobel 算子）
    """
    sx = ndimage.sobel(image, axis=0, mode='constant')
    sy = ndimage.sobel(image, axis=1, mode='constant')
    sobel = np.hypot(sx, sy)
    return sobel

def apply_threshold(image, threshold=0.5):
    """
    阈值分割
    """
    return (image > threshold).astype(float)

def plot_results(original, filtered, edges, segmented):
    """
    可视化结果
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 原始图像
    im0 = axes[0, 0].imshow(original, cmap='gray')
    axes[0, 0].set_title('模拟 CT 图像')
    axes[0, 0].axis('off')
    plt.colorbar(im0, ax=axes[0, 0], fraction=0.046)
    
    # 滤波后
    im1 = axes[0, 1].imshow(filtered, cmap='gray')
    axes[0, 1].set_title('高斯滤波后（σ=2）')
    axes[0, 1].axis('off')
    plt.colorbar(im1, ax=axes[0, 1], fraction=0.046)
    
    # 边缘检测
    im2 = axes[1, 0].imshow(edges, cmap='gray')
    axes[1, 0].set_title('边缘检测（Sobel）')
    axes[1, 0].axis('off')
    plt.colorbar(im2, ax=axes[1, 0], fraction=0.046)
    
    # 分割结果
    im3 = axes[1, 1].imshow(segmented, cmap='gray')
    axes[1, 1].set_title('阈值分割（T=0.5）')
    axes[1, 1].axis('off')
    plt.colorbar(im3, ax=axes[1, 1], fraction=0.046)
    
    plt.tight_layout()
    plt.savefig('medical_image_results.png', dpi=150)
    plt.show()
    
    print(f"\n✅ 结果已保存到 medical_image_results.png")

def main():
    print("=" * 50)
    print("医学图像处理 Demo")
    print("=" * 50)
    
    # 生成模拟 CT 图像
    print("\n🔄 正在生成模拟 CT 图像...")
    original = generate_synthetic_ct(size=256)
    
    # 高斯滤波
    print("🔄 正在进行高斯滤波...")
    filtered = apply_gaussian_filter(original, sigma=2)
    
    # 边缘检测
    print("🔄 正在进行边缘检测...")
    edges = apply_edge_detection(filtered)
    
    # 阈值分割
    print("🔄 正在进行阈值分割...")
    segmented = apply_threshold(filtered, threshold=0.5)
    
    # 统计信息
    print(f"\n📊 图像统计:")
    print(f"   - 图像尺寸: {original.shape}")
    print(f"   - 像素值范围: [{original.min():.2f}, {original.max():.2f}]")
    print(f"   - 分割区域面积: {np.sum(segmented)} 像素")
    
    # 可视化
    print("\n📊 正在生成可视化图表...")
    plot_results(original, filtered, edges, segmented)
    
    print("\n" + "=" * 50)
    print("✅ Demo 运行完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()