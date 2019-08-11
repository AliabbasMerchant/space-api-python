package pubsub

import (
	"errors"
	"sync"

	nts "github.com/nats-io/nats.go"

	"github.com/spaceuptech/space-cloud/config"
	"github.com/spaceuptech/space-cloud/modules/pubsub/nats"
	"github.com/spaceuptech/space-cloud/model"
	"github.com/spaceuptech/space-cloud/utils"
)

// Module is responsible for Pubsub
type Module struct {
	sync.RWMutex
	broker     string
	connection pubsubBroker
	enabled    bool
	storage    sync.Map
	channel    chan *nts.Msg
}

// Init returns a new instance of the Pubsub module
func Init() *Module {
	m := new(Module)
	return m
}

// SetConfig sets the config required by the Pubsub module
func (m *Module) SetConfig(pubsub *config.Pubsub) error {
	m.Lock()
	defer m.Unlock()

	if pubsub == nil || !pubsub.Enabled {
		m.enabled = false
		return nil
	}

	switch pubsub.Broker {
	case utils.Nats:
		m.broker = Pubsub.Broker
		if m.connection == nil {
			nc, err := nats.Connect(pubsub.Conn)
			if err != nil {
				return err
			}
			m.connection = nc
		}
	default:
		return errors.New("Functions Error: Broker is not supported")
	}

	m.enabled = true
	return nil
}

// IsEnabled checks if the Functions module is enabled
func (m *Module) IsEnabled() bool {
	m.RLock()
	defer m.RUnlock()

	return m.enabled
}
