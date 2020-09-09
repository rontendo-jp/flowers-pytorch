import argparse
from mymodel import MyModel

parser = argparse.ArgumentParser(description='Flower Image Trainer')

parser.add_argument('data_directory', action='store', type=str, help='data directory for training, validation, and test')
parser.add_argument('--gpu', action='store_true', help='use gpu, if not specified, will use cpu', default=False)
parser.add_argument('--arch', action='store', type=str, help='base model architechture. Currently only support vgg16 or vgg11', default="vgg16")
parser.add_argument('--epochs', action='store', type=int, help='how many epochs to train', default=1)
parser.add_argument('--learning_rate', action='store', type=float, help='learning rate', default=0.01)
parser.add_argument('--hidden_units', action='store', type=int, help='hidden unit', default=4096)
parser.add_argument('--save_dir', action='store', type=str, help='save model into file')

args = parser.parse_args()

print(args)

# mm = MyModel(use_gpu=args.gpu)
# model = mm.create_model(base_model=args.arch, hidden_unit_num=args.hidden_units)
# optimizer = mm.create_optimizer(model, learning_rate=args.learning_rate)
# mm.train_model(model, optimizer, epoch=args.epochs)