package facebook

import "time"

type Comment struct {
	ID        string
	userID    string
	postID    string
	content   string
	timeStamp time.Time
}

func NewComment(id, userId, postId, content string) *Comment {
	return &Comment{
		ID:        id,
		userID:    userId,
		postID:    postId,
		content:   content,
		timeStamp: time.Now(),
	}
}
