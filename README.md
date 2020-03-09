# GCPPubSub
A repo all about how to use Google's infamous Cloud PubSub service.

# Get Started

**Create your virtual environment named 'env'**

```
python -m venv env
```
**Activate the virtual environment**

```
C:/*PATH_TO_GITHUB_REPO*/pubsub_practice/env/Scripts/activate.bat
```

**Set environment variables**

```
set GOOGLE_APPLICATION_CREDENTIALS=C:/*PATH_TO_PUBSUB_JSON_CREDS*/PROJECT_ID-12_DIGIT_KEY.json

set PROJECT=PROJECT_ID
```

**Install dependencies**

```
pip install -r requirements.txt
```

# Run the Subscriber
#### What is a Subscriber?

A subscriber is used in a queueing model to retrieve messages from the queue and execute 
some command as a callback. A subscriber functions and exists completely uncoupled from the
publisher sending messages to the queue. In Google Cloud PubSub, subscribers are referred 
to as Subscribers and publishers are referred to as Topics. Subscribers have to 'subscribe'
to a Topic on creation.

#### How to run the Subscriber

```
python subscriber.py
```

#### What does this file do?

At the moment, the file instantaneously pulls all messages from the queue server and prints
the contents of the message it receives. 
