package facebook

type NotificationType int

const (
	NotificationTypeFriendRequest NotificationType = iota
	NotificationTypeFriendRequestAccept
	NotificationTypeComment
	NotificationTypeLike
	NotificationTypeMention
)

func (nt NotificationType) String() string {
	return [...]string{
		"FRIEND_REQUEST",
		"FRIEND_REQUEST_ACCEPTED",
		"COMMENT",
		"LIKE",
		"MENTION",
	}[nt]
}
