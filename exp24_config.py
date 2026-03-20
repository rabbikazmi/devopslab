config = {
    "APP_NAME": "DevOpsApp",
    "ENV": "development",
    "PORT": "8080"
}

with open(".env", "w") as f:
    for key, value in config.items():
        f.write(f"{key}={value}\n")

print(".env file generated successfully")