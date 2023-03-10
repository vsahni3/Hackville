import matplotlib.pyplot as plt # for plotting
from PIL import Image
import numpy as np # for transformation
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import torch # PyTorch package
import torchvision # load datasets
import torchvision.transforms as transforms # transform data
import torch.nn as nn # basic building block for neural neteorks
import torch.nn.functional as F # import convolution functions like Relu
import torch.optim as optim # optimzer

# python image library of range [0, 1] 
# transform them to tensors of normalized range[-1, 1]
PATH = './cifar_net.pth'
transform = transforms.Compose( # composing several transforms together
    [transforms.ToTensor(), # to tensor object
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]) # mean = 0.5, std = 0.5

# set batch_size
batch_size = 4

# set number of workers
num_workers = 2

# load train data
trainset = torchvision.datasets.CIFAR100(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=num_workers)

# load test data
testset = torchvision.datasets.CIFAR100(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

# put 100 classes into a set
classes = (
    "apple", "aquarium fish", "baby", "bear", "beaver", "bed", "bee",
    "beetle", "bicycle", "bottle", "bowl", "boy", "bridge", "bus",
    "butterfly", "camel", "can", "castle", "caterpillar", "cattle",
    "chair", "chimpanzee", "clock", "cloud", "cockroach", "couch",
    "crab", "crocodile", "cup", "dinosaur", "dolphin", "elephant",
    "flatfish", "forest", "fox", "girl", "hamster", "house", "kangaroo",
    "computer keyboard", "lamp", "lawn-mower", "leopard", "lion",
    "lizard", "lobster", "man", "maple tree", "motorcycle", "mountain",
    "mouse", "mushroom", "oak tree", "orange", "orchid", "otter",
    "palm tree", "pear", "pickup truck", "pine tree", "plain", "plate",
    "poppy", "porcupine", "possum", "rabbit", "raccoon", "ray", "road",
    "rocket", "rose", "sea", "seal", "shark", "shrew", "skunk", "skyscraper",
    "snail", "snake", "spider", "squirrel", "streetcar", "sunflower",
    "sweet pepper", "table", "tank", "telephone", "television", "tiger",
    "tractor", "train", "trout", "tulip", "turtle", "wardrobe", "whale",
    "willow tree", "wolf", "woman", "worm"
)


def imshow(img):
  ''' function to show image '''
  img = img / 2 + 0.5 # unnormalize
  npimg = img.numpy() # convert to numpy objects
  plt.imshow(np.transpose(npimg, (1, 2, 0)))
  plt.show()

# get random training images with iter function
dataiter = iter(trainloader)
images, labels = dataiter.__next__()


class Net(nn.Module):
    ''' Models a simple Convolutional Neural Network'''
	
    def __init__(self):
        ''' initialize the network '''
        super(Net, self).__init__()
        # 3 input image channel, 6 output channels, 
        # 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(3, 6, 5)
        # Max pooling over a (2, 2) window
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5) 
        self.fc1 = nn.Linear(16 * 5 * 5, 120) # 5x5 from image dimension
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 100)

    def forward(self, x):
        ''' the forward propagation algorithm '''
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def train():

    net = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

def testing():
    dataiter = iter(testloader)
    images, labels = dataiter.__next__()
    imshow(torchvision.utils.make_grid(images))
    print('GroundTruth: ', ' '.join('%s' % classes[labels[j]] for j in range(4)))
    outputs = net(images)

    torch.save(net.state_dict(), PATH)
    dataiter = iter(testloader)
    images, labels = dataiter.__next__()
    print(images.shape)

def predict(image):
    img_resized = image.resize((32, 32))

    # Save the resized image

    tensor_image = transform(img_resized)
    list_tens = tensor_image.tolist()
    list_tens = [list_tens for i in range(4)]
    new_tensor_img = torch.FloatTensor(list_tens)
    print(new_tensor_img.shape)
    output = net(new_tensor_img)
    _, predicted = torch.max(output, 1)

    print('Predicted: ', ' '.join('%s' % classes[predicted[j]]
                                for j in range(4)))
    return [classes[predicted[j]] for j in range(4)]
