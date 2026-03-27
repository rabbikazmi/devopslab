
#exp39.py
import psutil
import datetime
import logging
import random
from git import Repo

# Setup logging
logging.basicConfig(
    filename="report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

REPORT_FILE = "devops_report.txt"

# System metrics
def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

# CI/CD simulation
def simulate_pipeline_status():
    build_status = random.choice(["SUCCESS", "FAILED"])
    test_status = "PASSED" if build_status == "SUCCESS" else "SKIPPED"
    deploy_status = "DEPLOYED" if test_status == "PASSED" else "NOT DEPLOYED"
    return build_status, test_status, deploy_status

# REAL GitHub/Git data
def get_git_info():
    try:
        repo = Repo(".")   # current folder
        branch = repo.active_branch.name
        commit = repo.head.commit

        return {
            "repo_path": repo.working_dir,
            "branch": branch,
            "last_commit": commit.message.strip(),
            "author": commit.author.name,
            "commit_count": len(list(repo.iter_commits()))
        }
    except Exception as e:
        return {
            "repo_path": "Not a git repo",
            "branch": "-",
            "last_commit": "-",
            "author": "-",
            "commit_count": 0
        }

# Generate report
def generate_report():
    print("Generating DevOps Report...\n")
    logging.info("Report generation started")

    cpu, memory, disk = get_system_metrics()
    build, test, deploy = simulate_pipeline_status()
    git = get_git_info()
    now = datetime.datetime.now()

    try:
        with open(REPORT_FILE, "w") as f:
            f.write("========== DEVOPS REPORT ==========\n")
            f.write(f"Date & Time: {now}\n\n")

            # Git Section
            f.write("---- GIT (SCM) INFO ----\n")
            f.write(f"Repository Path : {git['repo_path']}\n")
            f.write(f"Branch          : {git['branch']}\n")
            f.write(f"Last Commit     : {git['last_commit']}\n")
            f.write(f"Author          : {git['author']}\n")
            f.write(f"Total Commits   : {git['commit_count']}\n\n")

            # Pipeline Section
            f.write("---- PIPELINE STATUS ----\n")
            f.write(f"Build Status    : {build}\n")
            f.write(f"Test Status     : {test}\n")
            f.write(f"Deploy Status   : {deploy}\n\n")

            # System Metrics
            f.write("---- SYSTEM METRICS ----\n")
            f.write(f"CPU Usage       : {cpu}%\n")
            f.write(f"Memory Usage    : {memory}%\n")
            f.write(f"Disk Usage      : {disk}%\n\n")

            # Health
            f.write("---- HEALTH STATUS ----\n")
            if cpu > 80 or memory > 80 or disk > 80:
                f.write("System Status   : WARNING (High Usage)\n")
            else:
                f.write("System Status   : HEALTHY\n")

        print("Report generated successfully!")
        logging.info("Report generated successfully")

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

# Run
if __name__ == "__main__":
    generate_report()