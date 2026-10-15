// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
// paste your drop and insertMany commands here
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)
 

// Step 4: load books.json
// paste your drop and insertMany commands here
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)


// Step 5: list authors and books
// paste your find commands here
db.authors.find()
db.books.find()


// Step 6: insert two new books
db.books.insertMany([
  { title: "Dune", published_year: 1965, author_ids: ["author_004"] },
  { title: "The Stranger", published_year: 1942, author_ids: ["author_005"] }
])


// Step 7: add missing authors
db.authors.insertMany([
  {_id: "author_004",name: "Frank Herbert",nationality: "American",bio: {
      short: "American science fiction author best known for Dune.",
      long: "Frank Herbert (1920-1986) was a journalist turned novelist. His 1965 novel Dune won the first Nebula Award and became one of the best-selling science fiction novels ever, known for its themes of ecology, politics, and religion."
    }
  },
  {_id: "author_005",name: "Albert Camus",nationality: "French",bio: {
      short: "French-Algerian novelist and philosopher of the absurd.",
      long: "Albert Camus (1913-1960) was born in French Algeria and wrote The Stranger and The Plague. His philosophy of the absurd explores the search for meaning in an indifferent world. He won the 1957 Nobel Prize in Literature."
    }
  }
])
 

// Step 8: filter books by a list of authors
db.books.find({ author_ids: { $in: ["author_005", "author_004"] } })
