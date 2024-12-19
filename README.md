# Todo Flask App

# Index 
1. Getting started with the project
2. Task Objectives and an Overview

# 1. Getting started with the project
1. Open app.py and change:
   - Line 256 = port for the application to run on 
   - Line 257 = host IP address for the application to run on
2. Run the program by using 
   > 'Python3 app.py'

# 2. Task objectives
## Task Objectives 
> A full PDF copy can be found in the root directory, called 'Flask Task.pdf'

### Task Management
- Users should be able to:
  - Add tasks with a description, priority level and deadline.
  - View tasks in a list format, sorted by priority or deadline.
  - Edit existing tasks (update description, deadline or priority)
  - Delete tasks
  
### Deadline Countdown
- Display time remaining for each task:
  - More than 1 day remaining:
    - Show the countdown in years, months and days.
  - Less than 1 day remaining
    - Highlight the task with a red background or color.
    - Display a live, updating countdown in hours, minutes and seconds

### Priority Levels
- Allow users to assign priority levels to each task (e.g. low, medium or high)
- Display tasks with a coloured label or icon to indicate priority.
  - Green for low.
  - Yellow for medium.
  - Red for high

### Task completion
- Add a feature to mark tasks as completed.
- Completed tasks:
- Are moved to a separate section (e.g. "Completed Tasks").
- Show the deadline as "Completed on [date/time].