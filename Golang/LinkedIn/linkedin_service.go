package linkedin

import (
	"fmt"
	"strings"
	"sync"
	"time"
)

type LinkedInService struct {
	users         map[string]*User
	jobPostings   map[string]*JobPosting
	notifications map[string][]*Notification

	mu sync.RWMutex
}

var (
	instance *LinkedInService
	once     sync.Once
)

func GetLinkedInService() *LinkedInService {
	once.Do(func() {
		instance = &LinkedInService{
			users:         make(map[string]*User),
			jobPostings:   make(map[string]*JobPosting),
			notifications: make(map[string][]*Notification),
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

func (s *LinkedInService) AddNotification(userID string, notification *Notification) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.notifications[userID] = append(s.notifications[userID], notification)
}

func (s *LinkedInService) SendConnectionRequest(sender, receiver *User) {
	connection := NewConnection(sender)
	receiver.AddConnection(connection)

	notification := NewNotification(
		fmt.Sprintf("NOTIF-%d", time.Now().UnixNano()),
		receiver,
		NotificationTypeConnectionRequest,
		fmt.Sprintf("New connection request from %s", sender.name),
	)
	s.AddNotification(receiver.ID, notification)
}

func (s *LinkedInService) AcceptConnectionRequest(user, connectionUser *User) {
	user.AddConnection(NewConnection(connectionUser))
}

func (s *LinkedInService) PostJobListing(jobPosting *JobPosting) {
	s.mu.Lock()
	s.jobPostings[jobPosting.ID] = jobPosting
	s.mu.Unlock()

	for _, user := range s.users {
		notification := NewNotification(
			fmt.Sprintf("NOTIF-%d", time.Now().UnixNano()),
			user,
			NotificationTypeJobPosting,
			fmt.Sprintf("New job posting: %s", jobPosting.title),
		)
		s.AddNotification(user.ID, notification)
	}
}

func (s *LinkedInService) SearchUsers(keyword string) []*User {
	s.mu.RLock()
	defer s.mu.RUnlock()

	var result []*User
	keyword = strings.ToLower(keyword)

	for _, user := range s.users {
		if strings.Contains(strings.ToLower(user.name), keyword) {
			result = append(result, user)
		}
	}
	return result
}

func (s *LinkedInService) SearchJobPostings(keyword string) []*JobPosting {
	s.mu.RLock()
	defer s.mu.RUnlock()

	var result []*JobPosting
	keyword = strings.ToLower(keyword)

	for _, job := range s.jobPostings {
		if strings.Contains(strings.ToLower(job.title), keyword) ||
			strings.Contains(strings.ToLower(job.description), keyword) {
			result = append(result, job)
		}
	}
	return result
}

func (s *LinkedInService) SendMessage(sender, receiver *User, content string) {
	message := NewMessage(
		fmt.Sprintf("MSG-%d", time.Now().UnixNano()),
		sender,
		receiver,
		content,
	)
	receiver.AddMessage(message, false)
	sender.AddMessage(message, true)
	notification := NewNotification(
		fmt.Sprintf("NOTID-%d", time.Now().UnixNano()),
		receiver,
		NotificationTypeMessage,
		fmt.Sprintf("New Message from %s", sender.name),
	)
	s.AddNotification(receiver.ID, notification)
}

func (s *LinkedInService) GetNotifications(userID string) []*Notification {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.notifications[userID]
}
