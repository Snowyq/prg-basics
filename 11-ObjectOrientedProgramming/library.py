from ebook import Ebook


def main():
    my_ebook = Ebook("Hobbit", "Tolkien", 234)

    my_ebook.display_status()
    my_ebook.open()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.next_page()
    my_ebook.display_status()
    my_ebook.prev_page()
    my_ebook.prev_page()
    my_ebook.display_status()
    my_ebook.close()


if __name__ == "__main__":
    main()
