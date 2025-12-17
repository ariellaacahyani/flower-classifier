# 🌸 Fastai Flower Classifier

This repository contains the code for a deep learning model that classifies images of flowers into 5 categories: Daisy, Dandelion, Rose, Sunflower, and Tulip.

## 🚀 Live Demo

A live, interactive demo of this model is deployed on Hugging Face Spaces.
**[TRY THE LIVE DEMO HERE](https://huggingface.co/spaces/riells/fastai_flower_classifier)**

---

## About This Project

This project demonstrates an end-to-end computer vision workflow. The model was built using `fastai` (on PyTorch) and is served via a `Gradio` web application.

### Tech Stack
* **Model:** `fastai` (built on `PyTorch`)
* **Web App:** `Gradio`
* **Deployment:** `Hugging Face Spaces` & `Git LFS`

### Key Files
* `flower_classifier.ipynb`: The Jupyter Notebook containing the full process: data loading, augmentation, model training, and evaluation.
* `app.py`: The Gradio application script used by Hugging Face to run the demo.
* `requirements.txt`: Required Python libraries.

### Note on Model File
The trained model file (`model.pth` or `.pkl`) is **not** included in this repository due to its large size. It is managed using **Git LFS** and is part of the Hugging Face Spaces deployment. To generate the model, you must run the `flower_classifier.ipynb` notebook.

