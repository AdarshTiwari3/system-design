# Design a Stack Overflow

### Requirements 

1. Users should be able to ask questions, answer them, and leave comments on both questions and answers.

2. Users can also upvote or downvote questions and answers.

3. Each question should have related tags for better organization.

4. Users should be able to search for questions using keywords, tags, or by looking up specific user profiles.

5. The system should maintain a reputation score for users, based on their activity and the quality of their contributions.

6. The system must support multiple users accessing it at the same time, while keeping all data accurate and consistent.


## Identify Core Objects

### 1. User
Represents a person using the platform, with a unique ID, username, reputation score.

### 2. Question
A post created by a user asking for help or information. Contains title, body, tags, list of answers, votes, and comments.

### 3. Answer
A reply to a question posted by another user. Can be upvoted, downvoted, commented on, and marked as an accepted answer.

### 4. Tag
A label attached to questions for categorization and improved search, e.g., `Python`, `LLD`, `System Design`.

### 5. VoteType
Enum defining valid vote types:
- `UPVOTE`
- `DOWNVOTE`

### 6. Comment
A short text added to a question or answer for clarification or discussion.

---

## Additional Notes (Short)

- Use an **Observer** to update reputation when votes and accepted answers occur.  
- Use a **Strategy** pattern for searching questions (by keyword, tag, or user).  
- A **Facade** can expose simple operation(ask question, answer, vote, comment, search).  
- Use thread-safe operations or locks for vote and reputation consistency.

---