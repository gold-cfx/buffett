from matplotlib import pyplot as plt

from src import config


def common(x_label, y_label, title):
    pic_size = (config.pic.size_width, config.pic.size_height)
    plt.figure(figsize=pic_size)
    plt.xticks(rotation=45)
    plt.yticks(rotation=30)
    plt.xlabel(x_label) if x_label else 0
    plt.ylabel(y_label) if y_label else 0
    plt.title(title) if title else 0
    return plt


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
