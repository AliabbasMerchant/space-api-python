package nats

import (
	"encoding/json"

	nts "github.com/nats-io/nats.go"
)

// nats holds the nats driver session
type nats struct {
	conn *nats.Conn
}

func Connect(conn string) (*nats, err) {
	nc, err := nts.Connect(pubsub.Conn)
	if err != nil {
		return err
	}
	return &nats{nc}, nil
}

func (n *nats) Publish(subject string, msg *model.PubsubMsg) error {
	b, err := json.Marshal(msg)
    if err != nil {
        return err
    }
	return n.conn.Publish(subject, b)
}

func (n *nats) QueueSubscribe(subject, group string, ch chan *model.PubsubMsg) (*nts.Subscription, error) {
	return n.conn.ChanQueueSubscribe(subject, group, ch)
}
