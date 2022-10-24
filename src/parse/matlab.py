from matplotlib import pyplot as plt

from src import config
from src.constant import constant


def common(x_label, y_label, title):
    pic_size = (config.pic.size_width, config.pic.size_height)
    plt.figure(figsize=pic_size)
    plt.xticks(rotation=45)
    plt.yticks(rotation=30)
    plt.xlabel(x_label) if x_label else 0
    plt.ylabel(y_label) if y_label else 0
    plt.title(title) if title else 0
    return plt


def common_draw(df, x_col, y_info):
    draw_type = y_info.pop(constant.draw_type)
    if draw_type == constant.bar:
        for y_col, y_col_kw in y_info.items():
            plt.bar(df[x_col], df[y_col], **y_col_kw)
    elif draw_type == constant.plot:
        for y_col, y_col_kw in y_info.items():
            plt.plot(df[x_col], df[y_col], **y_col_kw)


def bar(df, x_col, y_col_info, x_label, y_label, title, **kwargs):
    common(x_label, y_label, title)
    for y_col, y_col_kw in y_col_info.items():
        plt.bar(df[x_col], df[y_col], **y_col_kw)
    return plt


def plot(df, x_col, y_col_info, x_label, y_label, title, **kwargs):
    common(x_label, y_label, title)
    for y_col, y_col_kw in y_col_info.items():
        plt.plot(df[x_col], df[y_col], **y_col_kw)
    return plt


def mix(df, x_col, y_col_info_list, x_label=None, y_label=None, title=None, **kwargs):
    common(x_label, y_label, title)
    count = len(y_col_info_list)
    for index, y_col_info in enumerate(y_col_info_list, start=1):
        plt.subplot(count, 1, index)  # 图一包含2行1列子图，当前画在第一行第一列图上
        common_draw(df, x_col, y_col_info)
    return plt
