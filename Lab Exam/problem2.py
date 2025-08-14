def recommend_book_by_genre(genre):
    books_by_genre = {
        "romance": "fragrant flowers",
        "Horror": "anabelle",
        "scifi": "avengers"
    }
    return books_by_genre.get(genre, "No recommendation available")

# Example usage:
# List of books with their genres
books = [
    {"name": "fragrant flowers", "genre": "romance"},
    {"name": "anabelle", "genre": "Horror"},
    {"name": "avengers", "genre": "scifi"},
    {"name": "pride and prejudice", "genre": "romance"},
    {"name": "dracula", "genre": "Horror"},
    {"name": "dune", "genre": "scifi"}
]

def find_books(query):
    # Search by genre or book name (case-insensitive)
    query = query.lower()
    results = []
    for book in books:
        if book["genre"].lower() == query or book["name"].lower() == query:
            results.append(book["name"])
    if results:
        return results
    else:
        return ["No recommendation available"]

# Example usage:
print(find_books("romance"))  # Output: ['fragrant flowers', 'pride and prejudice']
print(find_books("Horror"))   # Output: ['anabelle', 'dracula']
print(find_books("avengers")) # Output: ['avengers']
preferred_genre = "Horror"
books_in_preferred_genre = find_books(preferred_genre)
print(f"Your preferred genre is {preferred_genre.lower()} and the books under it are: {books_in_preferred_genre}")


