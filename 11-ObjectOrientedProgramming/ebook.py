class Ebook:
    curr_page = 1
    is_open = False

    def __init__(self, title, author, pages_num):
        self.title = title
        self.author = author
        self.pages_num = pages_num

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            self.curr_page += 1

    def prev_page(self):
        if self.is_open:
            self.curr_page -= 1

    def set_page(self, page):
        self.curr_page = page

    def display_status(self):
        print(
            f"{self.title}, {self.author} pages: {self.pages_num}, current page: {self.curr_page}"
        )
