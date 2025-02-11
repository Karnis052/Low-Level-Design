package librarymanagementsystem

import "sync"

type Book struct {
	ISBN            string
	title           string
	authorName      string
	publicationYear int
	availabe        bool
	mu              sync.RWMutex
}

func NewBook(isbn, title, authorName string, publicationYear int) *Book {
	return &Book{
		ISBN:            isbn,
		title:           title,
		authorName:      authorName,
		publicationYear: publicationYear,
		availabe:        true,
	}
}

func (b *Book) IsAvailable() bool {
	b.mu.RLock()
	defer b.mu.RUnlock()
	return b.availabe
}

func (b *Book) SetAvailable(availabe bool) {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.availabe = availabe
}
