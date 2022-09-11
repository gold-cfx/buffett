# buffett

- 根据金融/股票数据 定制化作图
- python3.10开发（建议3.6以上试用）

# 使用方法

## 根据需求修改配置

- 配置路径：`etc/buffett.conf`

## 使用命令行查看帮助文档

```shell
python main.py -h
```

```text
usage: main.py [-h] {new_share_group_day_plot_pic,new_share_group_day_bar_pic,new_share_group_mouth_plot_pic,new_share_group_mouth_bar_pic} ...

获取图表

positional arguments:
  {new_share_group_day_plot_pic,new_share_group_day_bar_pic,new_share_group_mouth_plot_pic,new_share_group_mouth_bar_pic}
    new_share_group_day_plot_pic
                        新股发行市值-按天统计-折线图
    new_share_group_day_bar_pic
                        新股发行市值-按天统计-柱状图
    new_share_group_mouth_plot_pic
                        新股发行市值-按月统计-折线图
    new_share_group_mouth_bar_pic
                        新股发行市值-按月统计-柱状图

options:
  -h, --help            show this help message and exit

```

```shell
python main.py new_share_group_day_plot_pic -h
```

```text
usage: main.py new_share_group_day_plot_pic [-h] -s start_date -e end_date

options:
  -h, --help     show this help message and exit
  -s start_date  开始日期 样例：20221012
  -e end_date    结束日期 样例：20221012

```

## 执行命令样例

```shell
python main.py new_share_group_day_plot_pic -s 20210101 -e 20221231
python main.py new_share_group_day_bar_pic -s 20210101 -e 20221231
python main.py new_share_group_mouth_bar_pic -s 20210101 -e 20221231
python main.py new_share_group_mouth_plot_pic -s 20210101 -e 20221231
```