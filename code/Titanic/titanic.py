# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
train_data = pd.read_csv('train.csv')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def analyze_survival_rates():
    """分析不同特征的生还率"""
    plt.figure(figsize=(15, 10))

    # 1. 总体生还率
    plt.subplot(231)
    total_survival = pd.Series([1 - train_data['Survived'].mean(), train_data['Survived'].mean()])
    total_survival.plot(kind='pie', labels=['遇难', '生还'], autopct='%.1f%%', colors=['lightcoral', 'lightgreen'])
    plt.title('总体生还率')

    # 2. 性别与生还率 
    plt.subplot(232)
    survival_by_sex = train_data.groupby('Sex')['Survived'].mean()
    ax = survival_by_sex.plot(kind='barh', color=['lightcoral', 'lightgreen'])
    plt.title('不同性别生还率')
    plt.xlabel('生还率')
    plt.ylabel('性别')
    for i, v in enumerate(survival_by_sex):
        ax.text(v, i, f'{v:.1%}', ha='left', va='center')

    # 3. 年龄段与生还率
    plt.subplot(233)
    train_data['AgeGroup'] = pd.cut(train_data['Age'],
                                    bins=[0, 12, 18, 35, 50, 100],
                                    labels=['儿童', '青少年', '青年', '中年', '老年'])
    survival_by_age = train_data.groupby('AgeGroup', observed=True)['Survived'].mean()
    survival_by_age.plot(kind='bar', color='lightblue')
    plt.title('不同年龄段生还率')
    plt.xlabel('年龄段')
    plt.ylabel('生还率')
    plt.xticks(rotation=45)
    for i, v in enumerate(survival_by_age):
        plt.text(i, v, f'{v:.1%}', ha='center', va='bottom')

    # 4. 登船港口与生还率
    plt.subplot(234)
    survival_by_port = train_data.groupby('Embarked')['Survived'].mean()
    survival_by_port.plot(kind='bar', color='lightgreen')
    plt.title('不同登船港口生还率')
    plt.xlabel('登船港口(C=瑟堡,Q=皇后镇,S=南安普顿)')
    plt.ylabel('生还率')
    for i, v in enumerate(survival_by_port):
        plt.text(i, v, f'{v:.1%}', ha='center', va='bottom')

    # 5. 船舱等级与生还率
    plt.subplot(235)
    survival_by_class = train_data.groupby('Pclass')['Survived'].mean()
    survival_by_class.plot(kind='bar', color=['gold', 'silver', 'brown'])
    plt.title('不同船舱等级生还率')
    plt.xlabel('船舱等级')
    plt.ylabel('生还率')
    for i, v in enumerate(survival_by_class):
        plt.text(i, v, f'{v:.1%}', ha='center', va='bottom')

    # 6. 票价与生还率的散点图
    plt.subplot(236)
    fare_bins = pd.qcut(train_data['Fare'], q=20)  # 将票价分成20组
    fare_survival = train_data.groupby(fare_bins, observed=True)['Survived'].mean()
    # 获取每组的中间票价值
    fare_midpoints = train_data.groupby(fare_bins, observed=True)['Fare'].mean()

    plt.scatter(fare_midpoints, fare_survival,
               c='lightblue', alpha=0.6, s=100)
    plt.title('票价与生还率关系')
    plt.xlabel('票价(英镑)')
    plt.ylabel('生还率')

    z = np.polyfit(fare_midpoints, fare_survival, 1)
    p = np.poly1d(z)
    plt.plot(fare_midpoints, p(fare_midpoints), "r--", alpha=0.8)

    plt.tight_layout()
    plt.savefig('survival_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()


def print_survival_statistics():
    print("\n=== 泰坦尼克号生还率统计 ===")

    print(f"\n总体生还率: {train_data['Survived'].mean():.1%}")

    print("\n各性别生还率:")
    print(train_data.groupby('Sex')['Survived'].mean().apply(lambda x: f"{x:.1%}"))

    print("\n各年龄段生还率:")
    age_survival = train_data.groupby('AgeGroup', observed=True)['Survived'].mean()
    print(age_survival.apply(lambda x: f"{x:.1%}"))

    print("\n各登船港口生还率:")
    port_survival = train_data.groupby('Embarked')['Survived'].mean()
    print(port_survival.apply(lambda x: f"{x:.1%}"))

    print("\n各船舱等级生还率:")
    class_survival = train_data.groupby('Pclass')['Survived'].mean()
    print(class_survival.apply(lambda x: f"{x:.1%}"))

    print("\n票价统计:")
    print(f"生还者平均票价: £{train_data[train_data['Survived'] == 1]['Fare'].mean():.1f}")
    print(f"遇难者平均票价: £{train_data[train_data['Survived'] == 0]['Fare'].mean():.1f}")


if __name__ == "__main__":
    analyze_survival_rates()
    print_survival_statistics()
