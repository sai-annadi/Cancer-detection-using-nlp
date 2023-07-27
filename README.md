# Cancer-detection-using-nlp
![image](https://github.com/Saiannadi/Cancer-detection-using-naviesbayes/assets/111168434/a0b3c0d4-a95e-432d-b0dd-32cf6cc18997)


The Cancer Detection using NLP with Streamlit project is a powerful and user-friendly application designed to aid in early cancer detection based on symptoms provided by the user. The model used for prediction is trained in Google Colab, leveraging the vast computational resources and libraries available in the cloud-based environment. The dataset, scraped from cancer.net, undergoes preprocessing to extract relevant information and create a symptom-feature matrix for training the Multinomial Naive Bayes classifier.

Once the model training is completed in Colab, the trained classifier is serialized using the pickle library and saved as a binary file. This serialized model file is then seamlessly integrated into the Streamlit application. When a user enters their symptoms through the Streamlit web interface, the application loads the pre-trained model using pickle.load() to access the NLP classifier.

The user-provided symptoms are processed using the trained NLP features, and the model predicts the most probable type of cancer based on the input symptoms. The application then presents the prediction output to the user, providing valuable insights into potential health conditions associated with the provided symptoms. The integration of the pre-trained model into the Streamlit application ensures a smooth and efficient user experience, enabling quick and accurate symptom-based cancer predictions.

By combining the computational capabilities of Google Colab with the interactive nature of Streamlit, the Cancer Detection project offers a powerful and accessible tool for early cancer detection. Users can benefit from the expertise of the pre-trained NLP classifier without needing to worry about model training or complex coding. This collaborative approach empowers individuals with crucial health information, potentially leading to earlier cancer diagnosis and improved treatment outcomes.
