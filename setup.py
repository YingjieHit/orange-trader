from setuptools import setup, find_packages

setup(
    name='orange_trader',  # 库名
    version='0.0.1',  # 版本号
    packages=find_packages(),  # 包含的包
    install_requires=[  # 依赖项
        'numpy',
        'pandas',
        # 添加其他依赖
    ],
    author='Zhang Yingjie',  # 作者名
    author_email='yingjiehit@gmail.com',  # 作者邮箱
    description='A great HFT Trading project',  # 简要描述
    url='https://github.com/YingjieHit/orange-trader',  # 项目的URL
    keywords=['quantitative', 'trading', 'finance', 'HTF'],  # 关键词
)