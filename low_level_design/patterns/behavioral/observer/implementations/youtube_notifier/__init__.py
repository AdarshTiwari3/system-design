"""
Example: YouTube Notification System using Observer Design Pattern

Scenario:
---------
When a YouTube channel uploads a new video, all users who have subscribed 
to that channel receive a notification.

Roles:
------
1. Subscriber (User) - The observer:
   - Subscribes to a YouTube channel to get updates.
   - Can unsubscribe anytime to stop receiving notifications.

2. Publisher (YouTube Channel) - The subject:
   - Maintains a list of subscribers.
   - Can add (attach) or remove (detach) subscribers.
   - Notifies all subscribers whenever a new video is uploaded.

Workflow:
---------
- User clicks 'Subscribe' → Added to the channel's subscriber list.
- User clicks 'Unsubscribe' → Removed from the channel's subscriber list.
- Channel uploads a new video → Sends notifications to all current subscribers.

This design follows the Observer Pattern:
- Loose coupling between publisher and subscribers.
- Easy to add/remove subscribers without changing the publisher's code.

"""
