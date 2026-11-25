# GitHub Upload Steps

## Option A: Upload using the GitHub website

1. Sign in to your GitHub account.
2. Click **New repository**.
3. Enter repository name: `Python-Activity-Based-Learning`.
4. Choose Public or the visibility required by your faculty.
5. Click **Create repository**.
6. Extract this ZIP file on your computer.
7. Open the extracted `Python-Activity-Based-Learning` folder.
8. In the GitHub repository, choose **Add file → Upload files**.
9. Select all folders and files inside the extracted folder, including `README.md`, all 10 project folders, `Consolidated_Report.pdf`, and `GITHUB_STEPS.md`.
10. Wait for upload to finish, enter commit message `Add Python ABL assignment`, and click **Commit changes**.
11. Copy the repository URL and submit it to your Python Programming faculty member / Lab Mentor.

## Option B: Upload using Git in VS Code terminal

Open the extracted project folder in VS Code and run these commands:

```bash
git init
git add .
git commit -m "Add Python ABL assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Python-Activity-Based-Learning.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username. If Git asks you to sign in, complete the GitHub sign-in prompt.

## Before submitting

- Confirm the repository is named exactly `Python-Activity-Based-Learning`.
- Open each `main.py` and run it.
- Make sure the README contains your correct student details.
- Be ready to explain the algorithm, code, test cases, and output for all 10 projects.
