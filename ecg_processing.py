"""
ECG 心电图信号处理 Demo
展示：信号模拟、滤波、特征提取、可视化
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_ecg(duration=10, fs=360):
    """
    模拟生成 ECG 信号
    duration: 信号时长（秒）
    fs: 采样率（Hz）
    """
    t = np.linspace(0, duration, int(duration * fs))
    
    # 基础心率 75 bpm
    hr = 75 / 60  # Hz
    
    # 模拟 ECG 波形（简化版）
    ecg = 0.6 * np.sin(2 * np.pi * hr * t)  # 基础波形
    ecg += 0.2 * np.sin(2 * np.pi * 2 * hr * t)  # 二次谐波
    ecg += 0.1 * np.random.randn(len(t))  # 添加噪声
    
    # 模拟 R 波（QRS 复合波）
    for i in range(int(duration * hr)):
        idx = int(i * fs / hr)
        if idx < len(ecg):
            # 创建一个尖峰模拟 R 波
            r_wave = np.exp(-((t - t[idx]) ** 2) / 0.001)
            ecg += 1.5 * r_wave
    
    return t, ecg

def bandpass_filter(data, fs, lowcut=0.5, highcut=45, order=4):
    """
    带通滤波器
    保留 0.5-45 Hz 的频率成分（ECG 主要频率范围）
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return signal.filtfilt(b, a, data)

def detect_r_peaks(ecg, fs, threshold=0.8):
    """
    R 波检测（简化版）
    使用峰值检测
    """
    # 找到所有峰值
    peaks, _ = signal.find_peaks(ecg, height=threshold, distance=fs*0.5)
    return peaks

def plot_results(t, ecg_raw, ecg_filtered, r_peaks, fs):
    """
    可视化结果
    """
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    
    # 原始信号
    axes[0].plot(t, ecg_raw, 'b', linewidth=0.5)
    axes[0].set_title('原始 ECG 信号（含噪声）')
    axes[0].set_xlabel('时间 (s)')
    axes[0].set_ylabel('幅值')
    axes[0].grid(True)
    
    # 滤波后信号
    axes[1].plot(t, ecg_filtered, 'g', linewidth=0.5)
    axes[1].set_title('滤波后 ECG 信号（0.5-45 Hz 带通）')
    axes[1].set_xlabel('时间 (s)')
    axes[1].set_ylabel('幅值')
    axes[1].grid(True)
    
    # R 波检测结果
    axes[2].plot(t, ecg_filtered, 'g', linewidth=0.5)
    axes[2].plot(t[r_peaks], ecg_filtered[r_peaks], 'ro', markersize=8)
    axes[2].set_title(f'R 波检测结果（检测到 {len(r_peaks)} 个 R 波）')
    axes[2].set_xlabel('时间 (s)')
    axes[2].set_ylabel('幅值')
    axes[2].grid(True)
    
    plt.tight_layout()
    plt.savefig('ecg_results.png', dpi=150)
    plt.show()
    
    print(f"\n✅ 结果已保存到 ecg_results.png")

def main():
    print("=" * 50)
    print("ECG 心电图信号处理 Demo")
    print("=" * 50)
    
    # 参数设置
    fs = 360  # 采样率 360 Hz
    duration = 10  # 信号时长 10 秒
    
    print(f"\n📊 参数设置:")
    print(f"   - 采样率: {fs} Hz")
    print(f"   - 信号时长: {duration} 秒")
    print(f"   - 数据点数: {fs * duration}")
    
    # 1. 生成模拟 ECG 信号
    print("\n🔄 正在生成模拟 ECG 信号...")
    t, ecg_raw = generate_ecg(duration=duration, fs=fs)
    
    # 2. 带通滤波
    print("🔄 正在进行带通滤波...")
    ecg_filtered = bandpass_filter(ecg_raw, fs)
    
    # 3. R 波检测
    print("🔄 正在检测 R 波...")
    r_peaks = detect_r_peaks(ecg_filtered, fs)
    
    # 4. 计算心率
    rr_intervals = np.diff(r_peaks) / fs  # RR 间期（秒）
    heart_rate = 60 / np.mean(rr_intervals)  # 心率（bpm）
    
    print(f"\n📈 分析结果:")
    print(f"   - 检测到 R 波数量: {len(r_peaks)}")
    print(f"   - 平均 RR 间期: {np.mean(rr_intervals)*1000:.1f} ms")
    print(f"   - 估算心率: {heart_rate:.1f} bpm")
    
    # 5. 可视化
    print("\n📊 正在生成可视化图表...")
    plot_results(t, ecg_raw, ecg_filtered, r_peaks, fs)
    
    print("\n" + "=" * 50)
    print("✅ Demo 运行完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()