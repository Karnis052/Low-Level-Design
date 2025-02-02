package linkedin

import (
	"fmt"
)

func Run() {
	service := GetLinkedInService()
	user1 := NewUser("1", "Karnis", "karnis052@gmail.com", "12345")
	user2 := NewUser("2", "Fatema", "fatema@gmail.com", "fatema")

	service.RegisterUser(user1)
	service.RegisterUser(user2)

	//Login
	loggedInUser, err := service.LoginUser("karnis052@gmail.com", "12345")
	if err != nil {
		fmt.Printf("Logged in failed: %v\n", err)
		return
	}
	fmt.Printf("User logged in %s\n", loggedInUser.name)

	//Update profile
	loggedInUser.profile.SetHeadline("Software Engineer")
	loggedInUser.profile.SetSummary("Passionate about coding and problem-solving")
	service.UpdateUserProfile(loggedInUser)

	//send connection request
	service.SendConnectionRequest(user2, user1)

	//accept connection request
	service.AcceptConnectionRequest(user1, user2)

	//post job listing
	jobPosting := NewJobPosting(
		"1",
		"Software Engineer",
		"A laravel software engineer of 2 years experience",
		[]string{"Go", "MySQL", "NoSQL"},
		"Dhaka",
	)
	service.PostJobListing(jobPosting)

	//search users
	userSearchResult := service.SearchUsers("Karnis")
	fmt.Println("\nUser Search Result")
	for _, user := range userSearchResult {
		fmt.Printf("Name: %s\n", user.name)
		fmt.Printf("Headline: %s\n\n", user.profile.headline)
	}

	//search job
	jobSearchResult := service.SearchJobPostings("Software Engineer")
	for _, job := range jobSearchResult {
		fmt.Printf("Job title: %s\n", job.title)
		fmt.Printf("Job description: %s\n\n", job.description)
	}

	//send Message
	service.SendMessage(user2, user1, "Hello, how are you?")

	//get  notifications
	notifications := service.GetNotifications(user1.ID)
	fmt.Println("Notificationss ")
	for _, notification := range notifications {
		fmt.Printf("Type: %v\n", notification.notificationType)
		fmt.Printf("Content: %s\n", notification.content)
	}

}
