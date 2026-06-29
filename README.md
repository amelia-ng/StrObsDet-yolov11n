# Street Obstacle Detection using YOLOv11n
View HuggingFace interface: https://huggingface.co/spaces/ameliang/street-obstacle-detection


**Model did pretty well on random images from Google** Although, it cannot detect all objects and blurry objects as well as RT-DETR. [Repo for RT-DETR]([url](https://github.com/amelia-ng/RT-DETR-street-obstacles-detection/tree/main))


<img width="1526" height="623" alt="image" src="https://github.com/user-attachments/assets/e543c91c-307f-4312-a36e-9e8835e6637d" />

<img width="1593" height="890" alt="image" src="https://github.com/user-attachments/assets/e17b2e84-9a1b-40ff-b452-a90568479a12" />

The model still misses out several objects in some photos:
<img width="1698" height="870" alt="image" src="https://github.com/user-attachments/assets/0010b691-6a66-4c80-b3cf-98e1dfd9a6bc" />


Model Evaluation:
- mAP50_95: 0.75
- mAP50: 0.897
- precision: 0.92
- recall: 0.88

Training curves do not show signs of overfitting
<img width="1491" height="715" alt="image" src="https://github.com/user-attachments/assets/cbcf48e7-4988-488f-ad07-34c353cbe6b4" />
The confusion matrix shows a rare correlation between the mismatched classes
<img width="1016" height="790" alt="image" src="https://github.com/user-attachments/assets/35c0b8a6-37b5-4672-9d64-e58f06788083" />


