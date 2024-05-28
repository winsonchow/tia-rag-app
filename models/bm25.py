from rank_bm25 import BM25Okapi

# Rank the articles based on BM25 scores
def rank_articles(cleaned_articles, keywords):
    if cleaned_articles and cleaned_articles[0] != 'No relevant posts found.':
        # Tokenize the articles
        tokenized_articles = [article.split() for article in cleaned_articles]

        # Initialize BM25
        bm25 = BM25Okapi(tokenized_articles)

        # Tokenize the query
        tokenized_query = " ".join(keywords).split()

        # Get BM25 scores
        scores = bm25.get_scores(tokenized_query)
        
        # Get the indices of the top 5 articles
        top_5_indices = scores.argsort()[::-1][:5]
        
        # Select the top 5 articles based on BM25 scores
        top_5_articles = [cleaned_articles[i] for i in top_5_indices]

        return top_5_articles
    else:
        print("No relevant articles found.")
        return []