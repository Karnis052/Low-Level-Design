package linkedin

import (
	"fmt"
	"sync"
)

type LinkedInService struct {
	users        map[string]*User
	jobPosting   map[string]*JobPosting
	notification map[string]*Notification

	mu sync.RWMutex
}

var (
	instance *LinkedInService
	once     sync.Once
)

func GetLinkedInService() *LinkedInService {
	once.Do(func() {
		instance = &LinkedInService{
			users:        make(map[string]*User),
			jobPosting:   make(map[string]*JobPosting),
			notification: make(map[string]*Notification),
		}
	})
	return instance
}

func (s *LinkedInService) RegisterUser(user *User) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.users[user.ID] = user
}

func (s *LinkedInService) LoginUser(email, password string) (*User, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	for _, user := range s.users {
		if user.email == email && user.password == password {
			return user, nil
		}
	}
	return nil, fmt.Errorf("invalid email or password")
}

func (s *LinkedInService) UpdateUserProfile(user *User) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.users[user.ID] = user
}
