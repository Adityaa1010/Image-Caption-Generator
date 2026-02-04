
# Image Caption Generator using CNN + LSTM

This project generates natural language captions for images using a
CNN–LSTM architecture with Greedy and Beam Search decoding.

## 🚀 Features
- InceptionV3 CNN for image feature extraction
- LSTM-based caption generation
- Greedy vs Beam Search decoding
- BLEU score evaluation with smoothing
- Visualization of predictions

## 🧠 Model Architecture
- CNN: InceptionV3 (pretrained, frozen)
- RNN: LSTM
- Decoder: Softmax over vocabulary

## 📊 Evaluation
- BLEU score (NLTK with smoothing)
- Comparison between Greedy and Beam Search

## 📁 Dataset
- Flickr8k / Flickr30k
- Captions format: `image_name\tcaption`

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

2.Train model
python src/train.py

3. Generate captions
python src/inference.py

4. Evaluate
python src/evaluation.py
