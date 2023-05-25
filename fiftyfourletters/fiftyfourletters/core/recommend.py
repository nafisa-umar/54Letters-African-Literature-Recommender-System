from .models import Book
import numpy
import pickle


def recommend(rec_id):
    # Specify the path to your pickle file
    pickle_file_path = 'core/artifacts/similarity.pkl'

    # Unpickle the similarity matrix
    with open(pickle_file_path, 'rb') as file:
        similarity = pickle.load(file)

    # extract similarities
    similarities = similarity[rec_id]
    # Get the indices of the 5 highest similarities
    similar_book_ids = similarities.argsort()[-6:-1][::-1]
    print(similar_book_ids)
    return similar_book_ids
