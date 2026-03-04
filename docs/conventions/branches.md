# Git Branches for this project
Each branch name should consist of two parts, a **prefix** and a **suffix**.
The prefix shows the type of addition to the project, and the suffix is the title. Both are separated with a `/`.
### Example
- `docs/conventions` - For adding to or modifying the current rules for this repo

- `tl/de` - For adding to or modifying the translations to German

This way, we can be more flexible within Git itself. For example, from the terminal we can use wildcards to list all the branches under a certain prefix using `git branch --list *[prefix]/*"`

It also allows us to more clearly split responsibilities between group members. One person can focus on the branches under the `design` prefix, while another specialises in the `docs` branches.

## Suffix naming conventions
// TODO

## Prefix Dictionary

| Prefix   | Definition                                                          |
|----------|---------------------------------------------------------------------|
| `base`   | Changes to the core of the website (e.g base.html, routes etc.)     |
| `design` | Changes to website design (e.g per-locale or global CSS and images) |
| `docs`   | Changes to documentation                                            |
| `wip`    | Boilerplate additions (e.g setting up Flask for the first time)     |

