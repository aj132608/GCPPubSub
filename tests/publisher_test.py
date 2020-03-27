from publisher import Publisher


if __name__ == "__main__":
    project_id = 'pub-sub132608'
    topic_name = 'hello-topic'
    subscription_name = 'sub_one'
    message = b'Alex is pretty great'
    metadata = {
        "sender": "app",
        "vehicle_id": "V-1",
        "changed_val": "True"
    }

    publisher = Publisher(project_id, topic_name)

    print("\t\t\tPublish Test\n")

    print(f"Sending {message} to {subscription_name}\n")

    try:
        publisher.publish_message(subscription_name, message, metadata=metadata)
        print("Message successfully sent!\n")
    except Exception as e:
        print("Message was not successfully sent.")
        print(f"Exception: {e}\n")

    print("\t\t\tTopic Creation Test\n")

    print(f"Creating topic named topic-tester\n")
    topic_name = publisher.get_topic(project_id, 'topic-tester')
    print(topic_name)
    response = publisher.create_topic(topic_name)
    print(f"Response: {response}\n")

    print("\t\t\tTopic Deletion Test\n")

    print(f"Deleting topic named topic-tester\n")
    print(topic_name)
    publisher.delete_topic(topic_name)
    print(f"Success!")
