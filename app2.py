# app.py
import torch
import torch.nn as nn
from torchvision import models, transforms
from flask import Flask, jsonify, request, render_template
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import cv2
import torch

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html");

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=3001, debug=True)
