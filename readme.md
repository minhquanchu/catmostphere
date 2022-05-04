# Catmostphere

A management software for small coffee shop (I just like this name so nothing else)

## Basic introduction

- The program used a simplified MVC (model-view-controller)
  model ([Check out this link for more](https://www.freecodecamp.org/news/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053/))
- Since the data is relatively small, I do not to use any database system so we don't have to learn anything new

| Section    |  Functional Duty                                |
| ---------- | ----------------------------------------------- |
| model      | handling the business logic and modify the data |
| view       | handling the end user I/O and interface         |
| controller | acting as the bridge between the other two      |

## UI Packages (need votes)

- tkinter
- kivy

## view

- Login window:
    - take username and password, alert user if username or password is incorrect
    - check if user is admin or not:
        - if yes, add an admin option setting to menu window
- Menu window:
    - display menu items as button (to order same items multiple times, press the item again)
    - logout button
    - admin button, direct user to admin menu
    - next button to get to receipt
    - after finishing choosing, press next button to show the invoice window
- Receipt windows:
    - show invoice
    - invoices should include:
        + items order with (individual price and quantity)
        + cashier
        + time (hh:mm dd/mm/yyyy)
        + customer order note (string)
        + total
    - checkout button to complete the order. When pressed, send user back to menu window and shows an popup alert
      verifying the order completion
    - return button to return menu

- Admin window (optional):
    - show list of current employees
    - add button to add new user to users -> direct to a window to fill in new user info
    - next button to move to ledger -> direct to a new window that shows revenue and item sale
    - back button to return to menu