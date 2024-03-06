TO RUN THE CODE:

1. extract the model:
step 1: cd models
step 2: wget -O 21styles.model https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer/releases/download/v0.1/21styles.model
step 3: cd ..

2. run the camera_demo, specify the model and disable cuda:

python camera_demo.py demo --model models/21styles.model --cuda=0
