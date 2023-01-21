"""
训练可视化，绘制loss图
"""

import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

# 参数设置
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--logdir', default='logs',
                    help='directory to read logs')


# 绘图
def _visualize(path_to_log_dir):
    # 加载损失文件
    losses = np.load(os.path.join(path_to_log_dir, 'losses.npy'))
    plt.plot(losses)
    plt.xlabel('Step(k)')
    plt.ylabel('Loss')
    plt.savefig('images\\loss.png')
    plt.show()
    # viz = Visdom()
    # viz.line(losses)


def main(args):
    path_to_log_dir = args.logdir
    _visualize(path_to_log_dir)


if __name__ == '__main__':
    main(parser.parse_args())
