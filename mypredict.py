"""Run RoboMaster armor plate pose inference on local media."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description="对本地视频、图片或目录运行装甲板关键点推理")
    parser.add_argument("source", type=Path, help="输入视频、图片或目录")
    parser.add_argument("--model", type=Path, default=ROOT / "weights" / "best.pt", help="PyTorch 权重")
    parser.add_argument("--device", default="cpu", help="cpu 或 CUDA GPU 编号，例如 0")
    parser.add_argument("--imgsz", type=int, default=640, help="推理输入尺寸")
    parser.add_argument("--conf", type=float, default=0.25, help="置信度阈值")
    parser.add_argument("--project", type=Path, default=ROOT / "runs" / "pose", help="输出目录")
    parser.add_argument("--show", action="store_true", help="实时显示推理结果")
    args = parser.parse_args()
    if not args.source.exists():
        parser.error(f"输入路径不存在：{args.source}")
    if args.model.suffix.lower() != ".pt" or not args.model.is_file():
        parser.error(f"找不到 .pt 权重：{args.model}，请放入 weights/best.pt 或传入 --model")
    if args.imgsz <= 0 or not 0 <= args.conf <= 1:
        parser.error("--imgsz 必须大于 0，--conf 必须在 0 到 1 之间")

    from ultralytics import YOLO

    model = YOLO(str(args.model.resolve()))
    results = model.predict(
        source=str(args.source.resolve()),
        device=args.device,
        imgsz=args.imgsz,
        conf=args.conf,
        stream=True,
        save=True,
        show=args.show,
        project=str(args.project.resolve()),
        name="predict",
        verbose=False,
    )
    frames = sum(1 for _ in results)
    if not frames:
        parser.exit(1, "输入中没有可处理的图像或视频帧。\n")
    print(f"已处理 {frames} 张图像或视频帧。结果目录：{model.predictor.save_dir}")


if __name__ == "__main__":
    main()
