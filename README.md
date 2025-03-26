# 🚀 AI-Powered Data Profiling Tool

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)


## 🎯 Introduction
In the banking sector, regulatory compliance demands rigorous validation of transaction data against complex rules—a process often bogged down by manual effort and human error. Our Data Profiling Gen AI project revolutionizes this workflow by automating rule extraction and anomaly detection.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
In the banking sector, regulatory reporting demands meticulous compilation of vast data volumes to ensure compliance. Data profiling plays a pivotal role in this process, verifying that reported data adheres to strict regulatory guidelines. Traditionally, this task relies on manual efforts—profiling rules are painstakingly defined based on raw data and regulatory documents, a process that is time-consuming, error-prone, and inefficient.

_Why we built an AI-powered Data Profiler?_

- **Efficiency:** Manual profiling is slow; AI automates rule generation and validation, accelerating the process.
- **Accuracy:** Human errors in interpreting regulations or data are reduced through AI’s consistent logic.
- **Scalability:** AI handles growing data volumes and evolving regulations without proportional increases in human effort.
- **Adaptability:** Machine learning dynamically updates rules as regulatory requirements change.
- **Cost Savings:** Automation reduces reliance on labor-intensive manual reviews, lowering operational costs.

By leveraging AI, we transform regulatory reporting from a reactive, cumbersome task into a proactive, streamlined workflow—ensuring compliance with precision and agility.

## ⚙️ What It Does
Here’s how our Data Profiling tool works:

- ✅ Rule Extraction: Upload a PDF containing regulatory guidelines or compliance rules. Our system leverages DeepSeek R1 to intelligently extract and structure the most critical profiling rules.
- ✅ Automated Validation: Apply these AI-generated rules to your transaction datasets to instantly flag anomalies, ensuring adherence to compliance standards.
- ✅ Precision at Scale: By combining DeepSeek’s advanced NLP with customizable validation logic, we transform unstructured documents into actionable insights—reducing risk and accelerating audits.

Say goodbye to manual rule-mapping and embrace AI-driven compliance that’s faster, smarter, and error-free. 🚀

## 🛠️ How We Built It
Our solution is built on a robust Python backend, leveraging Streamlit for an intuitive frontend interface that lets users upload PDFs and visualize compliance results seamlessly. At its core, DeepSeek R1 processes regulatory documents to extract and refine rules, while libraries like Pandas enable efficient data wrangling and anomaly detection on transaction datasets.

## 🚧 Challenges We Faced
Developing an automated system to extract compliance rules from regulatory PDFs and validate transaction data came with its fair share of hurdles. Here are some key challenges we tackled:

- Rule Extraction from Complex PDFs
Regulatory documents often contain unstructured text, tables, and legal jargon, making it difficult for AI to accurately identify and extract relevant rules.

- Contextual Understanding of Compliance Rules
Not all rules are explicitly stated—some require implicit logic (e.g., "transactions above $10,000 must be reported" implies a threshold check). DeepSeek R1 sometimes over-generalized or misinterpreted ambiguous phrasing, requiring fine-tuning to improve precision.

- Mapping Rules to Transaction Data
Extracted rules needed precise translation into executable code (SQL, JSON, or validation logic).

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Run the commands
   ```sh
   python -m venv venv
   
   .\venv\Scripts\activate
   ```
3. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
   python run.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: Streamlit
- 🔹 Backend: Python
- 🔹 Gen-AI: Deepseek-r1

## 👥 Team
- **Pulkit Gupta** - [GitHub](#) | [LinkedIn](#)
- **Sakshi Jain** - [GitHub](#) | [LinkedIn](#)
- **Madhurim Gupta** - [GitHub](#) | [LinkedIn](#)
- **Rudra Pujara** - [GitHub](#) | [LinkedIn](#)
