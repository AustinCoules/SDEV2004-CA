# Git Branches
Each branch name should consist of two parts, a **prefix** and a **suffix**.
The prefix shows the type of addition to the project, and the suffix is the title. Both are separated with a `/`, and branches can have multiple suffixes depending on the scope.

### Example
- `docs/conventions` - For adding to or modifying the current rules for this repo
- `tl/de` - For adding to or modifying the translations to German
- `design/navigation/en` - For adding to or modifying the navigation bar for the English version of the website

This way, we can be more flexible within Git itself. For example, from the terminal we can use wildcards to list all the branches under a certain prefix using `git branch --list *[prefix]/*"`

It also allows us to more clearly split responsibilities between group members. One person can focus on the branches under the `design` prefix, while another specialises in the `docs` branches.

## Suffix naming conventions
The suffix is essentially the individual branch itself. Therefore, it should be named after the broad change you are intending to make.
This is **not** the same as commit messages; the branch name should not include aspects such as file names or verbs. If commit messages are to-do list items, branch names are the name of the to-do list itself.

Suffix names should be all lowercase and use `-` as spaces.

### Example
- `wip/flask-setup` - This branch sets up Flask and initial routes for the site.
- `docs/report/ind-austin-coules` - This branch is where Austin will work on their individual reports.

## How to use branches in Git
// TODO

## Prefix Dictionary
| Prefix   | Definition                                                                                                                 |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| `base`   | Changes to the core of the website (e.g base.html, routes etc.)                                                            |
| `design` | Changes to website design (e.g per-locale or global CSS and images)                                                        |
| `docs`   | Changes to documentation                                                                                                   |
| `html`   | Changes to HTML templates (e.g navigation.html)                                                                            |
| `tl`     | Changes to translations (e.g de/messages.po)                                                                               |
| `wip`    | Boilerplate additions (e.g setting up Flask for the first time) or changes that fall outside of the other given categories |
