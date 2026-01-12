#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
桌面应用安装配置文件
"""

from setuptools import setup, find_packages
import os

# 获取当前目录
here = os.path.abspath(os.path.dirname(__file__))

# 读取README文件
with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

# 读取requirements.txt文件
with open(os.path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='zerophone-desktop',
    version='0.1.0',
    description='智能体屏幕监控与控制中心桌面应用',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='KLJyouth1',
    author_email='your.email@example.com',
    url='https://github.com/KLJyouth1/zerophone',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'zerophone-desktop=app:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/KLJyouth1/zerophone/issues',
        'Source': 'https://github.com/KLJyouth1/zerophone',
    },
    keywords='desktop app, agent, screen monitoring, automation',
)
