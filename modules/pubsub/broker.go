package pubsub

import (
	"github.com/spaceuptech/space-cloud/model"
	"github.com/spaceuptech/space-cloud/utils"
)

natsWildcard string = ">"

type subscription interface {
	Unsubscribe() error
}

type pubsubBroker interface {
	Publish(subject string, msg *model.PubsubMsg) error
	QueueSubscribe(subject, group string, ch chan *model.PubsubMsg) (*subscription, error)
}

type pubsubSubscription {
	subs *subscription
	ch   chan *model.PubsubMsg
}

func (m *Module) Publish(subject string, data *model.PubsubMsg) error {
	return m.connection.Publish(subject, data)
}

func (m *Module) Subscribe(clientId, subject string, cb model.PubsubCallback) (error) {
	return m.QueueSubscribe(clientId, subject, clientId, cb)
}

func (m *Module) QueueSubscribe(clientId, subject, group string, cb model.PubsubCallback) (error) {
	ch := make(chan *model.PubsubMsg, 10)
	subject = utils.SingleLeadingTrailing(subject, "/")
	subs, err := m.connection.QueueSubscribe(subject + natsWildcard, group, ch)
	if err != nil {
		return err
	}
	pubsubSubs := pubsubSubscription{subs, ch}
	err = m.storeSubs(subject, clientId, &pubsubSubs)
	if err != nil {
		subs.Unsubscribe()
		ch.Close()
		return err
	}
	go func() {
		for msg := range ch {
        	cb(subject, msg)
		}
	}()
	return nil
}

func (m *Module) Unsubscribe(clientId, subject string) err {
	subject = utils.SingleLeadingTrailing(subject, "/")
	// TODO
	// get subs
	// type cast
	// delete
	// subs.subs.Unsubscribe()
	// subs.ch.Close()
	return nil
}

func (m *Module) UnsubscribeAll(clientId string) err {
	// TODO
	// iterate
	// delete
	return nil
}

//Map subject -> clientId -> pubsubSubscription
func (m *Module) storeSubs(subject, clientId string, subs *pubsubSubscription) error {
	// TODO
	return nil
}

// check if channels are of correct type
// check subject to be returned
