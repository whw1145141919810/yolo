# RoboMaster 装甲板关键点推理

使用 Ultralytics YOLO 对本地视频或图片做姿态估计，输出装甲板检测框和关键点。项目示例权重为 YOLO26n-pose，可识别 B1、B2、B3、R1、R2、R3 六类装甲板，每个装甲板输出四个关键点。

## 快速开始

从仓库根目录执行。以下命令适用于 Windows PowerShell，原项目环境使用 Python 3.13.15。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

向社团获取原始权重 `best.pt`，放在 `weights/best.pt`。使用自己的本地视频或图片替换下面的路径。

```powershell
.\.venv\Scripts\python.exe mypredict.py "videos\armor.mp4"
```

脚本默认用 CPU，逐帧读取和保存，运行结束后打印实际输出目录。默认输出在 `runs/pose/predict*/`。

## 使用 NVIDIA GPU

原项目使用 RTX 5060 Laptop GPU 和 CUDA 13.0 构建的 PyTorch。按显卡和驱动选择 PyTorch 安装包。使用相同环境时，可以在安装 `requirements.txt` 前执行以下命令。

```powershell
.\.venv\Scripts\python.exe -m pip install torch==2.14.1+cu130 torchvision==0.29.1+cu130 --index-url https://download.pytorch.org/whl/cu130
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe mypredict.py "videos\armor.mp4" --device 0
```

## 常用参数

| 参数 | 说明 |
| --- | --- |
| `--model` | 自定义本地 `.pt` 权重路径 |
| `--device` | `cpu` 或 GPU 编号，如 `0` |
| `--imgsz` | 推理输入尺寸，默认 640 |
| `--conf` | 置信度阈值，默认 0.25 |
| `--project` | 自定义结果目录 |
| `--show` | 打开窗口显示推理过程 |

将模型导出到 ONNX、试跑导出的模型，或在同一视频上比较两个格式的表现，见 [yolo-export](https://github.com/whw1145141919810/yolo-export)。

## 推理示例

原始演示为约 13 秒的装甲板视频，拍摄时绕装甲板一圈。

<img width="360" alt="装甲板姿态推理结果，显示检测框与关键点" src="https://github.com/user-attachments/assets/d7a6aa49-3291-4257-b480-7bfbf8a24ea3" />
