# CIS322E

## Set up Git config and SSH keys in Bitbucket
1. Download latest git bash from the [Git website](https://git-scm.com/install/).
2. Open git bash terminal.
3. Set your username and email by executing the following commands:
   - git config --global user.name "\<First and Last name>"
   - git config --global user.email "\<your Master's email>"
4. Execute: 'ssh-keygen -t ed25519 -C "\<your Master's email>"' to create a new SSH key using your email.
5. Execute 'cat ~/.ssh/id_ed25519.pub' to show your public SSH key value.
6. Copy the value.
7. In your web brower, go to the settings of the TMU CIS322 workspace: "https://bitbucket.org/account/settings/ssh-keys/".
8. Click the "Add key" button.
9. Under label, write "laptop git" to identify the key.
10. Paste the copied SSH public key value from step 5 in the the "Key" field.

## Clone the Bitbucket repository
1. In your web browser, navigate to the class repository from "https://bitbucket.org/cis322e_sp26/cis322e_sp26/src/main/".
2. The "Source" tab should be selected on the left sidebar. On the right of the screen, click on the "Clone" button.
3. In the dropdown menu, select "SSH".
4. Click on the copy button to the right of the text input bar.
5. Create a "Docker" folder on your computer (recommend inside your Documents folder).
6. Open a git bash terminal inside the newly created "Docker" folder.
7. Execute the command: "git config --global core.autocrlf false".
8. Paste the copied git clone command into the terminal and press [Enter] to execute.

## Setup Docker Container Environment
1. Download Docker Desktop for [Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [Mac](https://docs.docker.com/desktop/setup/install/mac-install/), or [Linux](https://docs.docker.com/desktop/setup/install/linux/).
2. During installation, make sure to add Docker to your PATH.
3. Open the VS Code application.
4. Open a git bash terminal ("Terminal" >> "New Terminal")
5. [Optional] If git bash terminal is not configured, press [Ctrl]+[Shift]+P, then type in "Terminal: Set Default Profile". Choose the git bash exe as the default terminal.
6. Execute this command in git bash to download the docker image: `docker pull therealhoneybadger/tmu_cis322:sp2026v1.1`
7. In the very bottom left of the VS Code window, click on the "><" button.
8. In the dropdown menu that appears, select "Reopen in Container".
9. After a moment, the Docker container is up and running. (if you are on a Mac, you may have to modify the devcontainer.json file from "localEnv:USERPROFILE" to "localEnv:HOME")
10. Open a terminal and verify the python version is 3.10.16 using `python --version`.
11. Also verify that your ssh keys are working properly using "git fetch" (there should be no warnings or errors).

## Web UI (full-stack wrapper around existing game logic)

This repository now includes a lightweight web layer that keeps existing game logic in `src/cardgames/*` intact.

- Backend API: `src/cardgames/webapp.py` (FastAPI)
- Frontend page: `src/cardgames/web/index.html`

Run locally with Docker:

1. Build image
   - `docker build -t cis322e_sp26:local .`
2. Start API + UI server (port 8000)
   - `docker run --rm -p 8000:8000 -v "$PWD":/work -w /work cis322e_sp26:local uvicorn cardgames.webapp:app --app-dir /work/src --host 0.0.0.0 --port 8000 --reload`
3. Open in browser
   - `http://localhost:8000`

Quick API check:

- `POST /api/games` creates a new game
- `POST /api/games/{id}/player1-choice` stores Player 1 card choice
- `POST /api/games/{id}/player2-choice` applies `switch_turn` logic, hides Player 1 card, and completes the round