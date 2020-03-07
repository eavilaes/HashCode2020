import sys

class Book:
    def __init__(self, score, id):
        self.score = score
        self.id = id

class Library:
    def __init__(self, id, books, signupTime, booksPerDay):
        self.id = id
        self.books = books
        self.signupTime = signupTime
        self.booksPerDay = booksPerDay
        self.points = 0
    def score(self):
        sum=0
        for b in books:
            sum+=b.score
        return sum
    def orderB(self):
        books.sort(key=lambda b: b.score, reverse = True)


#Main code
_in = open(str(sys.argv[1]), "r") #Open input file
out = open(str(sys.argv[1])[:-3]+".out", "w") #Output file .out

nBooks, nLibraries, nDays = _in.readline().split(" ") #First line variables
# nBooks = int(nBooks) #This is not used
nLibraries = int(nLibraries)
nDays = int(nDays)

booksS = _in.readline().split(" ") #Scores of the books
booksSint = []
for n in booksS:
    booksSint.append(int(n))

books = []  #Array of Book objects
i=0
for b in booksSint:
    b1 = Book(b,i)
    books.append(b1)
    i+=1

libraries = []
for li in range (0, nLibraries): #Each Library block of the input (2 lines)
    booksN, signupD, booksPerD = _in.readline().split(" ")
    booksN = int(booksN)
    signupD = int(signupD)
    booksPerD = int(booksPerD)

    #Read books ids of the library
    booksIdsL = _in.readline().split(" ")
    booksIdsLint = []
    for b in booksIdsL:
        booksIdsLint.append(int(b))

    booksArr = []
    for i in booksIdsLint:
        booksArr.append(books[i])

    l1 = Library(li, booksArr, signupD, booksPerD)
    libraries.append(l1)

#3 copies of the libraries to calculate the score of each library
timeA, scoreA, efficA = libraries, libraries, libraries

for i in range(1, len(timeA)):
    clave = timeA[i]
    j=i-1
    while (j>=0 and timeA[j].signupTime > clave.signupTime):
        timeA[j+1] = timeA[j]
        j=j-1
    timeA[j+1] = clave

for i in range(1, len(scoreA)):
    clave = scoreA[i]
    sc = clave.score()
    j=i-1
    while (j>=0 and scoreA[j].score() > sc):
        scoreA[j+1] = scoreA[j]
        j=j-1
    scoreA[j+1] = clave

for i in range(1, len(efficA)):
    clave = efficA[i]
    j=i-1
    while( j>=0 and efficA[j].booksPerDay > clave.booksPerDay):
        efficA[j+1] = efficA[j]
        j=j-1
    efficA[j+1] = clave

#Add up scores
for x in range (0, len(libraries)-1):
    libraries[timeA[x].id].points+=(len(libraries)-x)*2
    libraries[scoreA[x].id].points+=x
    libraries[efficA[x].id].points+=x

#Sort the libraries depeinding on their points
libraries.sort(key=lambda l: l.points, reverse = False)

#Get the libraries for the output
daysSpent=0
i=0
librariesOut = []
while daysSpent<nDays and i<len(libraries):
    if(libraries[i].signupTime < nDays-daysSpent):
        daysSpent+=libraries[i].signupTime
        librariesOut.append(libraries[i])
    i+=1

#Get the books for each library (ordering them)
#Print the output
out.write(str(len(librariesOut))+"\n")
for l in librariesOut:
    l.orderB()
    out.write(str(l.id) + " " + str(len(l.books)) +  "\n")
    for b in l.books:
        out.write(str(b.id) + " ")
    out.write("\n")

_in.close()
out.close()


