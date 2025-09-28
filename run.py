import subprocess

print("📦 Setting up database...")
subprocess.run(["python", "db_setup.py"])

print("🚀 Starting PlacementApp...")
subprocess.run(["python", "app.py"])
