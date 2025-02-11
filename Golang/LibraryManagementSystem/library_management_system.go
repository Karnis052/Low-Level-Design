package librarymanagementsystem

import "fmt"

func Run() {
	libraryManager := GetLibraryManager()

	book1 := NewBook("ISBN 1", "Title 1", "Author 1", 2020)
	book2 := NewBook("ISBN 2", "Title 2", "Author 2", 2021)
	book3 := NewBook("ISBN 3", "Title 3", "Author 3", 2022)

	libraryManager.AddBook(book1)
	libraryManager.AddBook(book2)
	libraryManager.AddBook(book3)

	member1 := NewMember("1", "Name 1", "Contact Info 1")
	member2 := NewMember("2", "Name 2", "Contact Info 2")

	libraryManager.RegisterMember(member1)
	libraryManager.RegisterMember(member2)

	if err := libraryManager.BorrowBook(member1.ID, book1.ISBN); err != nil {
		fmt.Printf("error while borrowing book %s\n", err)
	}
	if err := libraryManager.BorrowBook(member2.ID, book2.ISBN); err != nil {
		fmt.Printf("error while borrowing book %s\n", err)
	}
	if err := libraryManager.BorrowBook(member2.ID, book1.ISBN); err != nil {
		fmt.Printf("error while borrowing book %s\n", err)
	}
	if err := libraryManager.ReturnBook(member1.ID, book1.ISBN); err != nil {
		fmt.Printf("Error returning book: %v\n", err)
	}
	searchResult := libraryManager.SearchBook("Title")
	fmt.Printf("\n\nSearch Result\n")
	for _, book := range searchResult {
		fmt.Printf("%s by %v\n", book.title, book.authorName)
	}
}
