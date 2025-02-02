package linkedin

import "sync"

type Profile struct {
	profilePicture string
	headline       string
	summary        string
	experiences    []*Experience
	educations     []*Education
	skills         []*Skill
	mu             sync.RWMutex
}

func NewProfile() *Profile {
	// Return a pointer to a new Profile instance
	return &Profile{
		// Initialize Experiences as an empty slice of pointers to Experience structs
		experiences: make([]*Experience, 0),
		educations:  make([]*Education, 0),
		skills:      make([]*Skill, 0),
	}
}

func (p *Profile) SetSummary(summary string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.summary = summary
}

func (p *Profile) SetHeadline(headline string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.headline = headline
}

func (p *Profile) GetSummary() string {
	p.mu.RLock()
	defer p.mu.Unlock()
	return p.summary
}
