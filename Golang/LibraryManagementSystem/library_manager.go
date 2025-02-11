package librarymanagementsystem

import (
	"fmt"
	"strings"
	"sync"
)

const (
	maxBookPerMember = 5
	loanDurationDay  = 14
)

type LibraryManager struct {
	catalog map[string]*Book
	members map[string]*Memeber
	mu      sync.RWMutex
}

var (
	instance *LibraryManager
	once     sync.Once
)

func GetLibraryManager() *LibraryManager {
	once.Do(func() {
		instance = &LibraryManager{
			catalog: make(map[string]*Book),
			members: make(map[string]*Memeber),
		}
	})
	return instance
}

// Add Book
func (lm *LibraryManager) AddBook(book *Book) {
	lm.mu.Lock()
	defer lm.mu.Unlock()
	lm.catalog[book.ISBN] = book
}

// remove book
func (lm *LibraryManager) RemoveBook(isbn string) {
	lm.mu.Lock()
	defer lm.mu.Unlock()
	delete(lm.catalog, isbn)
}

//get books

func (lm *LibraryManager) GetBook(isbn string) *Book {
	lm.mu.RLock()
	defer lm.mu.Unlock()
	return lm.catalog[isbn]
}

//register member

func (lm *LibraryManager) RegisterMember(member *Memeber) {
	lm.mu.Lock()
	defer lm.mu.Unlock()
	lm.members[member.ID] = member
}

// unregister member
func (lm *LibraryManager) UnRegisterMember(memberId string) {
	lm.mu.Lock()
	defer lm.mu.Unlock()
	delete(lm.members, memberId)
}

//get member

func (lm *LibraryManager) GetMember(memberId string) *Memeber {
	lm.mu.RLock()
	defer lm.mu.RUnlock()
	return lm.members[memberId]
}

//borrow book

func (lm *LibraryManager) BorrowBook(memberId, isbn string) error {
	lm.mu.Lock()
	defer lm.mu.Unlock()
	member := lm.members[memberId]
	book := lm.catalog[isbn]

	if member == nil || book == nil {
		return fmt.Errorf("book or member not found")
	}

	if !book.IsAvailable() {
		return fmt.Errorf("requested book is not available")
	}
	if len(member.GetBorrowedBooks()) >= maxBookPerMember {
		return fmt.Errorf("member %s has reached the maximum number of borrowed books", member.name)
	}
	member.BorrowBook(book)
	book.SetAvailable(false)
	fmt.Printf("Book %s borrowed by %s\n", book.title, member.name)
	return nil
}

//return book

func (lm *LibraryManager) ReturnBook(memberId, isbn string) error {
	lm.mu.Lock()
	defer lm.mu.Unlock()

	member := lm.members[memberId]
	book := lm.catalog[isbn]

	if member == nil || book == nil {
		return fmt.Errorf("member or book is not found")
	}

	member.ReturnBook(book)
	book.SetAvailable(true)
	fmt.Printf("Book %s is returned by %s", book.title, member.name)
	return nil
}

//search book

func (lm *LibraryManager) SearchBook(keyword string) []*Book {
	lm.mu.RLock()
	defer lm.mu.RUnlock()

	keyword = strings.ToLower(keyword)
	books := make([]*Book, 0)

	for _, book := range lm.catalog {
		if strings.Contains(strings.ToLower(book.title), keyword) ||
			strings.Contains(strings.ToLower(book.authorName), keyword) {
			books = append(books, book)
		}
	}
	return books
}
