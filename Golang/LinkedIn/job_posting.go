package linkedin

import "time"

type JobPosting struct {
	ID           string
	title        string
	description  string
	requirements []string
	location     string
	postDate     time.Time
}

func NewJobPosting(id, title, description string, requirements []string, location string) *JobPosting {
	return &JobPosting{
		ID:           id,
		title:        title,
		description:  description,
		requirements: requirements,
		location:     location,
		postDate:     time.Now(),
	}
}
