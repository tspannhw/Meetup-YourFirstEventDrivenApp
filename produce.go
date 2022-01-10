package main

import (
        "log"
        "time"
        "fmt"
        "context"
        "github.com/apache/pulsar-client-go/pulsar"
)

func main() {

        client, err := pulsar.NewClient(pulsar.ClientOptions{
        URL:               "pulsar://localhost:6650",
        OperationTimeout:  30 * time.Second,
        ConnectionTimeout: 30 * time.Second,
        })

        if err != nil {
                log.Fatal(err)
        }

        producer, err := client.CreateProducer(pulsar.ProducerOptions{
                Topic: "persistent://meetup/newjersey/first",
        })

        _, err = producer.Send(context.Background(), &pulsar.ProducerMessage{
    Payload: []byte("hello"),
})

defer producer.Close()

if err != nil {
    fmt.Println("Failed to publish message", err)
}
fmt.Println("Published message")


}
