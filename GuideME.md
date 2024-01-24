# creating the enviornment with conda and installing dependencies

```
conda create -n dev python==3.9.16
conda activate dev
pip install -r requirements.txt
```

# Run Main.py to predict on images in Words directory

### To train the model with pretrained weights Run the Dev_Model_loading.ipynb file and save the model in the same directory.
### Then run Main_v2.py file to predicts with pretrained weights.