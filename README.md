# wednesday-bot
Never forget a Wednesday again!

An AWS Lambda function that logs into a Discord bot and posts a custom Wednesday message.

## Setup
First, run the following to create a settings file:

```
cp .env.example .env
```

Add your bot token/channel ID to this file.


Then, edit whatever message you want the bot to say in `wednesday/wednesday.txt`.

## Build

Too build your lambda function, run:

```
python setup.py ldist
```

A .zip file will be generated in `/dist`.
