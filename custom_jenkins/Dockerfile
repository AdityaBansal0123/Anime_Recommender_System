# Use the Long Term Support version of Jenkins
FROM jenkins/jenkins:lts

# Switch to root to install system packages
USER root

# 1. Update apt
# 2. Install prerequisites (Removed 'software-properties-common' to fix your error)
# 3. Add Docker's official GPG key
# 4. Set up the Docker repository
#    NOTE: We use "bookworm" here. Your base image is Debian Trixie (13), 
#    but Docker doesn't have a stable Trixie repo yet. Bookworm (12) is the 
#    safest compatible version.
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    bookworm stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# CRITICAL: Add the 'jenkins' user to the 'docker' group
# This allows Jenkins to run "docker build" without permission errors
RUN usermod -aG docker jenkins

# Switch back to the standard jenkins user
USER jenkins

# (Optional) Install Jenkins plugins via CLI if you have a plugins.txt
# COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt