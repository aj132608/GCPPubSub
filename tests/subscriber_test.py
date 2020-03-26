from subscriber import Subscriber

if __name__ == "__main__":
    project_id = 'pub-sub132608'
    subscription_name = 'sub_one'

    subscriber = Subscriber(project_id, subscription_name)

    subscriber.start_server()
