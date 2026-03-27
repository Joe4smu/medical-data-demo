"""
信号频谱分析 Demo
展示：FFT 变换、频谱图、功率谱密度
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_multi_frequency_signal(duration=5, fs=1000):
    """
    生成多频率混合信号
    模拟：多个频率成分 + 噪声
    """
    t = np.linspace(0, duration, int(duration * fs))
    
    # 多个频率成分
    signal_50hz = 1.0 * np.sin(2 * np.pi * 50 * t)   # 50 Hz 主频
    signal_120hz = 0.5 * np.sin(2 * np.pi * 120 * t) # 120 Hz 谐波
    signal_200hz = 0.3 * np.sin(2 * np.pi * 200 * t) # 200 Hz 高频
    noise = 0.2 * np.random.randn(len(t))            # 噪声
    
    # 混合信号
    mixed_signal = signal_50hz + signal_120hz + signal_200hz + noise
    
    return t, mixed_signal

def compute_fft(signal_data, fs):
    """
    计算 FFT（快速傅里叶变换）
    """
    n = len(signal_data)
    fft_result = np.fft.fft(signal_data)
    fft_freq = np.fft.fftfreq(n, 1/fs)
    
    # 只取正频率部分
    positive_freq_idx = fft_freq > 0
    fft_freq = fft_freq[positive_freq_idx]
    fft_magnitude = np.abs(fft_result[positive_freq_idx]) * 2 / n
    
    return fft_freq, fft_magnitude

def compute_power_spectrum(signal_data, fs):
    """
    计算功率谱密度（Welch 方法）
    """
    freqs, psd = signal.welch(signal_data, fs, nperseg=1024)
    return freqs, psd

def apply_bandpass(signal_data, fs, lowcut, highcut):
    """
    带通滤波
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(4, [low, high], btype='band')
    return signal.filtfilt(b, a, signal_data)

def plot_results(t, signal_raw, signal_filtered, fft_freq, fft_mag, psd_freq, psd):
    """
    可视化结果
    """
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    
    # 原始信号时域
    axes[0, 0].plot(t[:1000], signal_raw[:1000], 'b', linewidth=0.5)
    axes[0, 0].set_title('原始信号（时域）')
    axes[0, 0].set_xlabel('时间 (s)')
    axes[0, 0].set_ylabel('幅值')
    axes[0, 0].grid(True)
    
    # 滤波后信号时域
    axes[0, 1].plot(t[:1000], signal_filtered[:1000], 'g', linewidth=0.5)
    axes[0, 1].set_title('滤波后信号（80-150 Hz 带通）')
    axes[0, 1].set_xlabel('时间 (s)')
    axes[0, 1].set_ylabel('幅值')
    axes[0, 1].grid(True)
    
    # 原始信号频谱
    axes[1, 0].plot(fft_freq, fft_mag, 'b', linewidth=0.5)
    axes[1, 0].set_title('原始信号频谱（FFT）')
    axes[1, 0].set_xlabel('频率 (Hz)')
    axes[1, 0].set_ylabel('幅值')
    axes[1, 0].set_xlim(0, 300)
    axes[1, 0].grid(True)
    
    # 标注峰值频率
    peak_indices = signal.find_peaks(fft_mag, height=0.1, distance=10)[0]
    for idx in peak_indices[:5]:
        if fft_freq[idx] < 300:
            axes[1, 0].annotate(f'{fft_freq[idx]:.0f}Hz', 
                               xy=(fft_freq[idx], fft_mag[idx]),
                               xytext=(fft_freq[idx]+10, fft_mag[idx]+0.1),
                               fontsize=8)
    
    # 功率谱密度
    axes[1, 1].semilogy(psd_freq, psd, 'r', linewidth=0.5)
    axes[1, 1].set_title('功率谱密度（Welch 方法）')
    axes[1, 1].set_xlabel('频率 (Hz)')
    axes[1, 1].set_ylabel('功率谱密度 (V²/Hz)')
    axes[1, 1].set_xlim(0, 300)
    axes[1, 1].grid(True)
    
    # 频谱图（时频分析）
    f, t_spec, Sxx = signal.spectrogram(signal_raw, 1000, nperseg=256)
    im = axes[2, 0].pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud', cmap='jet')
    axes[2, 0].set_title('时频谱图（Spectrogram）')
    axes[2, 0].set_xlabel('时间 (s)')
    axes[2, 0].set_ylabel('频率 (Hz)')
    axes[2, 0].set_ylim(0, 300)
    plt.colorbar(im, ax=axes[2, 0], label='功率 (dB)')
    
    # 频率成分饼图
    freq_components = ['50 Hz', '120 Hz', '200 Hz', '噪声']
    amplitudes = [1.0, 0.5, 0.3, 0.2]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    axes[2, 1].pie(amplitudes, labels=freq_components, colors=colors, autopct='%1.1f%%')
    axes[2, 1].set_title('频率成分占比')
    
    plt.tight_layout()
    plt.savefig('spectrum_results.png', dpi=150)
    plt.show()
    
    print(f"\n✅ 结果已保存到 spectrum_results.png")

def main():
    print("=" * 50)
    print("信号频谱分析 Demo")
    print("=" * 50)
    
    # 参数设置
    fs = 1000  # 采样率 1000 Hz
    duration = 5  # 信号时长 5 秒
    
    print(f"\n📊 参数设置:")
    print(f"   - 采样率: {fs} Hz")
    print(f"   - 信号时长: {duration} 秒")
    print(f"   - 频率分辨率: {fs/(duration*fs):.2f} Hz")
    
    # 生成多频率信号
    print("\n🔄 正在生成多频率混合信号...")
    t, signal_raw = generate_multi_frequency_signal(duration=duration, fs=fs)
    
    # 计算 FFT
    print("🔄 正在计算 FFT...")
    fft_freq, fft_mag = compute_fft(signal_raw, fs)
    
    # 计算功率谱密度
    print("🔄 正在计算功率谱密度...")
    psd_freq, psd = compute_power_spectrum(signal_raw, fs)
    
    # 带通滤波
    print("🔄 正在进行带通滤波（80-150 Hz）...")
    signal_filtered = apply_bandpass(signal_raw, fs, 80, 150)
    
    # 找主频
    peak_indices = signal.find_peaks(fft_mag, height=0.1, distance=10)[0]
    main_freqs = fft_freq[peak_indices]
    main_amps = fft_mag[peak_indices]
    
    print(f"\n📈 检测到的主频成分:")
    for i, (freq, amp) in enumerate(zip(main_freqs[:5], main_amps[:5])):
        if freq < 300:
            print(f"   {i+1}. {freq:.1f} Hz, 幅值: {amp:.3f}")
    
    # 可视化
    print("\n📊 正在生成可视化图表...")
    plot_results(t, signal_raw, signal_filtered, fft_freq, fft_mag, psd_freq, psd)
    
    print("\n" + "=" * 50)
    print("✅ Demo 运行完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()