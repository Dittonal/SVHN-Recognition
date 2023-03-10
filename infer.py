"""
测试结果并保存
"""

import argparse
import torch
from PIL import Image
from torchvision import transforms
from model import Model
import warnings
import os
import csv
warnings.filterwarnings("ignore")


# 参数设置
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--checkpoint', type=str, default='logs\\model-122000.pth',
                    help='path to checkpoint, e.g. ./logs/model-100.pth')
parser.add_argument('-i', '--input', type=str,
                    default='data\\test\\', help='path to input image')


# 测试函数
def _infer(path_to_checkpoint_file, path_to_input_image):
    model = Model()
    model.restore(path_to_checkpoint_file)
    # model.cuda()

    with torch.no_grad():
        transform = transforms.Compose([
            transforms.Resize([64, 64]),
            transforms.CenterCrop([54, 54]),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

        # 创建文件对象
        f = open('test.csv', 'w', encoding='utf-8', newline='') 
        # 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 构建列表头
        csv_writer.writerow(["file_name", "house_number"])

        image_files = os.listdir(path_to_input_image)
        for file in image_files:
            image = Image.open(path_to_input_image+file)
            image = image.convert('RGB')
            image = transform(image)
            images = image.unsqueeze(dim=0)
            # images = image.unsqueeze(dim=0).cuda()

            length_logits, digit1_logits, digit2_logits, digit3_logits, digit4_logits, digit5_logits = model.eval()(images)

            length_prediction = length_logits.max(1)[1]
            digit1_prediction = digit1_logits.max(1)[1]
            digit2_prediction = digit2_logits.max(1)[1]
            digit3_prediction = digit3_logits.max(1)[1]
            digit4_prediction = digit4_logits.max(1)[1]
            digit5_prediction = digit5_logits.max(1)[1]

            output = [digit1_prediction.item(), digit2_prediction.item(),
                      digit3_prediction.item(), digit4_prediction.item(), digit5_prediction.item()]

            outstr = ''

            for i in range(length_prediction.item()):
                outstr += str(output[i])

            print(f"文件名：{file}\t结果：{outstr}")
            csv_writer.writerow([file, outstr]) # 写入csv文件



            # print('length:', length_prediction.item())
            # print('digits:', digit1_prediction.item(), digit2_prediction.item(
            # ), digit3_prediction.item(), digit4_prediction.item(), digit5_prediction.item())


def main(args):
    path_to_checkpoint_file = args.checkpoint
    path_to_input_image = args.input

    _infer(path_to_checkpoint_file, path_to_input_image)


if __name__ == '__main__':
    main(parser.parse_args())
