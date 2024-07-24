# 听说剪映收费了？
## 第一步 - 配置环境
1、在Anaconda里面新建一个环境，名字叫ai；

2、在ai环境下安装以下依赖：

GPU：

`pip install torch==2.3.0+cu121 torchvision==0.18.0+cu121 torchaudio==2.3.0+cu121 -f https://download.pytorch.org/whl/cu121/torch_stable.html -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn`

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn PySide6==6.6.3.1`

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn moviepy`

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn whisperx`

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn pysrt`

FFMPEG：

https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z

配置好系统 PATH 环境变量： C:\Program Files\ffmpeg\bin

3、启动！

`launcher.py`