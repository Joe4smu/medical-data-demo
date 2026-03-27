# Medical Data Processing Demo

一个全面的医学/生物医学数据处理示例项目集合，展示 Python 在医学数据分析中的多种应用场景。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 项目概览

| Demo | 文件 | 展示能力 |
|------|------|---------|
| 心电图处理 | `ecg_processing.py` | 信号处理、R波检测、心率分析 |
| 医学图像处理 | `medical_image_processing.py` | 图像滤波、边缘检测、分割 |
| 实验数据分析 | `experiment_data_analysis.py` | 批量数据处理、统计报告 |
| 频谱分析 | `spectrum_analysis.py` | FFT、功率谱密度、时频分析 |

---

## 📊 Demo 预览

### 1. ECG 心电图处理

展示医学信号处理的完整流程：

- 模拟 ECG 信号生成（心率 75 bpm）
- 带通滤波（0.5-45 Hz）
- R 波自动检测
- 心率计算

**核心代码：**
```python
# 带通滤波
ecg_filtered = bandpass_filter(ecg_raw, fs, lowcut=0.5, highcut=45)

# R 波检测
r_peaks = detect_r_peaks(ecg_filtered, fs)

# 计算心率
heart_rate = 60 / np.mean(rr_intervals)  # 结果: 75 bpm
```

---

### 2. 医学图像处理

展示 CT/MRI 图像的预处理流程：

- 模拟 CT 图像生成（含噪声）
- 高斯滤波去噪
- Sobel 边缘检测
- 阈值分割

**核心代码：**
```python
# 高斯滤波
filtered = ndimage.gaussian_filter(image, sigma=2)

# 边缘检测
edges = ndimage.sobel(filtered)

# 阈值分割
segmented = (filtered > 0.5).astype(float)
```

---

### 3. 实验数据自动化

展示批量实验数据处理：

- 批量数据读取（CSV/Excel）
- 统计分析（均值、标准差、变异系数）
- 分组分析
- 自动报告生成

**核心代码：**
```python
# 统计分析
stats = df.groupby('实验组').agg({
    '测量值1': ['mean', 'std'],
    '测量值2': ['mean', 'std']
})

# 生成报告
generate_report(df, stats_df, group_stats)
```

**输出文件：**
- `experiment_data.csv` - 原始数据
- `experiment_results.png` - 可视化图表
- `analysis_report.txt` - 统计报告

---

### 4. 信号频谱分析

展示频域分析方法：

- 多频率信号生成（50/120/200 Hz）
- FFT 快速傅里叶变换
- 功率谱密度（Welch 方法）
- 时频谱图（Spectrogram）

**核心代码：**
```python
# FFT 变换
fft_result = np.fft.fft(signal_data)
fft_freq = np.fft.fftfreq(n, 1/fs)

# 功率谱密度
freqs, psd = signal.welch(signal_data, fs)

# 时频分析
f, t, Sxx = signal.spectrogram(signal_data, fs)
```

---

## 🛠️ 技术栈

| 库 | 用途 |
|---|------|
| NumPy | 数值计算 |
| SciPy | 科学计算、信号处理 |
| Matplotlib | 数据可视化 |
| Pandas | 数据处理、统计分析 |

---

## 🚀 快速开始

### 安装依赖

```bash
pip install numpy scipy matplotlib pandas
```

### 运行各个 Demo

```bash
# ECG 信号处理
python ecg_processing.py

# 医学图像处理
python medical_image_processing.py

# 实验数据分析
python experiment_data_analysis.py

# 频谱分析
python spectrum_analysis.py
```

---

## 💼 应用场景

本项目涵盖的技术可应用于：

- 🏥 医疗仪器数据分析
- 🧪 实验室数据处理自动化
- 💓 生物医学信号处理（ECG、EEG、EMG）
- 🖼️ 医学影像预处理
- 📡 传感器数据分析

---

## 📝 技术亮点

| 技术 | 说明 |
|------|------|
| 数字滤波 | Butterworth 带通滤波器设计 |
| 峰值检测 | 基于阈值的 R 波自动检测 |
| 图像处理 | 高斯滤波、Sobel 边缘检测、阈值分割 |
| 频域分析 | FFT、功率谱密度、时频分析 |
| 数据自动化 | 批量处理、自动报告生成 |

---

## 👤 作者

**背景：** 生物医学工程 + 物理实验教师

**专注：** 医学数据处理、信号分析、自动化工具开发

---

## 📜 许可证

MIT License

---

欢迎 Star ⭐ 和 Fork！如有问题欢迎提 Issue。