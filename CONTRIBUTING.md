# How To Contribute

## Step 1 - Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Step 2 - Clone the forked repository

Now clone the forked repository to your machine:

- Using HTTPS


```sh
git clone "https://GitHub.com/<your-username>/intro.py.git"
```

- Using SSH

```sh
git clone "git@GitHub.com:<your-username>/intro.py.git"
```

**Note**: Replace <your-username> with your GitHub username.

## Step 3 - Create a branch

Change the current working directory to the cloned repo.
For example:

```sh
cd intro.py
```

Now create a new branch with the below naming convention:

```sh
git switch -c add-your-branch-name
```

For example:

```sh
git switch -c django-fileupload-feature
```

## Step 3 - Make changes and commit

- Add extra features in Django Application.

Now if you go to the project directory and enter the command `git status`, you can see the changes.

Add those changes with the `git add` command:

```sh
git add -A
```

Now commit those changes using the `git commit` command:

```sh
git commit -m "Documment Your Commit"
```

For example:

```sh
git commit -m "File Upload feature completed"
```

## Step 4 - Push the changes to GitHub

Push your changes to GitHub using the `git push` command:

```sh
git push -u origin <your-branch-name>
```

For example:

```sh
git push -u origin django-fileupload-feature
```

> If you enabled two-factor authentication in your GitHub account you won't be able to push via HTTPS using your accounts password. Instead you need to generate a personal access token. This can be done in the application settings of your GitHub account. Using this token as your password should allow you to push to your remote repository via HTTPS. Use your username as usual.

[Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Step 5 - Submit your changes for review

If you go to your repository page on GitHub you will see a `compare & pull request` button. Click that button.
And submit the pull request.
Soon the reviewer will merge the branch into `main`.

