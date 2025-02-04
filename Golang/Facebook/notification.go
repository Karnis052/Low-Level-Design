package facebook

import "time"

type Notification struct {
	ID        string
	userID    string
	nType     NotificationType
	content   string
	timestamp time.Time
}

func NewNotification(id, userId string, nType NotificationType, content string) *Notification {
	return &Notification{
		ID:        id,
		userID:    userId,
		nType:     nType,
		content:   content,
		timestamp: time.Now(),
	}
}
