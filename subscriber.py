from google.cloud import pubsub_v1
import time


if __name__ == "__main__":
    project_id = 'pub-sub132608'
    topic_name = 'projects/pub-sub132608/topics/hello-topic'
    subscription_name = 'sub_one'

    print(f"Listening for messages on {subscription_name}")
    print("...")
    while True:
        try:
            subscriber = pubsub_v1.SubscriberClient()

            subscription_path = subscriber.subscription_path(
                project_id, subscription_name
            )


            def callback(message):
                print(f"Received message: {message.data}")
                message.ack()


            streaming_pull_future = subscriber.subscribe(
                subscription_path, callback=callback
            )

            try:
                streaming_pull_future.result(timeout=0)
            except Exception as e:  # noqa
                # print(f"Exception: {e}")
                streaming_pull_future.cancel()
        except KeyboardInterrupt:
            print("Closing Subscriber.")

        time.sleep(5)
