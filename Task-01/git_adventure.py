#!/usr/bin/env python3
"""
INFRIX INTERNSHIP - TASK 01
Git & Version Control Adventure
Author: Isba Noor Abbasi
Date: 7-June-2026
"""

import datetime
import subprocess
import os

class GitAdventure:
    """Your Git learning journey tracker"""
    
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.datetime.now()
        self.learnings = []
        
    def add_learning(self, concept, command):
        """Track what you learn"""
        self.learnings.append({
            'concept': concept,
            'command': command,
            'timestamp': datetime.datetime.now()
        })
        print(f"✅ Learned: {concept}")
        
    def show_progress(self):
        """Display your learning journey"""
        print("\n" + "="*60)
        print(f"🌟 {self.name}'s Git Learning Journey at Infrix")
        print("="*60)
        print(f"Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Concepts mastered: {len(self.learnings)}")
        
        print("\n📚 What I've Learned:")
        for i, item in enumerate(self.learnings, 1):
            print(f"  {i}. {item['concept']}")
            print(f"     Command: git {item['command']}")
            
    def celebrate(self):
        """Celebrate achievements"""
        print("\n" + "🎉" * 20)
        print("🎊 CONGRATULATIONS! 🎊")
        print("You've completed Task 01 - Git Mastery!")
        print("🎉" * 20)
        
        print("\n💪 You can now:")
        print("  • Time travel through your code (git log)")
        print("  • Create parallel universes (git branch)")
        print("  • Save checkpoints (git commit)")
        print("  • Collaborate like a pro!")
        
def run_git_command(command):
    """Run git command and show result"""
    try:
        result = subprocess.run(f'git {command}', shell=True, 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ git {command} - Success!")
            return True
        else:
            print(f"✗ Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    print("\n🚀 INFRIX AI & AUTOMATION INTERNSHIP")
    print("="*40)
    
    # Get your name
    name = input("\nWhat's your name? ").strip() or "Intern"
    
    # Create your adventure
    adventure = GitAdventure(name)
    
    print(f"\n🎮 Welcome {name}! Let's start your Git adventure...")
    
    # Show initial status
    print("\n📊 Current Git Status:")
    run_git_command("status")
    
    # Track learnings
    print("\n📝 Let's track what you'll learn today:")
    
    adventure.add_learning("Initialize a repository", "init")
    adventure.add_learning("Check repository status", "status")
    adventure.add_learning("Add files to staging", "add <file>")
    adventure.add_learning("Commit changes", "commit -m 'message'")
    adventure.add_learning("View commit history", "log --oneline")
    
    # Show progress
    adventure.show_progress()
    
    # Git fun facts
    print("\n🎯 Did You Know?")
    facts = [
        "Git can track who changed what and when!",
        "You can undo almost anything in Git!",
        "Git was created in just 2 weeks!",
        "The Git logo is actually called 'git'!"
    ]
    import random
    print(f"  💡 {random.choice(facts)}")
    
    # Congratulations
    adventure.celebrate()
    
    # Next steps
    print("\n📋 NEXT STEPS:")
    print("  1. Run: git log --oneline --graph")
    print("  2. Create a branch: git checkout -b my-feature")
    print("  3. Make another commit on your new branch")
    print("  4. Take a screenshot of your git graph")
    
    print("\n✨ You're now ready for Task 02 at Infrix! ✨")

if __name__ == "__main__":
    main()