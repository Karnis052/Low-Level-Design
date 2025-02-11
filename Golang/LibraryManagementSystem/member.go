package librarymanagementsystem

import "sync"

type Memeber struct {
	ID            string
	name          string
	contactInfo   string
	borrowedBooks map[string]*Book
	mu            sync.RWMutex
}

func NewMember(id, name, contactInfo string) *Memeber {
	return &Memeber{
		ID:            id,
		name:          name,
		contactInfo:   contactInfo,
		borrowedBooks: make(map[string]*Book),
	}
}

func (m *Memeber) BorrowBook(book *Book) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.borrowedBooks[book.ISBN] = book
}
func (m *Memeber) ReturnBook(book *Book) {
	m.mu.Lock()
	defer m.mu.Unlock()
	delete(m.borrowedBooks, book.ISBN)
}

func (m *Memeber) GetBorrowedBooks() []*Book {
	m.mu.RLock()
	defer m.mu.RUnlock()
	books := make([]*Book, 0, len(m.borrowedBooks))
	for _, book := range m.borrowedBooks {
		books = append(books, book)
	}
	return books
}
