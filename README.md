# Medical Data Processing Demo

一个全面的医学/生物医学数据处理示例项目集合，展示 Python 在医学数据分析中的多种应用场景。

## 🎯 项目概览

| Demo | 文件 | 展示能力 |
|------|------|---------|
| 心电图处理 | `ecg_processing.py` | 信号处理、R波检测、心率分析 |
| 医学图像处理 | `medical_image_processing.py` | 图像滤波、边缘检测、分割 |
| 实验数据分析 | `experiment_data_analysis.py` | 批量数据处理、统计报告 |
| 频谱分析 | `spectrum_analysis.py` | FFT、功率谱密度、时频分析 |

## 📊 功能演示

### 1. ECG 心电图处理
- ✅ 信号模拟生成
- ✅ 带通滤波（0.5-45 Hz）
- ✅ R 波自动检测
- ✅ 心率计算

### 2. 医学图像处理
- ✅ 模拟 CT 图像生成
- ✅ 高斯滤波去噪
- ✅ Sobel 边缘检测
- ✅ 阈值分割

### 3. 实验数据自动化
- ✅ 批量数据读取（CSV/Excel）
- ✅ 统计分析（均值、标准差、变异系数）
- ✅ 分组分析
- ✅ 自动报告生成

### 4. 信号频谱分析
- ✅ 多频率信号生成
- ✅ FFT 快速傅里叶变换
- ✅ 功率谱密度（Welch 方法）
- ✅ 时频谱图（Spectrogram）

## 🛠️ 技术栈

- Python 3.8+
- NumPy - 数值计算
- SciPy - 科学计算
- Matplotlib - 数据可视化
- Pandas - 数据处理

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

## 📁 输出文件

运行后会生成：
- `ecg_results.png` - ECG 处理结果图
- `medical_image_results.png` - 图像处理结果图
- `experiment_results.png` - 数据分析图表
- `experiment_data.csv` - 原始数据
- `analysis_report.txt` - 自动生成的统计报告
- `spectrum_results.png` - 频谱分析结果图

## 💼 应用场景

本项目涵盖的技术可应用于：

- 医疗仪器数据分析
- 实验室数据处理自动化
- 生物医学信号处理（ECG、EEG、EMG）
- 医学影像预处理
- 传感器数据分析

## 📝 许可证

MIT License

## 👤 作者

生物医学工程背景，专注于医学数据处理与分析。

欢迎 Star ⭐ 和 Fork！
