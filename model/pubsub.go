package model

// PubsubMsg is the message recevied by the subscriber
type PubsubMsg struct {
	Data    []byte
}

type PubsubCallback func(subject string, msg *PubsubMsg) ()
