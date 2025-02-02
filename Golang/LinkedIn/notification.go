package linkedin

import "time"

type Notification struct {
	ID               string
	user             *User
	notificationType NotificationType
	content          string
	timeStamp        time.Time
}

func NewNotification(id string, user *User, notifyType NotificationType, content string) *Notification {
	return &Notification{
		ID:               id,
		user:             user,
		notificationType: notifyType,
		content:          content,
		timeStamp:        time.Now(),
	}
}
