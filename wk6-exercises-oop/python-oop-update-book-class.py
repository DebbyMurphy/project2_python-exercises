# Q1) Together, we wrote a class for a Book object. Update this class to add the ability to:
# 1. Go directly to a specific page number.
# 2. Bookmark a specific page number, i.e. not just the current page.
# 3. Automatically go back to the start of the book (i.e. page 1) when the user turns the final page.


class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1

    def move_bookmark(self):
        self.bookmarked_page = self.current_page
    
    def turn_page(self, forward):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages

# ---------------------------------------------------------
    def moveto_page(self, pagenumber):
        if pagenumber > 0:
            self.current_page = pagenumber
# ---------------------------------------------------------

book_1 = Book("Cats", "Real Person", 213, 1)
book_1.moveto_page(20)
print(book_1.current_page)



