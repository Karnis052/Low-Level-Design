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

	loggedInUser, err := service.LoginUser("karnis052@gmail.com", "12345")
	if err != nil {
		fmt.Printf("Logged in failed: %v\n", err)
		return
	}
	fmt.Printf("User logged in %s\n", loggedInUser.name)
}
