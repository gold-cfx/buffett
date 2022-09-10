import os

from src.base import Data
from src.constant import constant

all_plugin = {}
wait_flush_require = {}


def repair_requires():
    for cls, requires in wait_flush_require.items():
        cls_require = getattr(cls, constant.require_key, {})
        for require_name in requires:
            if require_name in cls_require:
                raise ValueError(f"{require_name}-已经被{cls}引用")
            data_type = all_plugin[require_name]
            cls_require[require_name] = data_type
            setattr(cls, constant.require_key, cls_require)


def register_plugin(cls: Data):
    if cls.data_type in all_plugin:
        raise ValueError(f"{cls.data_type}-已经存在！")
    all_plugin[cls.data_type] = cls
    return cls


def require_plugin(require_name):
    def require(cls: Data):
        if constant.require_key in cls.__dict__:
            _require = cls.__dict__[constant.require_key]
        else:
            _require = {}
        if require_name in _require:
            raise ValueError(f"{require_name}-已经被{cls}引用")
        require_source = all_plugin.get(require_name)
        if require_source:
            _require[require_name] = require_source
        else:
            wait_flush_require.setdefault(cls, []).append(require_name)
        setattr(cls, constant.require_key, _require)
        return cls

    return require


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
                __import__(f"src.all_tools.{f_name}.{ff_name[0:-3]}")


def load_all_driver():
    parse_tools()
    repair_requires()
