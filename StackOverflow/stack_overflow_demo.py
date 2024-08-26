from stack_overflow import StackOverflow

class StackOverflowDemo:
    @staticmethod
    def run():
        system = StackOverflow()

        # Create users
        alice = system.createUser("Alice", "alice@example.com")
        bob = system.createUser("Bob", "bob@example.com")
        charlie = system.createUser("Charlie", "charlie@example.com")

        # Alice asks a question
        java_question = system.askQuestion(alice, "What is polymorphism in Java?",
                                            "Can someone explain polymorphism in Java with an example?",
                                            ["java", "oop"])

        # Bob answers Alice's question
        bob_answer = system.answerQuestion(bob, java_question,
                                            "Polymorphism in Java is the ability of an object to take on many forms...")

        # Charlie comments on the question
        system.addComment(charlie, java_question, "Great question! I'm also interested in learning about this.")

        # Alice comments on Bob's answer
        system.addComment(alice, bob_answer, "Thanks for the explanation! Could you provide a code example?")

        # Charlie votes on the question and answer
        system.voteQuestion(charlie, java_question, 1)  # Upvote
        system.voteAnswer(charlie, bob_answer, 1)  # Upvote

        # Alice accepts Bob's answer
        system.acceptAnswer(bob_answer)

        # Bob asks another question
        python_question = system.askQuestion(bob, "How to use list comprehensions in Python?",
                                            "I'm new to Python and I've heard about list comprehensions. Can someone explain how to use them?",
                                            ["python", "list-comprehension"])

        # Alice answers Bob's question
        alice_answer = system.answerQuestion(alice, python_question,
                                            "List comprehensions in Python provide a concise way to create lists...")

        # Charlie votes on Bob's question and Alice's answer
        system.voteQuestion(charlie, python_question, 1)  # Upvote
        system.voteAnswer(charlie, alice_answer, 1)  # Upvote

        # Print out the current state
        print(f"Question: {java_question.title}")
        print(f"Asked by: {java_question.author.username}")
        print(f"Tags: {', '.join(tag.name for tag in java_question.tags)}")
        print(f"Votes: {java_question.getVoteCount()}")
        print(f"Comments: {len(java_question.getComments())}")
        print(f"\nAnswer by {bob_answer.author.username}:")
        print(bob_answer.content)
        print(f"Votes: {bob_answer.getVoteCount()}")
        print(f"Accepted: {bob_answer.is_accepted}")
        print(f"Comments: {len(bob_answer.getComments())}")

        print("\nUser Reputations:")
        print(f"Alice: {alice.reputation}")
        print(f"Bob: {bob.reputation}")
        print(f"Charlie: {charlie.reputation}")

        # Demonstrate search functionality
        print("\nSearch Results for 'java':")
        search_results = system.searchQuestions("java")
        for q in search_results:
            print(q.title)

        print("\nSearch Results for 'python':")
        search_results = system.searchQuestions("python")
        for q in search_results:
            print(q.title)

        # Demonstrate getting questions by user
        print("\nBob's Questions:")
        bob_questions = system.getQuestionsByUser(bob)
        for q in bob_questions:
            print(q.title)

if __name__ == "__main__":
    StackOverflowDemo.run()