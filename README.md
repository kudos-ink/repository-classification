# Repositories Classification

This repository serves a collection of JSON files intended for use by the Kudos Portal.

## Filters

![Kudos portal's filters](images/kudos-filters.png)

- [interests.json](interests.json) will be used in "Interests"
- [languages.json](languages.json) will be used in "Languages"
- [repository_full.json](repository_full.json) will be used in "Projects"

## Issues

![Kudos portal's issues](images/kudos-issues.png)

Issues from repositories listed in [repository_full.json](repository_full.json) are retrieved by our backend services and displayed on the portal. Only repositories with a valid internal "id" are processed, a task manually carried out by the maintainers.

## Add your repository

![Add your project in Kudos (1)](images/kudos-add-1.png)

![Add your project in Kudos (2)](images/kudos-add-2.png)

When you click on any "Include your project" button, an issue will be opened, ready to be completed with your repository information.

![Add your project in Kudos](images/kudos-add.png)

Once submitted, the maintainers will review the submission, and it will then be included in our [repository_full.json](repository_full.json) file. The new issues associated with it will subsequently be displayed on our main portal. We will notify you through the issue when it is ready!
