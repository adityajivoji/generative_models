from main.main import main
from loader import loader

batch_size = 64
num_epochs = 10
training_data = loader.trainLoader(batch_size)
testing_data = loader.testLoader(batch_size)
main()