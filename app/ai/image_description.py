from transformers import pipeline

def predict_product_category_from_keywords(keywords):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Define your keywords and candidate labels
    keywords = "smartphone, 5G, latest technology"
    candidate_labels = ["Electronics", "Fashion", "Home & Garden", "Books"]

    # Use the model to classify the keywords
    results = classifier(keywords, candidate_labels)

    # Print the predicted category with the highest score
    print(results["labels"][0])
