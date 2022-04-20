# Catmostphere
A management software for small coffee shop (I just like this name so nothing else)

## Basic introduction
- The program used a simplified MVC (model-view-controller) model ([Check out this link for more](https://www.freecodecamp.org/news/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053/))
- Since the data is relatively small, I decide not to use any database system so we don't have to learn anything new (**Note**: The code is designed in WSL (windows subsystem linux) so if you run this in window, you might want to check the path string in files (linux user '/' instead of '\\' so maybe it won't run)

| Section    |  Functional Duty                                |
| ---------- | ----------------------------------------------- |
| model      | handling the business logic and modify the data |
| view       | handling the end user I/O and interface         |
| controller | acting as the bridge between the other two      |

## Packages
- tkinter
- screeninfo