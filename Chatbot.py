def chatbot():

    print("\n" + "=" * 200)
    print(" CONVERSATION HUB STARTED 🌟")
    print("🤖 Your digital companion is online.")
    print(" Ask me about CodeAlpha, internships, projects, and more!")
    print(" Type 'bye' whenever you'd like to leave.")
    print("=" * 200)

    while True:
        user = input("\n You: ").lower().strip()

        # Greetings
        if user in ["hello", "hi", "hey"]:
            print("\n Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("\n Bot: I'm fine, thanks! What about you?")

        elif user in ["i am fine", "im fine", "i'm fine", "fine"]:
            print("\n Bot: That's great to hear! ")

        elif user in ["good", "great", "awesome", "excellent"]:
            print("\n Bot: Wonderful! Keep smiling.")

        elif user in ["bad", "sad", "not good"]:
            print("\n Bot: I'm sorry to hear that. Hope things get better soon.")

        # Personal Questions
        elif user == "what is your name":
            print("\n Bot: My name is CodeAlpha Chatbot.")

        elif user == "who created you":
            print("\n Bot: I was created using Python programming.")

        elif user == "what can you do":
            print("""
🤖 Bot:

I can:
• Greet users
• Answer simple questions
• Provide information about CodeAlpha
• Explain internships, certificates, and projects
• Tell a joke
• Have a basic conversation
""")

        # CodeAlpha Information
        elif "codealpha" in user:
            print("""
🤖 Bot:

🏢 About CodeAlpha

CodeAlpha is an organization that provides internship opportunities
for students and freshers to gain practical experience and improve
their technical skills.

📚 Domains Offered:
• Python Programming
• Java Programming
• Web Development
• Artificial Intelligence
• Machine Learning
• Data Science
• Cyber Security

🎯 Benefits:
• Real-world projects
• Skill development
• Internship certificates
• Portfolio building
• Industry exposure
""")

        # Internship Information
        elif "internship" in user:
            print("""
🤖 Bot:

📌 CodeAlpha Internship Program

• CodeAlpha provides virtual internship opportunities.
• Internships are designed for students and freshers.
• Participants work on practical tasks and projects.
• The internship helps improve technical and problem-solving skills.
• Interns gain hands-on experience in their chosen domain.
• It is a great opportunity to build confidence and industry knowledge.

✨ Popular Internship Domains:
Python, Java, Web Development, AI, ML,
Data Science, and Cyber Security.
""")

        # Certificate Information
        elif "certificate" in user:
            print("""
🤖 Bot:

🏆 Certificate Information

• Certificates are awarded after successful completion
  of internship tasks.

• The certificate validates your learning and effort.

• You can add it to:
  - Resume
  - LinkedIn Profile
  - Portfolio

• Certificates help demonstrate technical skills
  and project experience to employers.

🎓 A certificate can strengthen your professional profile.
""")

        # Project Information
        elif "project" in user:
            print("""
🤖 Bot:

💻 Project Information

• Interns work on practical and industry-related projects.
• Projects help improve coding and problem-solving skills.
• Each project focuses on applying theoretical knowledge.
• Projects can be included in your portfolio.
• Completing projects demonstrates dedication and technical ability.

🚀 Benefits of Projects:
• Hands-on experience
• Portfolio development
• Better understanding of technologies
• Improved confidence
""")

        # Joke
        elif "joke" in user:
            print("""
🤖 Bot:

😄 Why do programmers prefer dark mode?

Because light attracts bugs!
""")

        # Thank You
        elif user in ["thank you", "thanks"]:
            print("\n🤖 Bot: You're welcome! Happy to help. 😊")

        # Exit
        elif user == "bye":
            print("\n🤖 Bot: Goodbye! Have a wonderful day. 👋")
            break

        # Unknown Input
        else:
            print("""
🤖 Bot:

Sorry, I don't understand that.

💡 Try asking:
• What is CodeAlpha?
• Tell me about internships
• Tell me about certificates
• Tell me about projects
• Tell me a joke
• What can you do?
""")

# Run Chatbot
chatbot()