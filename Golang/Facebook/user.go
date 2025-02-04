package facebook

import "sync"

type User struct {
	ID             string
	name           string
	email          string
	password       string
	profilePicture string
	bio            string
	friends        map[string]bool
	posts          []*Post
	mu             sync.RWMutex
}

func NewUser(id, name, email, password, profilePicture, bio string) *User {
	return &User{
		ID:             id,
		name:           name,
		email:          email,
		password:       password,
		profilePicture: profilePicture,
		bio:            bio,
		friends:        make(map[string]bool),
		posts:          make([]*Post, 0),
	}
}

func (u *User) AddFriend(friendId string) {
	u.mu.Lock()
	defer u.mu.Unlock()
	u.friends[friendId] = true
}

func (u *User) AddPost(post *Post) {
	u.mu.Lock()
	defer u.mu.Unlock()
	u.posts = append(u.posts, post)

}

func (u *User) GetFriends() []string {
	u.mu.RLock()
	defer u.mu.RUnlock()
	friends := make([]string, 0, len(u.friends))
	for friendID := range u.friends {
		friends = append(friends, friendID)
	}
	return friends
}

func (u *User) GetPosts() []*Post {
	u.mu.RLock()
	defer u.mu.RUnlock()
	posts := make([]*Post, len(u.posts))
	copy(posts, u.posts)
	return posts
}
