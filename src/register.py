import os
from argparse import ArgumentParser

from src.base import Data
from src.constant import constant
from src.utils.utils import MyDict

all_tools = MyDict()
wait_flush_require = MyDict()

root_parser = ArgumentParser(description='获取图表')
sub_parser = root_parser.add_subparsers()
sub_parser.required = True


def register(cls: Data):
    if cls.data_type in all_tools:
        raise ValueError(f"{cls.data_type}-已经存在！")
    all_tools[cls.data_type] = cls
    if getattr(cls, "add_arguments", None):
        cls.add_arguments(sub_parser)

    return cls


def require(require_name):
    def wrap(cls: Data):
        if constant.require_key in cls.__dict__:
            _require = cls.__dict__[constant.require_key]
        else:
            _require = {}
        if require_name in _require:
            raise ValueError(f"{require_name}-已经被{cls}引用")
        require_source = all_tools.get(require_name)
        if require_source:
            _require[require_name] = require_source
        else:
            wait_flush_require[cls] = [require_name]
        setattr(cls, constant.require_key, _require)
        return cls

    return wrap


def parse_tools():
    for f_name in os.listdir(constant.tools_dir):
        next_path = os.path.join(constant.tools_dir, f_name)
        if not os.path.isdir(next_path):
            continue
        if f_name == '__pycache__':
            continue
        if not os.path.exists(os.path.join(next_path, "__init__.py")):
            continue
        for ff_name in os.listdir(next_path):
            if ff_name.endswith('.py'):
                module_name = f"src.all_tools.{f_name}.{ff_name[0:-3]}"
                __import__(module_name)


def repair_requires():
    for cls, requires in wait_flush_require.items():
        cls_require = getattr(cls, constant.require_key, {})
        for require_name in requires:
            if require_name in cls_require:
                raise ValueError(f"{require_name}-已经被{cls}引用")
            data_type = all_tools[require_name]
            cls_require[require_name] = data_type
            setattr(cls, constant.require_key, cls_require)


def load_all_tools():
    parse_tools()
    repair_requires()
    all_tools.clean()
    wait_flush_require.clean()
