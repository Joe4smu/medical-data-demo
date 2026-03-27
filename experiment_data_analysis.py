"""
实验数据自动化处理 Demo
展示：批量读取数据、统计分析、自动报告生成
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_sample_data(n_samples=50):
    """
    生成模拟实验数据
    模拟：多组实验测量结果
    """
    np.random.seed(42)
    
    data = {
        '实验组': [],
        '测量值1': [],
        '测量值2': [],
        '测量值3': [],
        '温度': [],
        '时间戳': []
    }
    
    for i in range(n_samples):
        group = f"Group_{i % 5 + 1}"
        # 模拟测量值（带噪声）
        base_value = 100 + (i % 5) * 10
        data['实验组'].append(group)
        data['测量值1'].append(base_value + np.random.randn() * 5)
        data['测量值2'].append(base_value * 0.8 + np.random.randn() * 3)
        data['测量值3'].append(base_value * 1.2 + np.random.randn() * 4)
        data['温度'].append(25 + np.random.randn() * 2)
        data['时间戳'].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    return pd.DataFrame(data)

def calculate_statistics(df):
    """
    计算统计量
    """
    stats = {}
    
    for col in ['测量值1', '测量值2', '测量值3']:
        stats[col] = {
            '均值': df[col].mean(),
            '标准差': df[col].std(),
            '最大值': df[col].max(),
            '最小值': df[col].min(),
            '变异系数': df[col].std() / df[col].mean() * 100
        }
    
    return pd.DataFrame(stats).T

def group_analysis(df):
    """
    分组分析
    """
    return df.groupby('实验组').agg({
        '测量值1': ['mean', 'std'],
        '测量值2': ['mean', 'std'],
        '测量值3': ['mean', 'std']
    }).round(2)

def plot_results(df, stats_df):
    """
    可视化结果
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 箱线图
    df.boxplot(column=['测量值1', '测量值2', '测量值3'], ax=axes[0, 0])
    axes[0, 0].set_title('测量值分布（箱线图）')
    axes[0, 0].set_ylabel('数值')
    
    # 分组均值
    group_means = df.groupby('实验组')[['测量值1', '测量值2', '测量值3']].mean()
    group_means.plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('各组均值对比')
    axes[0, 1].set_xlabel('实验组')
    axes[0, 1].set_ylabel('均值')
    axes[0, 1].legend(loc='upper right')
    
    # 散点图
    axes[1, 0].scatter(df['测量值1'], df['测量值2'], alpha=0.6, c='blue')
    axes[1, 0].set_xlabel('测量值1')
    axes[1, 0].set_ylabel('测量值2')
    axes[1, 0].set_title('测量值1 vs 测量值2')
    
    # 直方图
    axes[1, 1].hist(df['测量值1'], bins=20, alpha=0.7, label='测量值1')
    axes[1, 1].hist(df['测量值2'], bins=20, alpha=0.7, label='测量值2')
    axes[1, 1].set_xlabel('数值')
    axes[1, 1].set_ylabel('频数')
    axes[1, 1].set_title('数值分布直方图')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig('experiment_results.png', dpi=150)
    plt.show()
    
    print(f"\n✅ 结果已保存到 experiment_results.png")

def generate_report(df, stats_df, group_stats):
    """
    生成分析报告
    """
    report = f"""
{'='*60}
实验数据分析报告
{'='*60}

生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

一、数据概览
{'-'*40}
- 总样本数: {len(df)}
- 实验组数: {df['实验组'].nunique()}
- 数据列数: {len(df.columns)}

二、统计摘要
{'-'*40}
{stats_df.to_string()}

三、分组分析
{'-'*40}
{group_stats.to_string()}

四、结论
{'-'*40}
1. 测量值1 的变异系数为 {stats_df.loc['测量值1', '变异系数']:.2f}%
2. 测量值2 的变异系数为 {stats_df.loc['测量值2', '变异系数']:.2f}%
3. 测量值3 的变异系数为 {stats_df.loc['测量值3', '变异系数']:.2f}%

{'='*60}
"""
    
    with open('analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(report)
    print("✅ 报告已保存到 analysis_report.txt")

def main():
    print("=" * 50)
    print("实验数据自动化处理 Demo")
    print("=" * 50)
    
    # 生成模拟数据
    print("\n🔄 正在生成模拟实验数据...")
    df = generate_sample_data(n_samples=50)
    
    # 保存原始数据
    df.to_csv('experiment_data.csv', index=False, encoding='utf-8')
    print("✅ 原始数据已保存到 experiment_data.csv")
    
    # 计算统计量
    print("\n📊 正在计算统计量...")
    stats_df = calculate_statistics(df)
    
    # 分组分析
    print("📊 正在进行分组分析...")
    group_stats = group_analysis(df)
    
    # 可视化
    print("\n📊 正在生成可视化图表...")
    plot_results(df, stats_df)
    
    # 生成报告
    print("\n📝 正在生成分析报告...")
    generate_report(df, stats_df, group_stats)
    
    print("\n" + "=" * 50)
    print("✅ Demo 运行完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()