# CollaborativeContentRecs

Project Setup Instructions

Prerequisites

Before running this project, ensure you have the following installed and set up on your system:
- [Docker](https://www.docker.com/) (must be installed and active)
- [Visual Studio Code (VSC)](https://code.visualstudio.com/)

Setting Up the Project

1. Open the Project in Visual Studio Code
   - Launch VSC and open the project folder.
   - You will see a notification prompting you to open the project in a container.
   - Click on "Reopen in Container".

2. Copy CSV Files to the Container
   - After the container is running, you need to move the .csv files into the root directory of the container.
   - Use the terminal and run the following command, replacing <container_id> with your actual container ID:
     docker cp <file_name>.csv <container_id>:/root/
   - To find your container ID, you can run:
     docker ps
     This will list all running containers along with their IDs.

3. Run the Code
   - Once the .csv files are inside the container, you can proceed to run the project as needed. 

Notes

- Ensure that Docker is running before attempting to open the project in a container.
- Make sure the .csv files are correctly copied to /root/ before running the code.
