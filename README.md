# yolo
yolo装甲板视频推理
一、 项目完成功能：识别装甲板并标出关键点
二、 Python版本：3.13.15  主要依赖：Pytorch 2.14.1+cu130  使用GPU
三、 模型权重准备方式：社团提供  放置位置：weights
四、 依赖安装步骤：
       # 1) 建虚拟环境
       python -m venv .venv

       # 2) 升级基础工具
       .\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

       # 3) PyTorch 
       .\.venv\Scripts\python.exe -m pip install torch torchvision --index-url      https://download.pytorch.org/whl/cu130

       # 4) Ultralytics + 其他依赖
       .\.venv\Scripts\python.exe -m pip install -r requirements.txt

       # 5) 把配置/缓存目录固定到项目内
       #     .venv\Lib\site-packages\sitecustomize.py；用 install.ps1 会自动生成
  实际运行：pycharm
  结果保存位置：scripts\runs\pose
五、 视频拍摄地点：水建楼D404   时长：13秒   场景说明：围绕装甲板拍了一圈
六、 <img width="887" height="1920" alt="B5A5260E031351C93F702376CDB3CB42" src="https://github.com/user-attachments/assets/d7a6aa49-3291-4257-b480-7bfbf8a24ea3" />
