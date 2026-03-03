🛡️ Hybrid Deep Learning for Botnet Attack Detection in IoT Networks

🎓 Final Year Project
👩‍💻 S. Preethi
📅 2022–2023

📌 Project Overview

With the rapid growth of IoT devices, botnet attacks like DDoS, DoS, Reconnaissance, and Information Theft have increased drastically.

This project proposes a Hybrid Deep Learning model using:

🔹 PCA (Dimensionality Reduction)

🔹 Autoencoder

🔹 LSTM

🔹 CNN

To efficiently detect botnet attacks in resource-constrained IoT environments.

📂 Dataset Used: Bot-IoT Dataset

🧠 Problem Statement

IoT devices:

Have limited memory ⚠️

Cannot handle high-dimensional traffic data ❌

Are vulnerable to botnet attacks 🦠

We solve this by:

Reducing feature dimensions

Building a lightweight hybrid deep learning model

Achieving high detection accuracy 🎯

🏗️ System Architecture
4
🔄 Workflow

1️⃣ Data Selection
2️⃣ Data Preprocessing
3️⃣ Normalization
4️⃣ PCA (Dimensionality Reduction)
5️⃣ Autoencoder
6️⃣ LSTM & CNN Classification
7️⃣ Performance Evaluation

📊 Dataset Information

📌 Dataset: Bot-IoT

📈 Original Features: 43

💾 Original Size: 1.085 GB

🎯 Attack Categories:

DDoS

DoS

Reconnaissance

Information Theft

⚙️ Technologies Used
Component	Technology
Language	🐍 Python
IDE	Anaconda Navigator – Spyder
ML Libraries	Scikit-learn
DL Framework	TensorFlow / Keras
OS	Windows 7
🔬 Modules Description
📌 1. Data Selection

Loaded Bot-IoT dataset

Selected relevant attack traffic features

🧹 2. Data Preprocessing

Missing value removal

Label Encoding

Duplicate removal

📏 3. Normalization

MinMax Scaling (0–1)

Standard Scaling

📉 4. Dimensionality Reduction

PCA reduces high-dimensional features

Removes noise & redundant information

🧬 5. Autoencoder

Encoder + Decoder architecture

Learns compressed feature representation

Lightweight memory usage

🤖 6. Classification

🔁 LSTM (Sequential Pattern Detection)

🧱 CNN (Feature Extraction)

🧮 Performance Metrics

We evaluate using:

✅ Accuracy

✅ Precision

✅ Recall

✅ F1 Score
