package facebook

import (
	"fmt"
	"log"
)

func Run() {
	socialNetwork := GetSocialNetwork()

	//create user
	user1 := NewUser("1", "Karnis", "karnis@gmail.com", "karnis", "profile1.jpg", "Keep faith")
	user2 := NewUser("2", "Fatema", "fatema@gmail.com", "fatema", "profile2.jpg", "Believers ")

	//register user
	if err := socialNetwork.RegisterUser(user1); err != nil {
		log.Printf("Failed to register user1: %v", err)
		return
	}
	if err := socialNetwork.RegisterUser(user2); err != nil {
		log.Printf("Failed to register user2: %v", err)
		return
	}

	// login
	loggedUser, err := socialNetwork.LoginUser("karnis@gmail.com", "karnis")
	if err != nil {
		log.Printf("login failed %v", err)
		return
	}
	fmt.Printf("user logged in %v\n", loggedUser.name)

	//send friend request
	if err := socialNetwork.SendFriendRequest(user1.ID, user2.ID); err != nil {
		log.Printf("failed to send friend request %v", err)
		return
	}

	loggedUser2, err := socialNetwork.LoginUser("fatema@gmail.com", "fatema")
	if err != nil {
		log.Printf("login failed %v", err)
		return
	}
	fmt.Printf("user logged in %v\n", loggedUser2.name)

	//accept friend request
	if err := socialNetwork.AcceptFriendRequest(user2.ID, user1.ID); err != nil {
		log.Printf("failed to accept friend request %v", err)
		return
	}

	//add post
	post1 := NewPost("1", user1.ID, "Hlw, It is my first post.", []string{}, []string{})
	post2 := NewPost("2", user2.ID, "Have a good day!", []string{}, []string{})

	if err := socialNetwork.CreatePost(post1); err != nil {
		log.Printf("failed to create post1 %v", err)
		return
	}
	if err := socialNetwork.CreatePost(post2); err != nil {
		log.Printf("failed to create post2 %v", err)
		return
	}

	//comment in post
	comment := NewComment("1", user2.ID, post1.ID, "You are Welcome.")
	if err := socialNetwork.CommentOnPost(comment); err != nil {
		log.Printf("failed to comment on post %v", err)
		return
	}

	//like in post
	if err := socialNetwork.LikePost("1", "2"); err != nil {
		log.Printf("failed to like the post %v", err)
		return
	}
	if err := socialNetwork.LikePost("2", "1"); err != nil {
		log.Printf("failed to like the post %v", err)
		return
	}
	//get newsfeed
	newsfeed, err := socialNetwork.GenerateNewsfeed(user1.ID)
	if err != nil {
		log.Printf("failed to generate newsfeed for %v and have %v", user1.ID, err)
		return
	}
	fmt.Printf("\nNewsfeed:\n")

	for _, post := range newsfeed {
		fmt.Printf("Post content: %v\n", post.content)
		fmt.Printf("Post likes: %v\n", len(post.GetLikes()))
		fmt.Printf("Post comments: %v\n\n", len(post.GetComments()))
	}
	// all notification
	notifications, err := socialNetwork.GetNotifications(user1.ID)
	if err != nil {
		log.Printf("Failed to load notification of user %v", user1.ID)
		return
	}
	fmt.Printf("\nNotifications:\n")
	for _, notification := range notifications {
		fmt.Printf("Type: %v\n", notification.nType)
		fmt.Printf("Content: %v\n\n", notification.content)

	}

}
