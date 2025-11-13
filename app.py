import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner('flower.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),  
    title="Flowers Classifier",
    description="A Flower classifier trained on Kaggle dataset with fastai.",
    article = "<p style='text-align: center'><a href='https://github.com/ariellaacahyani' target='_blank'>My GitHub</a></p>"
    )

interface.launch(share=True)