import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


# 数据
models = ['M1', 'M2', 'M3']
in_domain_scores = [66.1, 66.3, 66.4]
out_domain_scores = [52.5, 54.3, 55.5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 分别为每个柱子设置颜色
hatches = ['/', '\\', 'x']  # 不同的纹理以区分柱子

legend_labels = [
    'RankLLaMA',
    'LLaMA+Lrank',
    'LLaMA+CPT+Lrank'
]


# 创建图形和两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

bar_width = 0.6  # 减小柱子宽度

# 子图1: in-domain
for i, (model, score) in enumerate(zip(models, in_domain_scores)):
    rect = ax1.bar(model, score, color='white', edgecolor=colors[i], hatch=hatches[i], width=bar_width, label=legend_labels[i])
    ax1.text(i, score + 0.01, f'{score:.1f}', ha='center', va='bottom', fontsize=20)  # 显示柱子上方的数字
ax1.set_xlabel('(a) In-domain', fontsize=20)
ax1.set_ylim(66.0, 66.5)

ax1.tick_params(axis='y', labelsize=20)  # 设置纵坐标数字的字号
ax1.set_xticks([])  # 去除x轴的刻度标签

# 子图2: out-domain
for i, (model, score) in enumerate(zip(models, out_domain_scores)):
    rect = ax2.bar(model, score, color='white', edgecolor=colors[i], hatch=hatches[i], width=bar_width, label=legend_labels[i])
    ax2.text(i, score + 0.01, f'{score:.1f}', ha='center', va='bottom', fontsize=20)  # 显示柱子上方的数字
ax2.set_xlabel('(b) Out-domain', fontsize=20)
ax2.set_ylim(52.0, 56.0)

ax2.tick_params(axis='y', labelsize=20)  # 设置纵坐标数字的字号
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 设置刻度间隔为1

ax2.set_xticks([])  # 去除x轴的刻度标签

# # 为第二个柱子添加图例
handles, labels = ax1.get_legend_handles_labels()
lgd = fig.legend(handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=3, fontsize=20)
lgd.get_frame().set_linewidth(0.0)
plt.rc('font', family='serif', serif='Times New Roman')
# 显示图形
fig.subplots_adjust(top=0.85, bottom=0.15, left=0.1, right=0.9)


# 自定义图例句柄
# legend_elements = [
#     Line2D([0], [0], color='white', lw=4, label='Long Bar', marker='s', markerfacecolor='gray', markersize=15),
#     Line2D([0], [0], color='white', lw=2, label='Short Bar', marker='s', markerfacecolor='gray', markersize=8)
# ]

# # 为整个图形添加图例，并放置在顶部中间
# lgd = fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2, fontsize=20)

# # 调整布局以适应图例和子图标题
# fig.subplots_adjust(top=0.85, bottom=0.15, left=0.1, right=0.9)


plt.show()

# 保存图像，应在调用show()之前完成
plt.savefig('model_performance.pdf', bbox_inches='tight')
