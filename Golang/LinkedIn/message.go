package linkedin

import "time"

type Message struct {
	ID        string
	sender    *User
	receiver  *User
	content   string
	timeStamp time.Time
}

func NewMessage(id string, sender, receiver *User, content string) *Message {
	return &Message{
		ID:        id,
		sender:    sender,
		receiver:  receiver,
		content:   content,
		timeStamp: time.Now(),
	}
}
