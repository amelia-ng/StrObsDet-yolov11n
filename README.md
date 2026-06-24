# Street Obstacle Detection using YOLOv11n

Trained and Fine-tuned YOLOv11n on Kaggle's ROD data, then deployed it into a HuggingFace app.

Check out the app interface at: https://huggingface.co/spaces/ameliang/street-obstacle-detection

Model Evaluation:
--
mAP50_95: 0.75
mAP50: 0.897
precision: 0.92
recall: 0.88
--
Training curves do not show signs of overfitting
<img width="1491" height="715" alt="image" src="https://github.com/user-attachments/assets/cbcf48e7-4988-488f-ad07-34c353cbe6b4" />
The confusion matrix shows rare correlation between mismatched class
<img width="1016" height="790" alt="image" src="https://github.com/user-attachments/assets/35c0b8a6-37b5-4672-9d64-e58f06788083" />

**Model did pretty well on random images from Google**
<img width="1539" height="608" alt="image" src="https://github.com/user-attachments/assets/f1d592c3-4e6d-4724-be17-97398c51bca7" />
<img width="1554" height="677" alt="image" src="https://github.com/user-attachments/assets/94497f5b-9da0-4fc5-af89-c5744199e0e2" />
The model still misses out several objects in unseen photos:
<img width="1539" height="447" alt="image" src="https://github.com/user-attachments/assets/053f2d82-2655-479c-80c7-afbc88dfc059" />

