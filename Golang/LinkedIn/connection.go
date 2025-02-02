package linkedin

import "time"

type Connection struct {
	user           *User
	connectionDate time.Time
}

func NewConnection(user *User) *Connection {
	return &Connection{
		user:           user,
		connectionDate: time.Now(),
	}
}
