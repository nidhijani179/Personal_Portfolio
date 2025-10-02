#!/usr/bin/env python3
"""
Setup script for Nidhi Jani's Portfolio Website
"""

import os
import sys
import subprocess

def run_command(command):
    """Run a command and return success status"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🚀 Setting up Nidhi Jani's Portfolio Website...")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        sys.exit(1)
    
    print("✅ Python version check passed")
    
    # Create virtual environment
    print("📦 Creating virtual environment...")
    if not run_command("python -m venv venv"):
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    print("✅ Virtual environment created")
    
    # Activate virtual environment and install dependencies
    print("📥 Installing dependencies...")
    
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && pip install -r requirements.txt"
    else:  # macOS/Linux
        activate_cmd = "source venv/bin/activate && pip install -r requirements.txt"
    
    if not run_command(activate_cmd):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    print("✅ Dependencies installed")
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        print("⚙️ Creating .env file...")
        if os.path.exists('.env.example'):
            if os.name == 'nt':
                run_command("copy .env.example .env")
            else:
                run_command("cp .env.example .env")
            print("✅ .env file created from template")
        else:
            print("⚠️ .env.example not found, skipping .env creation")
    
    # Create necessary directories
    directories = [
        'static/images',
        'static/files',
        'static/css',
        'static/js'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("✅ Directory structure verified")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Add your images to static/images/")
    print("2. Add your resume PDF to static/files/")
    print("3. Update .env with your email configuration (optional)")
    print("4. Run the development server:")
    
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("   python run.py")
    print("\n🌐 Your portfolio will be available at: http://localhost:5000")

if __name__ == "__main__":
    main()