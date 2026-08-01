dataset = {
    1: "Python is an amazing programming language.",
    2: "Time complexity helps us build fast search engines.",
    3: "Binary search algorithms cut data in half."
}

def clean_and_split(text):
    # 1. Make everything lowercase
    lower_text = text.lower()
    
    # 2. Remove the period at the end
    cleaned_text = lower_text.replace(".", "")
    
    # 3. Chop the sentence into a list of words
    words_list = cleaned_text.split()
    
    return words_list

# Create an empty dictionary to hold our index
inverted_index = {}

# Loop through each document in our dataset
for doc_id, sentence in dataset.items():
    # Clean the sentence and get the list of words
    words = clean_and_split(sentence)
    
    # Look at each word one by one
    for word in words:
        # If the word is not in our index yet, add it with an empty list
        if word not in inverted_index:
            inverted_index[word] = []
        
        # Add the current document ID to this word's list
        # But only if it's not already there (to avoid duplicates)
        if doc_id not in inverted_index[word]:
            inverted_index[word].append(doc_id)

def search(query_word):
    # 1. Clean the search word just like we cleaned our dataset
    cleaned_query = query_word.lower().strip()
    
    # 2. Look up the word in our inverted index
    if cleaned_query in inverted_index:
        # Get the list of document IDs
        matching_ids = inverted_index[cleaned_query]
        print(f"\nResults for '{query_word}':")
        
        # Loop through the matching IDs and print the original sentences
        for doc_id in matching_ids:
            print(f"  - Document {doc_id}: {dataset[doc_id]}")
    else:
        print(f"\n'{query_word}' not found in any document.")

search("search")
search("Python")
search("spaceship")


