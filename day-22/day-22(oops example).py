'''
Think About the System First (High-Level Design)

Ask yourself:

Who are the main users?
voters

What actions happen in the system?

displaying of parties then voters adding
their vote to a particular party next adding votes to respective party

👉 For an Online Voting System, typical components:

Voters
Candidates
Elections
Votes
Admin (optional)

Base Class
User (Abstract Class)
Attributes: name, id, age
Method: display_info()

Voter (inherits User)
Attributes: voter_id, has_voted
Methods: vote()
Candidate (inherits User)
Attributes: party, vote_count
Methods: add_vote()

class User:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def display_info(self):
        print(f'User details: Name:{self.name}, ID:{self.id}, Age:{self.age}')

class Voter(User):
    def __init__(self,name,id,age,voter_id,has_voted):
        super.__init__(name,id,age)
        self.voter_id = voter_id
        self.has_voted = has_voted

    def vote(self):
        print("Voter_id: {self.voter_id}, Has_voted: {self.has_voted}")

class Candidate(User):
    def __init__(self,party, vote_count):
        self.vote_count = 0
        self.party = {}
        self.vote_count += has_voted

    def add_vote():
        
'''

class User:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def display_info(self):
        print(f'User details: Name:{self.name}, ID:{self.id}, Age:{self.age}')


class Voter(User):
    def __init__(self,name,id,age,voter_id):
        super().__init__(name,id,age)
        self.voter_id = voter_id
        self.__has_voted = False

class Candidate(User):
    def __init__(self,name,id,age,party):
        super().__init__(name,id,age)
        self.party = party
        self.vote_count = 0
        
    def add_vote(self,vote_count):
            self.__vote_count += 1
        
        
class Election():
    def __init__(self):
        self.voters = []
        self.candidates = []
        
    def add_candidate(self,candidate):
        self.candidates.append(candidate)
        
    def register_voter(self,voter):
        self.voters.append(voter)

    def cast_vote(self,voter,candidate):
        if not voter.has_voted_status():
            candidate.add_vote()
            voter.__has_voted = True
        else:
            print("Already voted")
        

        

