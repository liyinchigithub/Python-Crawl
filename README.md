# Python-Crawl

基于Slenium爬取城市天气信息生成echarts图表并写入数据库


# 一、安装依赖

## （一）创建虚拟目录

```shell
# python -m venv 虚拟环境名称，名称是随意起的
python -m venv tutorial-env
```
## （二）激活虚拟环境
当激活虚拟环境时命令行上会有个虚拟环境名前缀。

### 1.Unix或MacOS上激活虚拟环境
```shell
source tutorial-env/bin/activate
```

### 2.windows上激活虚拟环境
```shell
tutorial-env\Scripts\activate.bat
```

### 3.如果有新的依赖引入，冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```

### 4.安装requirement.txt依赖
```shell
pip install -r requirements.txt
```


# 二、运行程序

## （一）运行程序

### 1.pytset单元测试脚本启动方式

```shell
pytest -v ./src/main.py
```
