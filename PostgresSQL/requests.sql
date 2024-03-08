-- Get all tasks for a specific user.
SELECT title FROM task WHERE user_id = 7;

-- Select tasks by a specific status.
SELECT title FROM task WHERE status_id = 1;

-- Update the status of a specific task.
UPDATE task SET status_id = 3 WHERE status_id = 2;

-- Get a list of users who have no tasks.
SELECT fullname FROM users WHERE id NOT IN (SELECT user_id FROM task);

-- Add a new task for a specific user.
INSERT INTO task (title, description, status_id, user_id)
VALUES ('work hard', 'work hard means no lunch and 60h work week', 1, 3);

-- Get all tasks that are not yet completed.
SELECT title FROM task WHERE status_id <> 3;

-- Delete a specific task. Use DELETE to remove a task by its id.
DELETE FROM task WHERE id = 3;

-- Find users with a specific email. Use SELECT with a LIKE condition to filter by email.
SELECT * FROM users WHERE email LIKE '%52@%';

-- Update a user's name. Change the user's name using UPDATE.
UPDATE users SET fullname = 'Alex String' WHERE id = 1;

-- Get the number of tasks for each status. Use SELECT, COUNT, GROUP BY to group tasks by statuses.
SELECT status_id, COUNT(title) FROM task GROUP BY status_id;

-- Get tasks assigned to users with a specific domain part of the email.
SELECT t.title, u.fullname
FROM task t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- Get a list of tasks that do not have a description. Select tasks that lack a description.
SELECT * FROM task WHERE description IS NULL;

-- Select users and their tasks that are in 'In Progress' status.
SELECT u.fullname, t.title
FROM users u
JOIN task t ON u.id = t.user_id
WHERE t.status_id = 2;

-- Get users and the number of their tasks. Use LEFT JOIN and GROUP BY to select users and count their tasks.
SELECT u.fullname, COUNT(t.title)
FROM users u
LEFT JOIN task t ON u.id = t.user_id
GROUP BY u.fullname;
