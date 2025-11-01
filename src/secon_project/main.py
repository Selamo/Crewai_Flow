from secon_project.crew import MyFirstCrew
def run():
    """
    Run the crew with a specific topic
    """
    # Define what topic we want to research and write about
    inputs = {
    'topic': 'artificial intelligence in healthcare'
    }
    # Create the crew and run it
    crew = MyFirstCrew().crew()
    result = crew.kickoff(inputs=inputs)
    # Print the final result
    print("\n\n========================")
    print("FINAL RESULT:")
    print("========================")
    print(result)
    
if __name__ == "__main__":
     run()