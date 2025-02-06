package facebook

import (
	"fmt"
	"sort"
	"sync"
	"time"
)

type SocialNetwork struct {
	users         map[string]*User
	posts         map[string]*Post
	notifications map[string][]*Notification
	mu            sync.RWMutex
}

var (
	instance *SocialNetwork
	one      sync.Once
)

func GetSocialNetwork() *SocialNetwork {
	one.Do(func() {
		instance = &SocialNetwork{
			users:         make(map[string]*User),
			posts:         make(map[string]*Post),
			notifications: make(map[string][]*Notification),
		}
	})
	return instance
}

// Register User
func (sn *SocialNetwork) RegisterUser(user *User) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()
	if _, exists := sn.users[user.ID]; exists {
		return fmt.Errorf("User with ID %s is already exists", user.ID)
	}
	sn.users[user.ID] = user
	return nil
}

// Login User
func (sn *SocialNetwork) LoginUser(email, password string) (*User, error) {
	sn.mu.RLock()
	defer sn.mu.RUnlock()
	for _, user := range sn.users {
		if user.email == email && user.password == password {
			return user, nil
		}
	}
	return nil, fmt.Errorf("invalid email or password")

}

// update user profile
func (sn *SocialNetwork) UpdateUserProfile(user *User) {
	sn.mu.Lock()
	defer sn.mu.Unlock()
	sn.users[user.ID] = user

}

//Send Friend Request

func (sn *SocialNetwork) SendFriendRequest(senderId, receiverId string) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()

	receiver, exists := sn.users[receiverId]
	if !exists {
		return fmt.Errorf("receiver not found")
	}
	notification := NewNotification(
		fmt.Sprintf("notif-%d", time.Now().UnixNano()),
		receiver.ID,
		NotificationTypeFriendRequest,
		fmt.Sprintf("Friend request from %s", senderId),
	)
	sn.AddNotification(receiverId, notification)
	return nil
}

//Accept request

func (sn *SocialNetwork) AcceptFriendRequest(recieverId, senderId string) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()

	receiver, exists1 := sn.users[recieverId]
	sender, exists2 := sn.users[senderId]
	if !exists1 || !exists2 {
		return fmt.Errorf("user not found")
	}
	receiver.AddFriend(senderId)
	sender.AddFriend(recieverId)

	notification := NewNotification(
		fmt.Sprintf("notif-%d", time.Now().UnixNano()),
		senderId,
		NotificationTypeFriendRequestAccept,
		fmt.Sprintf("Friend request accepted by %s", receiver.name),
	)
	sn.AddNotification(senderId, notification)
	return nil

}

//createPost

func (sn *SocialNetwork) CreatePost(post *Post) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()
	user, exists := sn.users[post.ID]
	if !exists {
		return fmt.Errorf("user not found")
	}
	user.AddPost(post)
	sn.posts[post.ID] = post
	return nil
}

//generate newsfeed

func (sn *SocialNetwork) GenerateNewsfeed(userId string) ([]*Post, error) {
	sn.mu.RLock()
	defer sn.mu.RUnlock()

	user, exists := sn.users[userId]
	if !exists {
		return nil, fmt.Errorf("user not found")
	}
	var newsfeed []*Post
	newsfeed = append(newsfeed, user.GetPosts()...)
	for friendID := range user.friends {
		if friend, ok := sn.users[friendID]; ok {
			newsfeed = append(newsfeed, friend.GetPosts()...)
		}
	}
	sort.Slice(newsfeed, func(i, j int) bool {
		return newsfeed[i].timeStamp.After(newsfeed[j].timeStamp)
	})
	return newsfeed, nil
}

//comment post

func (sn *SocialNetwork) CommentOnPost(comment *Comment) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()

	_, exists := sn.users[comment.userID]
	if !exists {
		return fmt.Errorf("User not found")
	}
	post, existsPost := sn.posts[comment.postID]
	if !existsPost {
		return fmt.Errorf("post not found")
	}
	post.AddComment(comment)
	notification := NewNotification(
		fmt.Sprintf("notif-%d", time.Now().UnixNano()),
		post.userID,
		NotificationTypeComment,
		fmt.Sprintf("Your post receive a comment from %s", comment.userID),
	)
	sn.AddNotification(post.userID, notification)
	return nil
}

//like post

func (sn *SocialNetwork) LikePost(userId, postId string) error {
	sn.mu.Lock()
	defer sn.mu.Unlock()
	post, exists := sn.posts[postId]
	if !exists {
		return fmt.Errorf("post not found")
	}
	if added := post.AddLike(userId); added {
		notification := NewNotification(
			fmt.Sprintf("notif-%d", time.Now().UnixNano()),
			post.userID,
			NotificationTypeLike,
			fmt.Sprintf("Your post get a like from %s", userId),
		)
		sn.AddNotification(post.userID, notification)
	}
	return nil

}

//add notification

func (sn *SocialNetwork) AddNotification(userId string, notification *Notification) {
	// sn.mu.Lock()
	// defer sn.mu.Unlock()
	sn.notifications[userId] = append(sn.notifications[userId], notification)

}

// get notification
func (sn *SocialNetwork) GetNotifications(userId string) ([]*Notification, error) {
	sn.mu.RLock()
	defer sn.mu.RUnlock()

	if _, exists := sn.users[userId]; !exists {
		return nil, fmt.Errorf("user not found")
	}

	return sn.notifications[userId], nil
}
